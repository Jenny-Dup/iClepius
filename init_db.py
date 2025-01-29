from app import app, db

print("Initializing database...")

with app.app_context():
    db.create_all()

print("Database initialized!")
