import base64
import time

import cv2, os
import threading
from typing import List, Callable
import flet as ft
import tensorflow as tf
from tensorflow.keras.applications.efficientnet import preprocess_input
from pathlib import Path
from datetime import datetime
import numpy as np


IMG_SIZE = (224, 224)
SAVE_DIR = "captured_paddy"
os.makedirs(SAVE_DIR, exist_ok=True)



# BASE_DIR = Path(__file__).resolve().parent.parent
# MODEL_PATH = BASE_DIR / "models" / "paddy_3class_shadow_model.h5"

# model = tf.keras.models.load_model(MODEL_PATH, compile=False)

model = tf.keras.models.load_model("models/paddy_3class_shadow_model.h5",compile=False)
CLASS_NAMES = ["Hmawbi", "Karenma", "Thai"]
CONF_THRESHOLD = 65  # minimum confidence for a class

class CameraController:
    def __init__(self,state,image : ft.Image , src : int = 0, max_cameras: int = 5):
        self.max_cameras = max_cameras
        self.cameras: List[int] = []
        self.scanning: bool = False

        self.state = state
        self.image = image
        self.src = src
        self._running = False # opencv stream
        self._thread = None
        self.cap = None
        self.fps = 30

    def start(self) -> None:
        """
        Start the camera thread
        :return:
        """
        if self._running:
            return

        self.cap = cv2.VideoCapture(self.src)
        if not self.cap.isOpened(): #if video capture is not open
            raise RuntimeError(f'Could not open camera {self.src}')
        self._running = True
        self._thread = threading.Thread(target=self._run, daemon=True)
        self._thread.start()



    def _run(self):

        delay = 1 / max(1,self.fps)
        while self._running and self.cap.isOpened():
            ret, frame = self.cap.read()
            if not ret:
                break

            frame = cv2.flip(frame,1)
            self.frame  = frame 
            success  , buf = cv2.imencode('.jpg', frame)
            if not success:
                continue

            b64 = base64.b64encode(buf).decode('utf-8')
            self.image.src_base64 = b64
            self.image.update()
            # self.image.visible = True
            self.image.update()
            self.state.update()
            time.sleep(delay)



    def classifiy(self):
        
        if not hasattr(self, "frame"):
            return

        frame = self.frame.copy()
        print("frame_here")
        # Preprocess
        img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img_resized = cv2.resize(img_rgb, IMG_SIZE)
        img_input = np.expand_dims(img_resized, axis=0)
        img_input = preprocess_input(img_input)

        # Predict
        pred = model.predict(img_input, verbose=0)[0]
        class_index = int(np.argmax(pred))
        confidence = pred[class_index] * 100

        if confidence >= CONF_THRESHOLD:
            label = f"{CLASS_NAMES[class_index]} {confidence:.1f}%"
            color = (0, 255, 0)
        else:
            label = "UNCERTAIN"
            color = (0, 0, 255)

        # Draw on frame
        cv2.putText(
            frame,
            label,
            (10, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.2,
            color,
            3,
        )

        # Save image
        filename = datetime.now().strftime("%Y%m%d_%H%M%S") + ".jpg"
        cv2.imwrite(os.path.join(SAVE_DIR, filename), frame)

        # print(f"📸 Captured: {filename} → {label}")

        # Update Flet image
        _, buf = cv2.imencode(".jpg", frame)
        self.image.src_base64 = base64.b64encode(buf).decode()
        self.image.update()
        print("data label is ",label)
        return label

    def stop(self):
        self._running = False
        if self._thread:
            self._thread.join(timeout=1)

        if self.cap is not None:
            self.cap.release()
        self.image.src_base64 = ""
        # self.image.visible = False
        self.image.update()
        self.image.update()






    def scan_cameras(self, callback: Callable[[List[int]], None] = None):
        """
        Scan available cameras in a background thread.
        Calls the callback with the list of found camera indices.
        """

        def scan():
            self.scanning = True
            found = []
            for i in range(self.max_cameras):
                cap = cv2.VideoCapture(i)
                if cap.isOpened():
                    found.append(i)
                    cap.release()
            self.cameras = found
            self.scanning = False
            if callback:
                callback(found)

        threading.Thread(target=scan, daemon=True).start()
