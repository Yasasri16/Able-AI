import cv2
import mediapipe as mp
import requests

from gesture_ai.gesture_rules import classify_gesture
from gesture_ai.model import understand_gestures
from gesture_ai.llm_refine import refine_text

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

def send_to_backend(sentence):
    url = "http://localhost:8000/process-gesture"
    payload = {"sentence": sentence}
    requests.post(url, json=payload)

cap = cv2.VideoCapture(0)
tokens = []

with mp_hands.Hands(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
) as hands:

    print("Show gestures. Press Q to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(frame_rgb)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                mp_draw.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS
                )

                gesture = classify_gesture(hand_landmarks)
                if gesture:
                    tokens.append(gesture)
                    print("Detected:", gesture)

        cv2.imshow("Gesture Recognition", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()

tokens = list(set(tokens))
print("Tokens:", tokens)

if tokens:
    sentence = refine_text(tokens)
    print("Sentence:", sentence)
    send_to_backend(sentence)
