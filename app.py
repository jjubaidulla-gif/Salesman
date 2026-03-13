import streamlit as st
from gtts import gTTS
import os

# 1. அடிப்படை அமைப்புகள் (முக்கியம்: இதுதான் முதல் வரியாக இருக்க வேண்டும்)
st.set_page_config(page_title="Digit Eyes Real App", page_icon="👁️", layout="wide")

# 2. வாய்ஸ் அசிஸ்டண்ட் பங்க்ஷன்
def speak(text):
    try:
        tts = gTTS(text=text, lang='ta')
        tts.save("response.mp3")
        st.audio("response.mp3", format="audio/mp3", autoplay=True)
    except:
        st.warning("ஆடியோ பிளே செய்ய முடியவில்லை.")

# 3. சைடு மெனு (Sidebar)
st.sidebar.title("டிஜிட்டல் ஆப்டிகல்ஸ்")
st.sidebar.info("விர்ச்சுவல் ட்ரை-ஆன் செய்ய இடதுபக்க மெனுவில் 'Virtual Try On' என்பதைத் தேர்ந்தெடுக்கவும்.")

menu = ["முகப்பு", "லென்ஸ் வகைகள் & விலைகள்", "பிராண்டுகள்", "கண் பாதுகாப்பு", "தொடர்புக்கு"]
choice = st.sidebar.selectbox("பகுதியைத் தேர்ந்தெடுக்கவும்", menu)

# --- முகப்பு பக்கம் ---
if choice == "முகப்பு":
    st.title("👁️ டிஜிட்டல் ஆப்டிகல்ஸ் - AI ஆப்")
    st.header("வரவேற்பு!")
    st.write("உங்கள் கண்களுக்கான சிறந்த தீர்வுகளை இங்கே பெறலாம். வாய்ஸ் அசிஸ்டண்ட் வசதியுடன் எங்களை அணுகுங்கள்.")
    if st.button("வரவேற்பு செய்தியை கேட்க"):
        speak("டிஜிட்டல் ஆப்டிகல்ஸ் உங்களை அன்புடன் வரவேற்கிறது. சிறந்த லென்ஸ் வகைகளைத் தேர்ந்தெடுக்க மெனுவைப் பார்க்கவும்.")

# --- லென்ஸ் வகைகள் & விலைகள் ---
elif choice == "லென்ஸ் வகைகள் & விலைகள்":
    st.title("🔍 லென்ஸ் கேட்டலாக்")
    lenses = {
        "Single Vision (சாதாரண)": "₹600 முதல்",
        "Blue Cut (கம்ப்யூட்டர்)": "₹1,200 முதல்",
        "Photochromic (நிறம் மாறும்)": "₹1,800 முதல்",
        "Progressive (தூரம் & கிட்டம்)": "₹2,500 முதல்"
    }
    for l_name, l_price in lenses.items():
        col1, col2 = st.columns([3, 1])
        with col1: st.subheader(l_name)
        with col2: st.write(f"**{l_price}**")
        if st.button(f"{l_name} பற்றி கேட்க", key=l_name):
            speak(f"{l_name} லென்ஸ் விலை {l_price} முதல் தொடங்குகிறது.")
        st.divider()

# --- மற்ற பகுதிகள் (சுருக்கமாக) ---
elif choice == "கண் பாதுகாப்பு":
    st.title("🏥 கண் பாதுகாப்பு குறிப்புகள்")
    st.write("1. 20-20-20 விதியைப் பின்பற்றுங்கள். 2. வருடம் ஒருமுறை கண் பரிசோதனை செய்யுங்கள்.")
    if st.button("குறிப்புகளை கேட்க"):
        speak("கண்களைப் பாதுகாக்க இருபது இருபது இருபது விதியைப் பின்பற்றுங்கள்.")
