from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///iclepius.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Database and CORS
db = SQLAlchemy(app)
CORS(app)

# Home route - Serves index.html
@app.route("/")
def home():
    return render_template("index.html")

# Import routes AFTER initializing app and db (avoids circular imports)
import routes

# Run Flask app
if __name__ == "__main__":
    app.run(debug=True)
