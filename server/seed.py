import sys
import os
import csv

# Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from server.base import create_app, db
from server.models import Episode, Guest, Appearance

app = create_app()

def seed():
    with app.app_context():
        print("Resetting database...")
        db.drop_all()
        db.create_all()

        guests = []
        episodes_dict = {}

        print("Seeding guests and episodes from seed.csv...")
        try:
            with open('seed.csv', newline='', encoding='utf-8-sig') as csvfile:
                reader = csv.DictReader(csvfile)
                for i, row in enumerate(reader, start=1):
                    # Create guest
                    guest = Guest(
                        name=row['Raw_Guest_List'],
                        occupation=row['GoogleKnowlege_Occupation']
                    )
                    db.session.add(guest)
                    guests.append(guest)

                    # Create episode if not already created
                    date = row['Show']
                    if date not in episodes_dict:
                        episode = Episode(date=date, number=i)
                        db.session.add(episode)
                        episodes_dict[date] = episode

            db.session.commit()
        except FileNotFoundError:
            print("seed.csv not found.")

        print("Creating sample appearances...")
        # Link first few guests and episodes
        guest_list = Guest.query.limit(2).all()
        episode_list = Episode.query.limit(2).all()

        if guest_list and episode_list:
            appearance1 = Appearance(rating=5, guest_id=guest_list[0].id, episode_id=episode_list[0].id)
            appearance2 = Appearance(rating=4, guest_id=guest_list[1].id, episode_id=episode_list[1].id)
            db.session.add_all([appearance1, appearance2])
            db.session.commit()

        print("✅ Database seeded successfully.")

if __name__ == '__main__':
    seed()
