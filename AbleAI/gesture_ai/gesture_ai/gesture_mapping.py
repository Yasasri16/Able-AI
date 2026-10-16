import json

with open("data/MS-ASL/MSASL_classes.json", "r") as f:
    CLASSES = json.load(f)

def map_gestures(gesture_ids):
    return [CLASSES[str(g)] for g in gesture_ids]
