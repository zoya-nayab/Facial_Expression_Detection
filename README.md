😊 Facial Expression Detection
A real-time facial expression detection app built with Python, OpenCV, and DeepFace. Detects your face through webcam and analyzes your emotion every 5 seconds with a live progress bar.

📸 Features
•	Real-time webcam feed
•	Purple bounding box around detected face
•	Dominant emotion display with percentage bar
•	Analyzes emotion every 5 seconds with countdown timer
•	Screenshot saving with s key

🛠️ Tech Stack
•	Python 3.10
•	OpenCV — webcam capture & face detection
•	DeepFace — emotion analysis
•	TensorFlow / Keras — deep learning backend
•	NumPy / Matplotlib — data handling & visualization

📁 Project Structure
facial-expression-detection/
│
├── .venv/                  # Virtual environment
├── src/
│   ├── __init__.py
│   ├── detector.py         # Emotion detection logic
│   ├── camera.py           # Webcam handling
│   └── utils.py            # Drawing utilities
├── models/                 # Custom models (if any)
├── assets/                 # Test images/videos
├── outputs/                # Saved screenshots
├── main.py                 # Entry point
├── requirements.txt        # Dependencies
└── README.md

⚙️ Setup & Installation
1. Clone the repository
git clone https://github.com/your-username/facial-expression-detection.git
cd facial-expression-detection
2. Create virtual environment
python -m venv .venv
3. Activate virtual environment
# Windows
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate
4. Install dependencies
pip install -r requirements.txt

▶️ Run the Project
python main.py

🎮 Controls
Key	Action
q	Quit the application
s	Save screenshot to /outputs

📦 Requirements
Install all dependencies with:
pip install opencv-python deepface tensorflow tf-keras numpy matplotlib pillow

🤖 How It Works
1.	Webcam captures live video feed
2.	OpenCV detects face and draws a purple bounding box
3.	Every 5 seconds, DeepFace analyzes the dominant emotion
4.	A purple progress bar shows the confidence percentage
5.	A countdown timer shows when the next scan will happen

📊 Detected Emotions
•	😊 Happy
•	😢 Sad
•	😠 Angry
•	😨 Fear
•	😲 Surprise
•	🤢 Disgust
•	😐 Neutral

🙌 Acknowledgements
•	DeepFace by Sefik Ilkin Serengil
•	OpenCV
•	TensorFlow

📄 License
This project is open source and available under the MIT License.

