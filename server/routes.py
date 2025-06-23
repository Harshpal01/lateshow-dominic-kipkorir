from flask import Blueprint, request, jsonify
from server.models import db, Episode, Guest, Appearance

routes = Blueprint('routes', __name__)

# GET /episodes
@routes.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([e.to_dict() for e in episodes]), 200

# GET /episodes/<int:id>
@routes.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return jsonify({"error": "Episode not found"}), 404

    data = episode.to_dict()
    data['appearances'] = [
        {
            "id": a.id,
            "rating": a.rating,
            "guest_id": a.guest_id,
            "episode_id": a.episode_id,
            "guest": a.guest.to_dict()
        } for a in episode.appearances
    ]
    return jsonify(data), 200

# GET /guests
@routes.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([g.to_dict() for g in guests]), 200

# POST /appearances
@routes.route('/appearances', methods=['POST'])
def create_appearance():
    try:
        data = request.get_json()
        rating = data.get('rating')
        episode_id = data.get('episode_id')
        guest_id = data.get('guest_id')

        if not isinstance(rating, int) or rating < 1 or rating > 5:
            return jsonify({"errors": ["Rating must be between 1 and 5"]}), 400

        episode = Episode.query.get(episode_id)
        guest = Guest.query.get(guest_id)

        if not episode or not guest:
            return jsonify({"errors": ["Invalid episode or guest ID"]}), 400

        appearance = Appearance(
            rating=rating,
            episode_id=episode_id,
            guest_id=guest_id
        )

        db.session.add(appearance)
        db.session.commit()

        return jsonify({
            "id": appearance.id,
            "rating": appearance.rating,
            "guest_id": appearance.guest_id,
            "episode_id": appearance.episode_id,
            "episode": episode.to_dict(),
            "guest": guest.to_dict()
        }), 201

    except Exception as e:
        return jsonify({"errors": [str(e)]}), 400

# DELETE /episodes/<int:id>
@routes.route('/episodes/<int:id>', methods=['DELETE'])
def delete_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return jsonify({"error": "Episode not found"}), 404

    db.session.delete(episode)
    db.session.commit()
    return jsonify({}), 204
