from camera_input import get_gestures_from_camera
from model import understand_gestures
from llm_refine import refine_text

print("🎥 Starting Gesture Capture...")
gestures = get_gestures_from_camera()

print("🧠 Raw gestures:", gestures)

tokens = understand_gestures(gestures)
print("✅ Valid tokens:", tokens)

if tokens:
    sentence = refine_text(tokens)
    print("\n🗣 Interpreted Sentence:")
    print(sentence)
else:
    print("❌ No valid gestures detected")
    