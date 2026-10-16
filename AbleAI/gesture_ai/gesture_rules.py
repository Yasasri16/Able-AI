def fingers_up(hand_landmarks):
    tips = [4, 8, 12, 16, 20]
    fingers = []

    for tip in tips[1:]:  # ignore thumb
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)

    return fingers


def classify_gesture(hand_landmarks):
    fingers = fingers_up(hand_landmarks)

    if fingers == [1,1,1,1]:
        return "hi"

    elif fingers == [1,1,0,0]:
        return "peace"

    elif fingers == [0,0,0,0]:
        return "help"

    elif fingers == [0,1,0,0]:
        return "pain"

    elif fingers == [1,0,0,0]:
        return "ok"

    return None

