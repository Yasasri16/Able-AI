import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data", "MS-ASL")

with open(os.path.join(DATA_DIR, "MSASL_classes.json"), "r") as f:
    GESTURE_CLASSES = set(json.load(f))

with open(os.path.join(DATA_DIR, "MSASL_synonym.json"), "r") as f:
    raw_synonyms = json.load(f)

GESTURE_SYNONYMS = {}
for item in raw_synonyms:
    if isinstance(item, list) and len(item) > 1:
        GESTURE_SYNONYMS[item[0]] = item[1:]

def normalize_gesture(gesture):
    gesture = gesture.lower()
    for canonical, synonyms in GESTURE_SYNONYMS.items():
        if gesture == canonical or gesture in synonyms:
            return canonical
    return gesture

def understand_gestures(gestures):
    understood = []
    for g in gestures:
        g_norm = normalize_gesture(g)
        if g_norm in GESTURE_CLASSES:
            understood.append(g_norm)
    return understood
