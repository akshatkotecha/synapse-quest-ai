import os
from dotenv import load_dotenv

load_dotenv()
print("DEBUG API KEY:", os.getenv("OPENAI_API_KEY"))

from flask import Flask, jsonify, request
from services.code_analysis.code_score_engine import analyze_code_for_task
from flask_cors import CORS
from chat import chat_bp
from alert_engine import generate_alerts
from leaderboard import compute_leaderboard

app = Flask(__name__)
CORS(app)

app.register_blueprint(chat_bp)

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/alerts", methods=["POST"])
def alerts():
    data = request.json
    alerts = generate_alerts(data["user"], data["behavior"], data["task"])
    return jsonify(alerts)

@app.route("/leaderboard", methods=["POST"])
def leaderboard():
    leaderboard = compute_leaderboard(request.json)
    return jsonify(leaderboard)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json

    code = data.get("code")
    task = {
        "title": data.get("title"),
        "expected_outputs": data.get("expected_outputs", [])
    }

    result = analyze_code_for_task(task, code)

    return jsonify(result)
@app.route("/github-webhook", methods=["POST"])
def github_webhook():
    payload = request.json

    commits = payload.get("commits", [])

    for commit in commits:
        message = commit.get("message")
        author = commit.get("author", {}).get("name", "unknown")

        # For now simulate code content
        code = "print('commit detected')"

        task = {
            "title": message,
            "expected_outputs": ["implementation"]
        }

        result = analyze_code_for_task(task, code)

        print(f"Commit by {author} analyzed:", result)

    return jsonify({"status": "processed"})



if __name__ == "__main__":
    app.run(debug=True)
