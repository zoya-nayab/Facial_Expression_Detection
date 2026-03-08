import cv2
import time
from src.camera import get_camera, release_camera
from src.detector import detect_expression
from src.utils import draw_label, draw_face_box, save_output

def main():
    print("Starting Facial Expression Detection...")
    print("Press 'q' to quit")
    print("Press 's' to save a screenshot")

    cap = get_camera()

    emotion = "Analyzing..."
    scores = {}
    face_coords = None
    last_analysis_time = 0
    interval = 5  # seconds

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        current_time = time.time()

        # Only analyze every 5 seconds
        if current_time - last_analysis_time >= interval:
            emotion, scores, face_coords = detect_expression(frame)
            last_analysis_time = current_time

        # Draw purple box around face
        if face_coords:
            frame = draw_face_box(frame, face_coords)

        # Draw emotion label and bar
        frame = draw_label(frame, emotion, scores)

        # Show countdown timer on screen
        countdown = int(interval - (current_time - last_analysis_time))
        cv2.putText(
            frame,
            f"Next scan in: {countdown}s",
            (50, 140),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (128, 0, 128),
            2
        )

        cv2.imshow("Facial Expression Detection", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            print("Quitting...")
            break
        elif key == ord('s'):
            save_output(frame)
            print("Screenshot saved!")

    release_camera(cap)
    print("Done!")

if __name__ == "__main__":
    main()