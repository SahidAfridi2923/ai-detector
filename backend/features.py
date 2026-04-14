import numpy as np

def extract_features(text, perplexity):
    words = text.split()

    length = len(words)
    unique_words = len(set(words))

    avg_word_length = np.mean([len(w) for w in words]) if words else 0

    sentence_count = text.count('.') + text.count('!') + text.count('?')
    avg_sentence_length = length / (sentence_count + 1)

    return [
        perplexity,
        length,
        unique_words,
        avg_word_length,
        avg_sentence_length
    ]