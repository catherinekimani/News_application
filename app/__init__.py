from ensurepip import bootstrap
from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def create_app(config_name):
    
    app = Flask(__name__)
    
    # creating app configuration
    app.config.from_object(config_options[config_name])
    
    # Registering blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    # initializing bootstrap
    bootstrap.init_app(app)
    # setting config
    from .requests import configure_request
    configure_request(app)
    
    
    return app