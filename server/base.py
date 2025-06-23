from flask import Flask
from server.extensions import db, migrate 
from server.routes import routes  

def create_app():
    app = Flask(__name__)

    # Configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lateshow.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints
    app.register_blueprint(routes)

    @app.route('/')
    def index():
        return {'message': 'Welcome to the Late Show API'}

    return app
