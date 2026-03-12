import streamlit as st
from streamlit_mic_recorder import mic_recorder
from gtts import gTTS
import os

st.set_page_config(page_title="Voice AI Optical Assistant", page_icon="🎙️")

st.title("டிஜிட்டல் ஆப்டிகல்ஸ் - Voice AI 🤖")

# வாய்ஸ் பதில் சொல்லும் செயல்பாடு
def speak(text):
    tts = gTTS(text=text, lang='ta')
    tts.save("response.mp3")
    st.audio("response.mp3", format="audio/mp3", autoplay=True)

st.write("மைக் பட்டனை அழுத்திப் பேசுங்கள் (உதாரணம்: கம்ப்யூட்டர் லென்ஸ்)")

# மைக் ரெக்கார்டர்
audio = mic_recorder(start_prompt="பேச இங்கே அழுத்தவும் 🎤", stop_prompt="நிறுத்த அழுத்தவும் 🛑", key='recorder')

if audio:
    # இங்கே நாம் எளிமையான கீவேர்ட் மேட்ச் பயன்படுத்துகிறோம்
    # குறிப்பு: முழுமையான AI ஸ்பீச்-டு-டெக்ஸ்ட்-க்கு இன்னும் கூடுதல் செட்டப் தேவைப்படும்
    # இப்போதைக்கு பட்டன் மூலம் வாய்ஸ் கேட்கும் வசதி:
    
    st.success("உங்கள் கேள்வி கேட்கப்பட்டது!")

st.write("---")
st.subheader("கேள்விகளைத் தேர்ந்தெடுத்துப் பதிலைக் கேளுங்கள்:")

options = {
    "கணினி லென்ஸ் பற்றி": "கணினி மற்றும் மொபைல் பயன்படுத்துபவர்களுக்கு ப்ளூ கட் லென்ஸ் மிகவும் சிறந்தது. இது உங்கள் கண்களைப் பாதுகாக்கும்.",
    "வெயில் லென்ஸ் பற்றி": "வெயிலில் செல்லும்போது கருப்பாக மாறும் போட்டோகுரோமிக் லென்ஸ் உங்களுக்கு வசதியாக இருக்கும்.",
    "ஆஃபர் விபரங்கள்": "இன்று எங்கள் கடையில் அனைத்து பிரேம்களுக்கும் இருபது சதவீத தள்ளுபடி உள்ளது."
}

choice = st.selectbox("கேள்வியைத் தேர்ந்தெடுக்கவும்:", ["தேர்ந்தெடுங்கள்..."] + list(options.keys()))

if choice != "தேர்ந்தெடுங்கள்...":
    response_text = options[choice]
    st.info(f"🤖 {response_text}")
    speak(response_text) # இது தானாகவே தமிழில் பேசும்

st.image("shop.jpg", use_container_width=True)
