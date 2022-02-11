from os import environ

from config import get_env_config, get_logger_config
from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS

from app.models import db, ma
from app.routes import register_blueprints

# ENV Config
ENV = environ.get('ENV', 'LOCAL')
config = get_env_config(ENV)

# Logger Config
logger = get_logger_config()

# App Config
app = Flask(__name__)
CORS(app)

app.config.from_object(config)

# DB Config
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
ma.init_app(app)

# Migrate Config
migrate = Migrate(app, db)


# Register Blueprints
register_blueprints(app)
