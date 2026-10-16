import cv2

def get_gestures_from_camera():
    cap = cv2.VideoCapture(0)
    gestures = []

    print("Press:")
    print(" D → Doctor")
    print(" A → Appointment")
    print(" H → Help")
    print(" Q → Quit")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow("Camera", frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord('d'):
            gestures.append("doctor")
            print("Detected: doctor")

        elif key == ord('a'):
            gestures.append("appointment")
            print("Detected: appointment")

        elif key == ord('h'):
            gestures.append("help")
            print("Detected: help")

        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return gestures
