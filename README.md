## Late Show API
This is a Flask-based RESTful API that manages data for The Late Show guests, episodes, and their appearances. It allows you to fetch, add, and delete information about show guests and their appearances.

## Project Structure
lateshow-dominic-kipkorir/
│
├── server/
│   ├── base.py             # App factory and app setup
│   ├── models.py           # SQLAlchemy models
│   ├── routes.py           # API route handlers
│   ├── extensions.py       # Shared db & migrate instances (if separated)
│   └── seed.py             # Database seeding script
│
├── migrations/             # Flask-Migrate folder (auto-generated)
├── seed.csv                # Optional CSV data source
├── app.py                  # Entrypoint for running the Flask server
├── Pipfile                 # Pipenv dependency file
├── Pipfile.lock            # Pipenv lock file
└── README.md               # Project documentation

## Getting Started
1. Clone the Repository
git clone https://github.com/your-username/lateshow-dominic-kipkorir.git
cd lateshow-dominic-kipkorir

2. Set Up a Virtual Environment
pipenv install
pipenv shell

4. Run Migrations
export FLASK_APP=app.py
flask db upgrade

If not initialized yet:
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

5. Seed the Database
python server/seed.py

6. Start the Server
python app.py

## API Endpoints
Episodes
GET /episodes — List all episodes

GET /episodes/<int:id> — Retrieve episode details

DELETE /episodes/<int:id> — Delete an episode

Guests
GET /guests — List all guests

Appearances
POST /appearances — Create a new guest appearance
Example body:
{
  "rating": 4,
  "guest_id": 1,
  "episode_id": 2
}

## Testing with Postman
Use the provided challenge-4-lateshow.postman_collection.json to test endpoints.
Make sure the server is running on port 5555 or update Postman settings accordingly.

## Notes
The app uses SQLite for simplicity.

Data is optionally loaded from seed.csv if available.

All relationships are bidirectional and cascade-safe.

## Author
Dominic Kipkorir