import streamlit as st
import mediapipe as mp
from PIL import Image
import numpy as np

# முகத்தைக் கண்டறியும் அமைப்பை உருவாக்குதல்
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=True)

st.title("🕶️ எளிய கண்ணாடி ட்ரையான் (No OpenCV)")

# 1. கண்ணாடி படத்தை அப்லோட் செய்தல் (PNG)
glass_file = st.sidebar.file_uploader("கண்ணாடி PNG படத்தை பதிவேற்றவும்", type=['png'])

# 2. வாடிக்கையாளர் புகைப்படம்
user_file = st.camera_input("உங்கள் முகத்தை புகைப்படம் எடுங்கள்")

if glass_file and user_file:
    # படங்களைத் திறத்தல்
    user_img = Image.open(user_file).convert("RGB")
    glass_img = Image.open(glass_file).convert("RGBA")
    
    # மெடிபைப் புரியும்படி படத்தை மாற்றுதல்
    img_array = np.array(user_img)
    results = face_mesh.process(img_array)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            # இடது கண் (33) மற்றும் வலது கண் (263) புள்ளிகள்
            h, w, _ = img_array.shape
            lx = int(face_landmarks.landmark[33].x * w)
            ly = int(face_landmarks.landmark[33].y * h)
            rx = int(face_landmarks.landmark[263].x * w)
            ry = int(face_landmarks.landmark[263].y * h)

            # கண்ணாடியின் அகலத்தைக் கணக்கிடுதல்
            eye_dist = abs(rx - lx)
            glass_width = int(eye_dist * 2.3) # முகத்திற்கு ஏற்ப மாற்றிப் பார்க்கலாம்
            glass_height = int(glass_width * (glass_img.height / glass_img.width))

            # கண்ணாடியை Resize செய்தல் (Pillow பயன்படுத்தி)
            resized_glass = glass_img.resize((glass_width, glass_height))

            # முகத்தில் சரியான இடத்தில் பொருத்துதல்
            # மூக்கின் மேல் பகுதிக்கு (Landmark 6) இணையாக வைப்போம்
            nx = int(face_landmarks.landmark[6].x * w)
            ny = int(face_landmarks.landmark[6].y * h)
            
            offset_x = nx - (glass_width // 2)
            offset_y = ny - (glass_height // 2)

            # அசல் படத்தின் மேல் கண்ணாடியை ஒட்டுதல்
            user_img.paste(resized_glass, (offset_x, offset_y), resized_glass)
            
            st.image(user_img, caption="அற்புதம்! கண்ணாடி சரியாகப் பொருந்துகிறது.", use_container_width=True)
    else:
        st.warning("முகம் சரியாகத் தெரியவில்லை. வெளிச்சமான இடத்தில் மீண்டும் முயலவும்.")
