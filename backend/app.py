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
