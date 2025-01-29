from flask import request, jsonify
from app import app, db
from models import User, Symptom
import openai

# Set OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

# User CRUD Routes
@app.route("/api/users", methods=["POST"])
def create_user():
    data = request.json
    new_user = User(
        name=data['name'],
        email=data['email'],
        age=data.get('age'),
        medical_history=data.get('medical_history', '')
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created successfully", "user": {"id": new_user.id, "name": new_user.name}}), 201

@app.route("/api/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([
        {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "age": user.age,
            "medical_history": user.medical_history
        }
        for user in users
    ]), 200

# Symptom CRUD Routes
@app.route("/api/symptoms", methods=["POST"])
def add_symptoms():
    data = request.json
    user_id = data['user_id']
    symptoms = data['symptoms']
    for symptom in symptoms:
        new_symptom = Symptom(user_id=user_id, symptom=symptom)
        db.session.add(new_symptom)
    db.session.commit()
    return jsonify({"message": "Symptoms added successfully"}), 201

@app.route("/api/symptoms", methods=["GET"])
def get_symptoms():
    symptoms = Symptom.query.all()
    return jsonify([
        {
            "id": symptom.id,
            "user_id": symptom.user_id,
            "symptom": symptom.symptom,
            "date": symptom.date
        }
        for symptom in symptoms
    ]), 200

@app.route("/api/symptoms/<int:symptom_id>", methods=["DELETE"])
def delete_symptom(symptom_id):
    symptom = Symptom.query.get_or_404(symptom_id)
    db.session.delete(symptom)
    db.session.commit()
    return jsonify({"message": "Symptom deleted successfully"}), 200

@app.route("/api/reset", methods=["DELETE"])
def reset_symptoms():
    try:
        db.session.query(Symptom).delete()
        db.session.commit()
        return jsonify({"message": "All symptoms have been reset"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# AI-Powered Diagnosis Route
@app.route("/api/diagnose", methods=["POST"])
def diagnose():
    data = request.json
    symptoms = data.get("symptoms", [])

    if not symptoms:
        return jsonify({"error": "No symptoms provided"}), 400

    print(f"✅ Received Symptoms: {symptoms}")

    prompt = f"I am experiencing the following symptoms: {', '.join(symptoms)}. What are the possible medical conditions associated with these symptoms?"

    try:
        print("🔍 Sending request to OpenAI API...")

        client = openai.OpenAI(api_key=OPENAI_API_KEY)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a medical assistant helping users understand possible diagnoses based on their symptoms."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=200,
            temperature=0.7
        )

        diagnosis = response.choices[0].message.content.strip()

        return jsonify({"diagnosis": diagnosis}), 200

    except Exception as e:
        print(f"❌ ERROR in AI Diagnosis: {e}")
        return jsonify({"error": f"Unable to generate diagnosis: {str(e)}"}), 500
