import streamlit as st
import cv2
import mediapipe as mp

st.set_page_config(page_title="Virtual Try-On", layout="wide")

st.title("🕶️ விர்ச்சுவல் கண்ணாடி ட்ரை-ஆன்")
st.write("கேமராவை ஆன் செய்து கண்ணாடியைப் பொருத்திப் பாருங்கள்.")

# முகத்தைக் கண்டறியும் செட்டப்
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
                # கண்ணின் புள்ளிகளில் ஒரு அடையாளம் காட்ட
                h, w, _ = frame.shape
                lx = int(face_landmarks.landmark[33].x * w)
                ly = int(face_landmarks.landmark[33].y * h)
                rx = int(face_landmarks.landmark[263].x * w)
                ry = int(face_landmarks.landmark[263].y * h)
                
                # ஒரு பச்சை நிறக் கோடு கண்களுக்கு இடையில் (கண்ணாடி வைக்க வேண்டிய இடம்)
                cv2.line(frame, (lx, ly), (rx, ry), (0, 255, 0), 2)
        
        FRAME_WINDOW.image(frame, channels="BGR")
    cap.release()
