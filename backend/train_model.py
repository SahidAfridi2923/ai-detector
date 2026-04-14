import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

from model import AIDetector
from features import extract_features

# Load dataset
df = pd.read_csv("final_data.csv").sample(3000, random_state=42)

# Initialize detector (for perplexity)
detector = AIDetector()

X = []
y = df['label']

print("⏳ Extracting features... (this may take time)")

# Feature extraction
for i, text in enumerate(df['text']):
    print(f"Processing {i+1}/{len(df)}")

    if not isinstance(text, str) or len(text.strip()) == 0:
        continue

    try:
        perplexity = detector.calculate_perplexity(text[:500])  # limit length
        features = extract_features(text, perplexity)
        X.append(features)
    except Exception as e:
        print(f"Skipping row {i} due to error:", e)


# Convert to DataFrame (safe)
X = pd.DataFrame(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y[:len(X)], test_size=0.2, random_state=42
)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"✅ Accuracy: {accuracy * 100:.2f}%")

# Save model
with open("ml_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("🎯 Model trained and saved as ml_model.pkl")