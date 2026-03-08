import cv2

def draw_label(frame, emotion, scores):
    # Draw dominant emotion text
    cv2.putText(
        frame,
        f"Emotion: {emotion.upper()}",
        (50, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.2,
        (128, 0, 128),  # Purple
        2
    )

    # Draw only the dominant emotion's progress bar
    if emotion in scores:
        percent = scores[emotion]
        bar_x, bar_y = 50, 80
        bar_width = 300
        filled_width = int((percent / 100) * bar_width)

        # Background bar (dark purple)
        cv2.rectangle(frame, (bar_x, bar_y), (bar_x + bar_width, bar_y + 25), (50, 0, 50), -1)

        # Filled bar (bright purple)
        cv2.rectangle(frame, (bar_x, bar_y), (bar_x + filled_width, bar_y + 25), (128, 0, 128), -1)

        # Percentage text on bar
        cv2.putText(
            frame,
            f"{round(percent, 1)}%",
            (bar_x + bar_width + 10, bar_y + 18),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (128, 0, 128),
            2
        )

    return frame

def draw_face_box(frame, face_coords):
    x, y, w, h = face_coords
    # Purple square box around face
    cv2.rectangle(frame, (x, y), (x + w, y + h), (128, 0, 128), 2)
    return frame

def save_output(frame, path="outputs/result.jpg"):
    cv2.imwrite(path, frame)
    print(f"Saved to {path}")