import cv2
import torch
import torchvision.transforms as transforms
import torch.nn.functional as F
from torchvision import models
from fastapi.responses import JSONResponse, StreamingResponse, HTMLResponse
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image, ImageFont, ImageDraw
import numpy as np
import mediapipe as mp
import time
import pygame

# ========== CONFIG ==========
MODEL_PATH = r"D:\ບົດຮຽນ\ວິຊາຄົ້ນຄວ້າປີ3\ບົດຈົບຊັ້ນ\USB_Final\Project Final\App\backend\models\ResNet50.pth"
# MODEL_PATH = r"D:\ບົດຮຽນ\ວິຊາຄົ້ນຄວ້າປີ3\ບົດຈົບຊັ້ນ\USB_Final\backend\models\MobileNetV3.pth"
ALERT_SOFT_PATH = r"D:\ບົດຮຽນ\ວິຊາຄົ້ນຄວ້າປີ3\ບົດຈົບຊັ້ນ\USB_Final\Project Final\App\backend\alerts\alert_soft.mp3"
ALERT_HARD_PATH = r"D:\ບົດຮຽນ\ວິຊາຄົ້ນຄວ້າປີ3\ບົດຈົບຊັ້ນ\USB_Final\Project Final\App\backend\alerts\alert_hard.mp3"
FONT_PATH = r"D:\ບົດຮຽນ\ວິຊາຄົ້ນຄວ້າປີ3\ບົດຈົບຊັ້ນ\USB_Final\Project Final\App\backend\fonts\NUOL95P.ttf"
CLASS_NAMES = ['Awake','Distracted', 'Drowsy']
IMG_SIZE = 224
DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

DROWSY_THRESHOLD = 35
DROWSY_COOLDOWN = 8
DISTRACTED_THRESHOLD = 45
DISTRACTED_COOLDOWN = 8



#ໃຊ້ກ້ອງ Camera 
streaming_enabled = False
cap = cv2.VideoCapture(0)
last_drowsy_alert = 0
last_distracted_alert = 0
drowsy_counter = 0
distracted_counter = 0


#ສະລັບໃຊ້ກ້ອງ Iriun Webcam
##===== ຄົ້ນຫາກ້ອງທີ່ໃຊ້ງານໄດ້ອັດຕະໂນມັດ (ຮອງຮັບ Iriun Webcam ຫຼື USB Webcam) =====
# streaming_enabled = False
# def find_available_camera(max_index=5):
#     for i in range(max_index):
#         test_cap = cv2.VideoCapture(i)
#         if test_cap.read()[0]:
#             test_cap.release()
#             print(f"✅ ພົບກ້ອງທີ່ໃຊ້ງານໄດ້: index {i}")
#             return i
#         test_cap.release()
#     print("❌ ບໍ່ພົບກ້ອງທີ່ໃຊ້ງານໄດ້")
#     return -1

# cam_index = find_available_camera()
# if cam_index == -1:
#     raise RuntimeError("❌ ບໍ່ສາມາດເຊື່ອມຕໍ່ກັບກ້ອງໃດໆ ກາລຸນາເຊື່ອມຕໍ່ກ້ອງ ຫຼື ເປີດ Iriun Webcam")

# cap = cv2.VideoCapture(cam_index)

##===== ຕົວປ່ຽນຄວບຄຸມແຈ້ງເຕືອນ =====
last_drowsy_alert = 0
last_distracted_alert = 0
drowsy_counter = 0
distracted_counter = 0

## ========== MODEL LOAD ==========
model = models.resnet50(pretrained=False)
model.fc = torch.nn.Linear(model.fc.in_features, 3)
model.load_state_dict(torch.load(MODEL_PATH, map_location=DEVICE))
model.to(DEVICE).eval()

#Model MobileNetV3-Large
# model = torch.hub.load('pytorch/vision:v0.10.0', 'mobilenet_v3_large', pretrained=False)
# model.classifier[3] = torch.nn.Linear(model.classifier[3].in_features, 3)
# model.load_state_dict(torch.load(MODEL_PATH, map_location=DEVICE))
# model.to(DEVICE).eval()


