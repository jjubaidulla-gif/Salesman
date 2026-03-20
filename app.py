import streamlit as st
import cv2
import numpy as np
import mediapipe as mp
from PIL import Image

st.set_page_config(page_title="Optical Shop VTO", layout="centered")
st.title("👓 உங்கள் முகத்திற்கு ஏற்ற கண்ணாடியைத் தேர்வு செய்யுங்கள்")

# முகத்தைக் கண்டறியும் டூல் (Mediapipe)
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=True)

# 1. கண்ணாடிப் படத்தை அப்லோட் செய்தல் (உங்கள் கடையின் கண்ணாடி)
# ஒருமுறை அப்லோட் செய்தால் போதும்
glass_file = st.sidebar.file_uploader("கண்ணாடி PNG படத்தை பதிவேற்றவும்", type=['png'])

# 2. வாடிக்கையாளர் புகைப்படம்
user_file = st.camera_input("உங்கள் முகத்தை புகைப்படம் எடுங்கள்")

if glass_file and user_file:
    # படங்களை கம்ப்யூட்டர் புரியும் படி மாற்றுதல்
    user_img = Image.open(user_file)
    user_img = np.array(user_img)
    
    glass_img = Image.open(glass_file).convert("RGBA")
    
    # முகத்தில் புள்ளிகளைக் கண்டறிதல்
    results = face_mesh.process(cv2.cvtColor(user_img, cv2.COLOR_RGB2BGR))
    
    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            # இடது மற்றும் வலது கண் புள்ளிகள் (Points 33 & 263)
            left_eye = face_landmarks.landmark[33]
            right_eye = face_landmarks.landmark[263]
            
            # கண்களுக்கு இடைப்பட்ட தூரம் (Width calculation)
            h, w, _ = user_img.shape
            lx, ly = int(left_eye.x * w), int(left_eye.y * h)
            rx, ry = int(right_eye.x * w), int(right_eye.y * h)
            
            glass_width = int(abs(rx - lx) * 2.5) # கண்ணாடியின் அளவு
            glass_height = int(glass_width * (glass_img.height / glass_img.width))
            
            # கண்ணாடியை Resize செய்தல்
            resized_glass = glass_img.resize((glass_width, glass_height))
            
            # முகத்தில் சரியான இடத்தில் பொருத்துதல் (Overlay)
            user_pil = Image.fromarray(user_img)
            offset = (lx - int(glass_width/4), ly - int(glass_height/2))
            user_pil.paste(resized_glass, offset, resized_glass)
            
            st.image(user_pil, caption="உங்கள் புதிய லுக்!", use_container_width=True)
    else:
        st.error("முகம் சரியாகத் தெரியவில்லை. வெளிச்சத்தில் மீண்டும் முயலவும்.")
