# iClepius - AI-Powered Symptom Checker

## Overview

**iClepius** is an AI-powered symptom checker designed to help users track their symptoms and receive potential diagnoses based on machine learning models. The goal is to provide a user-friendly and intelligent healthcare assistant that can guide users toward the next steps in managing their health.

### Features:
- ✅ AI-driven symptom analysis and possible diagnosis suggestions *(Coming Soon)*
- ✅ Secure and efficient backend powered by **Flask**
- ✅ User-friendly frontend built with **Tailwind CSS**
- ✅ **SQLite database** for storing user symptoms and tracking history
- ✅ Scalable and modular project structure for future expansions

---

## Tech Stack

iClepius leverages modern web technologies to deliver an intelligent and efficient symptom-checking experience:

| Component  | Technology Used |
|------------|----------------|
| **Backend** | Python, Flask |
| **Frontend** | HTML, JavaScript, Tailwind CSS |
| **Database** | SQLite |
| **AI/ML** | Future integration with AI models for diagnosis prediction |
| **Tools** | DB Browser for SQLite, Flask API, Jinja Templates |

---

## Setup & Installation

Follow these steps to set up **iClepius** locally:

### 1. Clone the repository
```bash
git clone https://github.com/your-username/iclepius.git
cd iclepius
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate  # On Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up the database
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 5. Run the application
```bash
flask run
```

## Usage

- **Enter symptoms:** Users can input their symptoms via a simple and intuitive form.
- **AI Analysis (Upcoming):** The system processes the symptoms and provides potential diagnosis suggestions.
- **Symptom tracking:** Users can log their symptoms over time for better health insights.
- **Next steps recommendation:** The system may suggest seeing a healthcare professional based on severity.

---

## Challenges Faced

Building **iClepius** came with several challenges, including:

- **Database Setup:** Structuring the SQLite database to efficiently handle user input.
- **Flask Backend Configuration:** Ensuring smooth API request handling and proper routing.
- **Tailwind CSS Integration:** Learning how to optimize Tailwind CSS for the UI while keeping styles clean.
- **AI Integration (Upcoming):** Researching and preparing for the integration of an AI model for diagnosis prediction.

---

## Learning Outcomes

Developing **iClepius** has helped solidify my understanding of:

- **Flask Development:** Structuring a Flask application with modular components.
- **Database Management:** Using SQLite for lightweight but effective data storage.
- **Frontend Styling:** Gaining experience with Tailwind CSS for efficient and responsive UI design.
- **AI in Healthcare:** Beginning exploration into AI-powered symptom checking and potential ML model integrations.

---

## Future Improvements

Some planned features and improvements include:

- **User Authentication:** Allowing users to create accounts and store their symptom history securely.
- **AI/ML Integration:** Implementing an AI model to provide more accurate symptom analysis.
- **Mobile Responsiveness:** Enhancing the UI for better mobile device compatibility.
- **Doctor Recommendations:** Suggesting local healthcare providers based on user symptoms.




