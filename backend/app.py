from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return "CodexHub AI Backend is running 🚀"

@app.route("/api/files/create", methods=["POST"])
def create_file():
    data = request.get_json()
    name = data.get("name")
    content = data.get("content")

    # Save file
    save_path = os.path.join("files", name)
    os.makedirs("files", exist_ok=True)
    with open(save_path, "w") as f:
        f.write(content)

    return jsonify({"message": f"{name} saved successfully"}), 201

if __name__ == "__main__":
    app.run(debug=True)

import base64
import requests

@app.route("/api/vision/scan", methods=["POST"])
def scan_image():
    data = request.get_json()
    image_data = data.get("image")
    if not image_data:
        return jsonify({"error": "Image data missing"}), 400

    # Gemini Vision Pro API call
    api_key = os.environ.get("GEMINI_API_KEY")
    headers = {"Content-Type": "application/json"}
    body = {
        "contents": [
            {
                "parts": [
                    {"inline_data": {"mime_type": "image/png", "data": image_data}},
                    {"text": "What code or problem do you detect in this image?"}
                ]
            }
        ]
    }

    response = requests.post(
        f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro-vision:generateContent?key={api_key}",
        headers=headers,
        json=body
    )

    if response.status_code == 200:
        reply = response.json()["candidates"][0]["content"]["parts"][0]["text"]
        return jsonify({"explanation": reply}), 200
    else:
        return jsonify({"error": "Failed to analyze image"}), 500

