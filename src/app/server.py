from flask import Flask
from dotenv import load_dotenv

load_dotenv()

from src.app.routes.agent import agent_bp
from src.app.routes.health import health_bp
from src.app.routes.auth import auth_bp

def create_app() -> Flask:
    app = Flask(__name__)

    app.register_blueprint(health_bp)
    app.register_blueprint(agent_bp, url_prefix="/agent")
    app.register_blueprint(auth_bp, url_prefix="/auth")

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
