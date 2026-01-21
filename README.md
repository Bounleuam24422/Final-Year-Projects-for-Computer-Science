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

### 📊 Model Evaluation Results
| Model Architecture | Training Accuracy | Training Loss | Training Time | Test Accuracy |
| :--- | :---: | :---: | :---: | :---: |
| **ResNet50** | 0.999 | 0.004 | 8h 17m 30s | 0.992 |
| **MobileNetV3-large** | 0.990 | 0.010 | 4h 39m 15s | 0.980 |


## Backend
This project is a real-time drive thdrows and di usingFastAPI, OpenCV, PyTo.
It providesreal-time, visual aler, and audio using pygame.
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
## Fontend
This is the React Frontend for the project Automatic Driver Drowsiness Warning Using Deep Learning.
It connects with the FastAPI backend to display real-time video detection, provide alerts, and present UI in Lao/English.
``` text
frontend/
├── src/
│   ├── assets/             # Static assets (e.g. logo.png)
│   ├── components/         # Reusable components (Header, Footer, etc.)
│   │   ├── Header.jsx
│   │   ├── Footer.jsx
│   ├── pages/              # Main pages
│   │   ├── Detection.jsx
│   │   ├── Home.jsx
│   ├── App.jsx             # Root component
│   ├── main.jsx            # Entry point
│   ├── App.css
│   ├── index.css
│   └── ...
├── index.html
├── package.json
├── tailwind.config.js
└── README.md
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

Backend

Update the paths inside main.py to matc
```text
MODEL_PATH = r"D:\path\to\ResNet50.pth"        # Trained model file
ALERT_SOFT_PATH = r"D:\path\to\alert_soft.mp3" # Soft alert sound
ALERT_HARD_PATH = r"D:\path\to\alert_hard.mp3" # Hard alert sound
FONT_PATH = r"D:\path\to\NUOL95P.ttf"          # Lao font file
```

### ▶️ Running
Backend
``` bash
uvicorn main:app --reload
```
Fontend
``` bash
npm run start
```
# web application GUI
## User Flow
- Start Detection, Stop Camera
- Processed Images
- Analysis Results
- Display Driver Status and Voice Alert
  
<img width="908" height="587" alt="image" src="https://github.com/user-attachments/assets/a025bcff-fd50-438b-b2ad-30ca4892d6bb" />



