"""
model.py
---------
Gesture Understanding Model (NO ML, NO LLM)

Uses MS-ASL vocabulary for validation and normalization.
"""

import json
import os

# -----------------------
# Load MS-ASL metadata
# -----------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data", "MS-ASL")

CLASSES_FILE = os.path.join(DATA_DIR, "MSASL_classes.json")
SYNONYM_FILE = os.path.join(DATA_DIR, "MSASL_synonym.json")

# MSASL_classes.json is a LIST
with open(CLASSES_FILE, "r") as f:
    GESTURE_CLASSES = set(json.load(f))

with open(SYNONYM_FILE, "r") as f:
    GESTURE_SYNONYMS = json.load(f)

# -----------------------
# Normalize gestures
# -----------------------
def normalize_gesture(gesture):
    gesture = gesture.lower()
    for canonical, synonyms in GESTURE_SYNONYMS.items():
        if gesture in synonyms:
            return canonical
    return gesture

# -----------------------
# Core understanding logic
# -----------------------
def understand_gestures(gestures):
    understood = []

    for g in gestures:
        g_norm = normalize_gesture(g)
        if g_norm in GESTURE_CLASSES:
            understood.append(g_norm)

    return understood

# -----------------------
# Test
# -----------------------
if __name__ == "__main__":
    test_input = ["Doctor", "Appointment", "Help"]
    print("Input:", test_input)
    print("Understood:", understand_gestures(test_input))
