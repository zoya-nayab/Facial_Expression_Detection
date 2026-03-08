import cv2
from deepface import DeepFace

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def detect_expression(frame):
    emotion = "Unknown"
    emotion_scores = {}
    face_coords = None

    # Detect face using OpenCV
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    if len(faces) > 0:
        x, y, w, h = faces[0]
        face_coords = (x, y, w, h)

        try:
            result = DeepFace.analyze(
                frame,
                actions=['emotion'],
                enforce_detection=False
            )
            emotion = result[0]['dominant_emotion']
            emotion_scores = result[0]['emotion']
        except Exception as e:
            print(f"Detection error: {e}")

    return emotion, emotion_scores, face_coords