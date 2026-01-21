# Final-Year-Projects-for-Computer-Science
Hi I am pleased to present my senior project, 'Automatic Driver Drowsiness Warning Using Deep Learning'. 
Developed during the 2024-2025 academic year at the Faculty of Natural Sciences,
this project reflects my core interest in Computer Science 


# For model creation, the architectural backbones used were
ResNet50 and MobileNetV3-Large
both of which are Convolutional Neural Networks (CNNs)

# The results show that the model built with
- ResNet50 achieved a test accuracy of 99.2% with a 0.43% error rate
- MobileNetV3-Large achieved a test accuracy of 98% with a 0.3% error rate. 


This project is a real-time drive thdrows and di usingFastAPI, OpenCV, PyTo.
It providesreal-time, visual aler, and audio using pygame.

## Backend
### Project Structure

```text
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
```

### 📦 Requiremen
Backend

- Python 3.8
- GPU su
- Webcam or Iriun W
  
Fontend
- Node.js v16+
- npm v8+

# 🔧 Installation
## Backend
### 1. Create a virtual
```text
python -m venv venv
source venv/bin/activate    # macOS / Linux
venv\Scripts\activate       # Windows
```

### 2. Install dependencies
Backend
```bash
pip install -r requirements.txt
```
Fontend
React
``` bash
npm install react react-dom
```

Vite + React plugin
``` bash
npm install -D vite @vitejs/plugin-react
```
TailwindCSS + PostCSS + Autoprefixer
``` bash
npm install -D tailwindcss postcss autoprefixer
```
If missing, initialize Tailwind:
``` bash
npx tailwindcss init -p
```
### ⚙️ Config

Update the paths inside main.py to matc
```text
MODEL_PATH = r"D:\path\to\ResNet50.pth"        # Trained model file
ALERT_SOFT_PATH = r"D:\path\to\alert_soft.mp3" # Soft alert sound
ALERT_HARD_PATH = r"D:\path\to\alert_hard.mp3" # Hard alert sound
FONT_PATH = r"D:\path\to\NUOL95P.ttf"          # Lao font file
```
### ▶️ Running the Backend

``` bash
uvicorn main:app --reload
```


📦 Requirements

Node.js v16+

npm v8+

Backend API running at http://localhost:8000

1. Install dependencies
# React
npm install react react-dom

# Vite + React plugin
npm install -D vite @vitejs/plugin-react

# TailwindCSS + PostCSS + Autoprefixer
npm install -D tailwindcss postcss autoprefixer


If missing, initialize Tailwind:

npx tailwindcss init -p

Running the Frontend

Start the development server:

npm run dev


The app will run on:

http://localhost:5173

📡 API Integration

The frontend connects to the FastAPI backend:

GET /start → Start detection

GET /stop → Stop detection

GET /video_feed → Fetch video stream

Make sure the backend is running on http://localhost:8000

📊 Features

🎥 Real-time webcam streaming

🚨 Driver drowsiness & distraction alerts

🌐 UI in Lao + English

🎨 TailwindCSS styled interface (Header, Footer, Detection Box)

🖼️ Screenshots (Optional)

(You can add later with actual UI screen
