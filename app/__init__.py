from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

# Initialize extensions
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions with the app
    db.init_app(app)
    login_manager.init_app(app)

    # Set login view for @login_required redirects (optional)
    login_manager.login_view = 'auth.login'  # You can adjust this later

    # Import and register blueprints/routes here later
    # from .routes import main as main_blueprint
    # app.register_blueprint(main_blueprint)

    return app
