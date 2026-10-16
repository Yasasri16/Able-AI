import re
import nltk
from nltk.corpus import stopwords

# Download once
nltk.download('stopwords')

STOP_WORDS = set(stopwords.words('english'))


def clean_text(text: str) -> str:
    """
    Basic cleaning:
    - Lowercase
    - Remove special characters
    - Normalize spaces
    """
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def remove_stopwords(text: str) -> str:
    """
    Remove common stopwords
    (optional but useful for ML intent detection)
    """
    tokens = text.split()
    filtered = [word for word in tokens if word not in STOP_WORDS]
    return " ".join(filtered)


def normalize_sentence(text: str) -> str:
    """
    Fix broken sentence structure lightly
    """
    text = clean_text(text)
    text = text.capitalize()
    if not text.endswith("."):
        text += "."
    return text


def preprocess_text(text: str, remove_stops: bool = False) -> str:
    """
    Main preprocessing pipeline
    """
    text = normalize_sentence(text)
    if remove_stops:
        text = remove_stopwords(text)
    return text


# Test
if __name__ == "__main__":
    sample = "me head pain no sleep days!!!"
    print("Original:", sample)
    print("Processed:", preprocess_text(sample))