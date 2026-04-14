import pandas as pd

# Load both datasets
df1 = pd.read_csv("cleaned_data.csv")
df2 = pd.read_csv("data.csv")

# Ensure same column names
df2.rename(columns={"text": "text", "label": "label"}, inplace=True)

# Convert labels to int (safety)
df1["label"] = df1["label"].astype(int)
df2["label"] = df2["label"].astype(int)

# Merge datasets
final_df = pd.concat([df1, df2], ignore_index=True)

# Shuffle dataset (VERY IMPORTANT)
final_df = final_df.sample(frac=1).reset_index(drop=True)

# Save final dataset
final_df.to_csv("final_data.csv", index=False)

print("✅ Merged dataset saved as final_data.csv")
print("Total samples:", len(final_df))
print(final_df["label"].value_counts())