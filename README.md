# Final-Year-Projects-for-Computer-Science
Hi I am pleased to present my senior project, 'Automatic Driver Drowsiness Warning Using Deep Learning'. 
Developed during the 2024-2025 academic year at the Faculty of Natural Sciences,
this project reflects my core interest in Computer Science 


# For model creation, the architectural backbones used were
- ResNet50
- MobileNetV3-Large
  
both of which are Convolutional Neural Networks (CNNs)

### 📊 Model Evaluation Results
| Model Architecture | Training Accuracy | Training Loss | Training Time | Test Accuracy |
| :--- | :---: | :---: | :---: | :---: |
| **ResNet50** | 0.999 | 0.004 | 8h 17m 30s | 0.992 |
| **MobileNetV3-large** | 0.990 | 0.010 | 4h 39m 15s | 0.980 |

# Project Structure
## Backend
This project is a real-time drive thdrows and di usingFastAPI, OpenCV, PyTo.
It providesreal-time, visual aler, and audio using pygame.

```text
backend/
├── app/main.py                # FastAPI Backend
├── models/ResNet50.pth, MobileNetV3.pth    # Trained model file
├── alerts/
│   ├── alert_soft.mp3
│   └── alert_hard.mp3
├── fonts/
│   └── NUOL95P.ttf
├── requirements.txt
└── README.md
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
```bash
uvicorn main:app --reload
```
Fontend
```bash
npm run start
```

# User Flow

1 Start Detection, Stop Camera

2 Processed Images

3 Analysis Results

4 Display Driver Status and Voice Alert
  
<img width="908" height="587" alt="image" src="https://github.com/user-attachments/assets/a025bcff-fd50-438b-b2ad-30ca4892d6bb" />

# Web Application GUI
## Home page

1 Start detection button (ປຸ່ມເລີ່ມ)
<img width="888" height="526" alt="image" src="https://github.com/user-attachments/assets/a989b8ca-62e3-45a2-93de-bd92c28ae061" />

## Results page

1 Prediction Display Area (ພື້ນທີ່ສະແດງຜົນການພະຍາກອນ)

2 Display Status and Prediction Accuracy (ສະແດງສະຖານະ ແລະ ຄວາມແໝ້ນຍຳ)

3 Display Driver's Current Status (ສະແດງສະຖານະປັດຈຸບັນຂອງຜູ້ຂັບຂີ່)

4 Close Camera Button (ປຸ່ມປິດກ້ອງ)

<img width="893" height="435" alt="image" src="https://github.com/user-attachments/assets/f0e61704-94b6-465e-91d1-6238d3cc4c0c" />

## Detection Result

Drowsy Detected

<img width="902" height="585" alt="image" src="https://github.com/user-attachments/assets/e2af7973-3567-4bc9-8c6a-8dfc648f9943" />

Distracted Detected

<img width="902" height="475" alt="image" src="https://github.com/user-attachments/assets/db47f206-f746-447e-8051-a0c54160521d" />


