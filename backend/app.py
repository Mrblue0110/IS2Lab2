from flask import Flask, jsonify

app = Flask(__name__)

# Dummy event data
EVENTS = [
    {"id": 1, "title": "Hackathon 2025", "date": "2025-11-15"},
    {"id": 2, "title": "AI Workshop", "date": "2025-12-01"},
]

def create_app():
    app = Flask(__name__)


    @app.route("/api/events")
    def get_events():
        return jsonify(EVENTS)

    return app

# Optional: allow local dev python backend/app.py
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)