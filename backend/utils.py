import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def text_features(text):
    words = text.split()

    if len(words) == 0:
        return {
            "length": 0,
            "unique_words": 0,
            "repetition_ratio": 0
        }

    unique_words = len(set(words))

    return {
        "length": len(words),
        "unique_words": unique_words,
        "repetition_ratio": round(len(words) / (unique_words + 1), 2)
    }