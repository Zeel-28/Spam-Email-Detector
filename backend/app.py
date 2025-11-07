from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)  # Allow frontend access

with open("backend/model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    message = data.get("message", "")
    if not message:
        return jsonify({"error": "No message provided"}), 400
    prediction = model.predict([message])[0]
    print(f"Prediction for message: {prediction}")
    return jsonify({"prediction": prediction})

@app.route("/")
def home():
    return "✅ Spam Email Detector Backend Running"

if __name__ == "__main__":
    app.run(debug=True)
