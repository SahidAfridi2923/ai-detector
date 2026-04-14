from flask import Flask, request, jsonify
from flask_cors import CORS
import os

from model import AIDetector
from utils import clean_text, text_features
from voice import get_voice_input   # 🎤 voice module

app = Flask(__name__)
CORS(app)

# Load model once
detector = AIDetector()


# Health check
@app.route("/", methods=["GET"])
def home():
    return "🚀 AI Detector Backend is Running"


# Text Analysis API
@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.get_json()

        # ✅ Validate input
        if not data or "text" not in data:
            return jsonify({"error": "No text provided"}), 400

        text = data["text"]

        if not isinstance(text, str) or len(text.strip()) == 0:
            return jsonify({"error": "Empty or invalid text"}), 400

        # Clean text
        clean = clean_text(text)

        # Extract features (for UI display)
        features = text_features(clean)

        # Predict
        prediction = detector.predict(clean)

        return jsonify({
            "mode": "text",
            "label": prediction["label"],
            "confidence": prediction["confidence"],
            "features": features
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Voice Analysis API (LOCAL USE ONLY)
@app.route("/voice-analyze", methods=["GET"])
def voice_analyze():
    try:
        # 🎤 Capture voice
        text = get_voice_input()

        if not text:
            return jsonify({"error": "Could not understand voice"}), 400

        # Clean text
        clean = clean_text(text)

        # Extract features
        features = text_features(clean)

        # Predict
        prediction = detector.predict(clean)

        return jsonify({
            "mode": "voice",
            "text": text,
            "label": prediction["label"],
            "confidence": prediction["confidence"],
            "features": features
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Run server (local + deployment ready)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)