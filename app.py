from flask import Flask, jsonify
import os
import requests

app = Flask(__name__)
BACKEND_API_URL = os.environ.get("BACKEND_API_URL", "http://backend-api:5000")

@app.route("/")
def index():
    try:
        r = requests.get(f"{BACKEND_API_URL}/comments")
        return jsonify({"frontend": "ok", "backend": r.json()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
