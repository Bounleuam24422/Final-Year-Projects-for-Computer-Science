# Final-Year-Projects-for-Computer-Science
Hi I am pleased to present my senior project, 'Automatic Driver Drowsiness Warning Using Deep Learning'. 
Developed during the 2024-2025 academic year at the Faculty of Natural Sciences,
this project reflects my core interest in Computer Science 

This research aims to study and implement a driver drowsiness detection system, 
which addresses a critical factor contributing to road accidents in society. By employing 
driver drowsiness analysis techniques, the system detects whether the driver is in an 
Awake, Drowsy, or Distracted state. This, in turn, is intended to significantly enhance 
road safety. 

For model creation, the architectural backbones used were
ResNet50 and MobileNetV3-Large, 
both of which are Convolutional Neural Networks (CNNs). For the web application development, JavaScript (React Framework) was used for the frontend to display the UI,
leveraging HTML/CSS (Tailwind Framework) for styling. 
The backend is responsible for streaming data to the frontend, developed using Python (FastAPI Framework) to create APIs for real-time inference. 
The trained models were then integrated into this web application to provide automated driver drowsiness alerts. 

The results show that the model built with ResNet50 achieved a test accuracy of 
99.2% with a 0.43% error rate, while the model using MobileNetV3-Large achieved a 
test accuracy of 98% with a 0.3% error rate. 

The developed web application allows users 
to activate their camera directly on the website, enabling the model to automatically 
predictthedriver'sdrowsinessstate


This project is a real-time drive thdrows and di usingFastAPI, OpenCV, PyTo.
It providesreal-time, visual aler, and audio using pygame.

📂 Recommended Pro
project/
├── main.py                # FastAPI Backend
├── models/ResNet50.pth    # Trained model file
├── alerts/
│   ├── alert_soft.mp3
│   └── alert_hard.mp3
├── fonts/
│   └── NUOL95P.ttf
├── requirements.txt
└── frontend/              # React Frontend
📦 Requiremen

Python 3.8

GPU su

Webcam or Iriun W

🔧 Installation

1. Create a virtual
python -m venv venv
source venv/bin/activate    # macOS / Linux
venv\Scripts\activate       # Windows


2. Install depe
pip install -r requirements.txt


If requirements.txt does

fastapi
uvicorn
opencv-python
torch
torchvision
pillow
pygame
mediapipe
numpy

⚙️ Config

Update the paths inside main.py to matc

MODEL_PATH = r"D:\path\to\ResNet50.pth"        # Trained model file
ALERT_SOFT_PATH = r"D:\path\to\alert_soft.mp3" # Soft alert sound
ALERT_HARD_PATH = r"D:\path\to\alert_hard.mp3" # Hard alert sound
FONT_PATH = r"D:\path\to\NUOL95P.ttf"          # Lao font file

▶️ Running the Backend

S

uvicorn main:app --reload


For deployment (accessible fr

uvicorn main:app --host 0.0.0.0 --port 8000

📡 API En

GET / → Bac

GET /start → Sta

GET /stop → Stop detec

GET /video_feed →_

🖥️ React Frontend Integration

Build a React component (e.g., DetectionBox.jsx) to disp

http://localhost:8000/video_feed


Use buttons t

/start → Start

/stop → Stop streami

Backend wil

📊 Outpu

Awake → Green box +ສະຖານະ: ມີສະຕິ

Drowsy → Red bສະຖານະ: ເຫງົານອນ! + Hard al

Distracted → Orangeສະຖານະ: ບໍ່ມີສະມາທິ! + S

No Face → Wສະຖານະ: ບໍ່ພົບ
# Installation

