import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import pickle
from features import extract_features


class AIDetector:
    def __init__(self):
        # Load tokenizer + model FIRST
        self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        self.gpt_model = GPT2LMHeadModel.from_pretrained("gpt2")
        self.gpt_model.eval()

        # Setup device AFTER model is created
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.gpt_model.to(self.device)

        # Load ML model (if exists)
        try:
            with open("ml_model.pkl", "rb") as f:
                self.ml_model = pickle.load(f)
        except:
            self.ml_model = None

    def calculate_perplexity(self, text):
        inputs = self.tokenizer(
            text, return_tensors="pt", truncation=True, max_length=512
        ).to(self.device)

        with torch.no_grad():
            outputs = self.gpt_model(**inputs, labels=inputs["input_ids"])

        return torch.exp(outputs.loss).item()

    def predict(self, text):
        perplexity = self.calculate_perplexity(text)
        features = extract_features(text, perplexity)

        if self.ml_model:
            prediction = self.ml_model.predict([features])[0]
            confidence = self.ml_model.predict_proba([features])[0].max()
        else:
            prediction = 0
            confidence = 0.5

        return {
            "label": "AI Generated" if prediction == 1 else "Human Written",
            "confidence": round(confidence * 100, 2),
        }