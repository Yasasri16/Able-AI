from transformers import pipeline

intent_classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

# Define possible intents
INTENTS = [
    "clarify unclear text",
    "expressing emotions",
    "asking for help",
    "general statement"
]

def detect_intent(text):
    result = intent_classifier(text, INTENTS)
    top_intent = result["labels"][0]
    confidence = round(result["scores"][0], 2)

    return top_intent, confidence


# Test
if __name__ == "__main__":
    samples = [
        "me head pain no sleep days",
        "I feel very anxious",
        "please help me understand this",
        "today weather is good"
    ]

    for s in samples:
        intent, score = detect_intent(s)
        print(f"Text: {s}")
        print(f"Intent: {intent} ({score})\n")