transform = transforms.Compose([
    transforms.Resize((IMG_SIZE, IMG_SIZE)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

pygame.mixer.init()
try:
    alert_soft = pygame.mixer.Sound(ALERT_SOFT_PATH)
    alert_hard = pygame.mixer.Sound(ALERT_HARD_PATH)
except:
    alert_soft = alert_hard = None

face_detector = mp.solutions.face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.6)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# ========== FASTAPI APP ==========
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
async def index():
    return """
    <h2>Driver Monitor Backend Running...</h2>
    <p>Visit your React frontend to start detection.</p>
    """

def draw_lao_text(img, text, position, font_size=22, color=(0, 0, 255)):
    img_pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(img_pil)
    font = ImageFont.truetype(FONT_PATH, font_size)
    rgb = (color[2], color[1], color[0])
    draw.text(position, text, font=font, fill=rgb)
    return cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)

def predict(image):
    face_pil = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    input_tensor = transform(face_pil).unsqueeze(0).to(DEVICE)
    with torch.no_grad():
        output = model(input_tensor)
        probs = F.softmax(output, dim=1)
        conf, pred = torch.max(probs, 1)
    return CLASS_NAMES[pred.item()], conf.item() * 100

# ========== STREAM ==========
def gen_frames():
    global streaming_enabled, last_drowsy_alert, last_distracted_alert, drowsy_counter, distracted_counter
    while True:
        if not streaming_enabled:
            time.sleep(0.1)
            continue

        success, frame = cap.read()
        if not success:
            continue

        h, w, _ = frame.shape
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        label, conf = "Unknown", 0
        face_crop, box = None, None

        results = face_detector.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        if results.detections:
            biggest = sorted(results.detections, key=lambda d: d.location_data.relative_bounding_box.width * d.location_data.relative_bounding_box.height, reverse=True)[0]
            bbox = biggest.location_data.relative_bounding_box
            x_m, y_m = int(bbox.xmin * w), int(bbox.ymin * h)
            w_m, h_m = int(bbox.width * w), int(bbox.height * h)
            margin = 40
            x1, y1 = max(0, x_m - margin), max(0, y_m - margin)
            x2, y2 = min(w, x_m + w_m + margin), min(h, y_m + h_m + margin)
            head_crop = frame[y1:y2, x1:x2]
            label, conf = predict(head_crop)
            face_crop = head_crop
            box = (x1, y1, x2, y2)

        if label != 'Distracted':
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            if len(faces) > 0:
                x, y, fw, fh = max(faces, key=lambda b: b[2]*b[3])
                face_crop = frame[y:y+fh, x:x+fw]
                label, conf = predict(face_crop)
                box = (x, y, x+fw, y+fh)

        if face_crop is not None and box:
            color = (0, 255, 0) if label == 'Awake' else (255, 0, 0)
            cv2.rectangle(frame, (box[0], box[1]), (box[2], box[3]), color, 2)
            cv2.putText(frame, f"{label} ({conf:.1f}%)", (box[0], box[1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

            # Drowsy section
        now = time.time()
        if label == 'Drowsy':
            drowsy_counter += 1
            # Only play drowsy alert if distracted alert is not playing
            if (drowsy_counter >= DROWSY_THRESHOLD and
                now - last_drowsy_alert > DROWSY_COOLDOWN and
                not pygame.mixer.Channel(1).get_busy()):  # Channel 1 is for distracted alert
                last_drowsy_alert = now
                if alert_hard:
                    pygame.mixer.Channel(0).play(alert_hard)
        else:
            drowsy_counter = 0

        # Distracted section
        if label == 'Distracted':
            distracted_counter += 1
            # Only play distracted alert if drowsy alert is not playing
            if (distracted_counter >= DISTRACTED_THRESHOLD and
                now - last_distracted_alert > DISTRACTED_COOLDOWN and
                not pygame.mixer.Channel(0).get_busy()):  # Channel 0 is for drowsy alert
                last_distracted_alert = now
                if alert_soft:
                    pygame.mixer.Channel(1).play(alert_soft)
        else:
            distracted_counter = 0

        # ===== Status Text =====
        if label == 'Awake':
            frame = draw_lao_text(frame, "ສະຖານະ: ມີສະຕິ", (10, 30), font_size=36, color=(0, 255, 0))
        elif label == 'Drowsy':
            frame = draw_lao_text(frame, "ສະຖານະ: ເຫງົານອນ!", (10, 30), font_size=36, color=(0, 0, 255))
        elif label == 'Distracted':
            frame = draw_lao_text(frame, "ສະຖານະ: ບໍ່ມີສະມາທິ!", (10, 30), font_size=36, color=(0, 165, 255))

        # _, jpeg = cv2.imencode('.jpg', frame)
        # yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')
        if face_crop is None or box is None:
            frame = draw_lao_text(frame, "ສະຖານະ: ບໍ່ພົບ", (10, 30),
                                font_size=36, color=(255, 255, 255))

        _, jpeg = cv2.imencode('.jpg', frame)
        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')

@app.get("/video_feed")
def video_feed():
    return StreamingResponse(gen_frames(), media_type="multipart/x-mixed-replace; boundary=frame")

@app.get("/start")
def start_stream():
    global streaming_enabled
    streaming_enabled = True
    return JSONResponse(content={"status": "started"})

@app.get("/stop")
def stop_stream():
    global streaming_enabled
    streaming_enabled = False
    return JSONResponse(content={"status": "stopped"})


