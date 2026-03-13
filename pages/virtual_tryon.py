import streamlit as st
import cv2
import mediapipe as mp

# எரர் வராமல் இருக்க இந்த வரிசைப்படி கொடுக்கவும்
mp_face_mesh = mp.solutions.face_mesh
# இப்போதைக்கு இதை மட்டும் மாற்றுங்கள்
face_mesh = mp_face_mesh.FaceMesh(
    static_image_mode=False,
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)
