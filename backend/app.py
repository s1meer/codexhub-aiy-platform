from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/files/create", methods=["POST"])
def create_file():
    data = request.get_json()
    name = data.get("name")
    content = data.get("content")

    try:
        with open(name, "w") as f:
            f.write(content)
        return jsonify({"message": f"{name} saved successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/", methods=["GET"])
def home():
    return "CodexHub AI Backend is running 🚀"

if __name__ == "__main__":
    app.run(debug=True)
