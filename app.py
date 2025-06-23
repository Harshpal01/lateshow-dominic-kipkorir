from flask import Flask
from flask_migrate import Migrate
from server.models import db
from server.routes import routes 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lateshow.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(routes)

@app.route('/')
def index():
    return { "message": "Late Show API" }

if __name__ == '__main__':
    app.run(debug=True, port=5555)
