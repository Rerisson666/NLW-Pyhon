from flask import Flask
from src.main import tags_routes_bp

app = Flask(__name__)

app.register_blueprint(tags_routes_bp)

