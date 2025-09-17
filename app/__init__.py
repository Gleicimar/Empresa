from bson import ObjectId
from flask import Flask
from config import Config
from flask_talisman import Talisman
from flask_wtf import CSRFProtect

csrf = CSRFProtect()
from flask_login import LoginManager

login_manager = LoginManager()

UPLOAD_FOLDER ='static/uploads'

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    Talisman(app, content_security_policy=None)
    csrf.init_app(app)
    login_manager.init_app(app)
    
    # user_loader obrigatório
    @login_manager.user_loader
    def load_user(user_id):
        return users.get(user_id)
    # blueprint
    from .routes.routes import main 

    app.register_blueprint(main)
    
    return app