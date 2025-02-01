from flask import Flask, render_template
from flask_cors import CORS
from dotenv import load_dotenv
import os
from extensions import db

load_dotenv()


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///iclepius.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    CORS(app)

    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError("❌ ERROR: OPENAI_API_KEY is missing! Check your .env file.")

    from routes import routes
    app.register_blueprint(routes)

    @app.route("/")
    def home():
        return render_template("index.html")

    return app

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)
