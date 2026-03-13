import streamlit as st
import cv2
import mediapipe as mp
import numpy as np

st.set_page_config(page_title="Virtual Try-On Zone", layout="wide")

st.title("🕶️ விர்ச்சுவல் கண்ணாடி உலகம்")
st.info("உங்கள் முகத்தைக் காட்டவும், கண்ணாடிகள் தானாகப் பொருந்தும்.")

# 1. முகத்தைக் கண்டறியும் செட்டப் (Face Mesh)
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)

run = st.toggle('கேமராவைத் தொடங்கு')
FRAME_WINDOW = st.image([])

if run:
    cap = cv2.VideoCapture(0)
    while run:
        ret, frame = cap.read()
        if not ret: break
        
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(rgb_frame)

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                # கண்களின் புள்ளிகளைக் கண்டறிதல் (Landmarks)
                # இந்த புள்ளிகள் கண்ணாடி எங்கு இருக்க வேண்டும் என்பதைத் தீர்மானிக்கும்
                h, w, c = frame.shape
                # வலது கண் மற்றும் இடது கண் புள்ளிகள்
                p1 = face_landmarks.landmark[33]
                p2 = face_landmarks.landmark[263]
                
                cx, cy = int(p1.x * w), int(p1.y * h)
                cv2.circle(frame, (cx, cy), 5, (0, 255, 0), -1) # ஒரு அடையாளத்திற்காக பச்சை வட்டம்
        
        FRAME_WINDOW.image(frame, channels="BGR")
    cap.release()
