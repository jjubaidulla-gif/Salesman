import streamlit as st
from gtts import gTTS

# 1. அடிப்படை அமைப்புகள்
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
menu = ["முகப்பு", "லென்ஸ் வகைகள் & விலைகள்", "பிராண்டுகள்", "கண் பாதுகாப்பு", "தொடர்புக்கு"]
choice = st.sidebar.selectbox("பகுதியைத் தேர்ந்தெடுக்கவும்", menu)

# --- முகப்பு பக்கம் ---
if choice == "முகப்பு":
    st.title("👁️ டிஜிட்டல் ஆப்டிகல்ஸ் - AI ஆப்")
    try:
        st.image("shop.jpg", use_container_width=True)
    except:
        st.info("shop.jpg அப்லோட் செய்யவும்.")
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
        "Progressive (தூரம் & கிட்டம்)": "₹2,500 முதல்",
        "Contact Lenses (காண்டாக்ட்)": "₹500 முதல்"
    }
    
    for l_name, l_price in lenses.items():
        col1, col2 = st.columns([3, 1])
        with col1:
            st.subheader(l_name)
        with col2:
            st.write(f"**{l_price}**")
        if st.button(f"{l_name} பற்றி கேட்க", key=l_name):
            speak(f"{l_name} லென்ஸ் விலை {l_price} முதல் தொடங்குகிறது.")
        st.divider()

# --- பிராண்டுகள் ---
elif choice == "பிராண்டுகள்":
    st.title("💎 சர்வதேச பிராண்டுகள்")
    st.write("எங்களிடம் உள்ள சிறந்த பிராண்டுகள்:")
    
    brands = {
        "ZEISS": "ஜெர்மனியின் மிகச்சிறந்த லென்ஸ் தொழில்நுட்பம்.",
        "ESSILOR (SLR)": "Crizal மற்றும் வரிலக்ஸ் லென்ஸ்கள்.",
        "HOYA": "ஜப்பானிய தரம் மற்றும் தெளிவு.",
        "NOVA": "நவீன காலத்திற்கான டிஜிட்டல் லென்ஸ்கள்."
    }
    
    for b_name, b_info in brands.items():
        st.subheader(b_name)
        st.write(b_info)
        if st.button(f"{b_name} பற்றி கேட்க", key=b_name):
            speak(f"{b_name} என்பது {b_info}")
        st.divider()

# --- கண் பாதுகாப்பு ---
elif choice == "கண் பாதுகாப்பு":
    st.title("🏥 கண் பாதுகாப்பு குறிப்புகள்")
    st.success("கண்களைப் பாதுகாக்க சில டிப்ஸ்:")
    st.write("1. 20-20-20 விதியைப் பின்பற்றுங்கள்.")
    st.write("2. வருடம் ஒருமுறை கண் பரிசோதனை செய்யுங்கள்.")
    st.write("3. தரமான கூலிங் கிளாஸ் அணியுங்கள்.")
    if st.button("குறிப்புகளை கேட்க"):
        speak("கண்களைப் பாதுகாக்க இருபது இருபது இருபது விதியைப் பின்பற்றுங்கள். மொபைல் பார்க்கும்போது கம்ப்யூட்டர் லென்ஸ் அணியுங்கள்.")

# --- தொடர்புக்கு ---
elif choice == "தொடர்புக்கு":
    st.title("📞 எங்களை அணுக")
    st.write("எங்கள் கடை முகவரி: (உங்கள் முகவரியை இங்கே இடவும்)")
    st.write("போன்: (உங்கள் நம்பர்)")
    st.markdown("[💬 WhatsApp-ல் பேச](https://wa.me/911234567890)") # உங்கள் நம்பரை மாற்றவும் 
