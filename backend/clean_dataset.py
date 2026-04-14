import pandas as pd

# Load your CSV
df = pd.read_csv("dataset\AI_Human_balanced_dataset.csv")

# Rename column
if "generated" in df.columns:
    df.rename(columns={"generated": "label"}, inplace=True)

# Convert float labels to int
df["label"] = df["label"].astype(int)

# Save cleaned file
df.to_csv("cleaned_data.csv", index=False)

print("✅ Dataset cleaned and saved as cleaned_data.csv")