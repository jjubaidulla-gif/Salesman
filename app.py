import streamlit as st
from gtts import gTTS

st.set_page_config(page_title="Digit Eyes Catalog", page_icon="👓", layout="wide")

# CSS - ஸ்டைலிங்
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .lens-card { padding: 20px; border-radius: 15px; background-color: white; box-shadow: 2px 2px 10px rgba(0,0,0,0.1); margin-bottom: 20px; }
    .price-tag { color: #28a745; font-weight: bold; font-size: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.title("👓 டிஜிட்டல் ஆப்டிகல்ஸ் - லென்ஸ் விபரங்கள்")

# 1. வாய்ஸ் அசிஸ்டண்ட்
def speak(text):
    try:
        tts = gTTS(text=text, lang='ta')
        tts.save("response.mp3")
        st.audio("response.mp3", format="audio/mp3", autoplay=True)
    except:
        pass

# 2. லென்ஸ் கேட்டலாக் (Data)
lens_data = {
    "Zeiss Lenses": [
        {"name": "Zeiss BlueGuard", "features": "நீல நிறக் கதிர்களைத் தடுக்கும், மிகத் தெளிவான பார்வை.", "price": "₹3,500 - ₹5,000"},
        {"name": "Zeiss PhotoFusion", "features": "வெயிலில் மிக வேகமாக கருப்பாக மாறும் தொழில்நுட்பம்.", "price": "₹6,000 - ₹8,500"},
        {"name": "Zeiss DriveSafe", "features": "இரவு நேர வாகன ஓட்டிகளுக்குச் சிறந்தது.", "price": "₹7,500+"}
    ],
    "SLR / Essilor Lenses": [
        {"name": "Crizal Prevencia", "features": "கண்களுக்குப் பாதுகாப்பு மற்றும் கீறல்கள் விழாத தன்மை.", "price": "₹2,800 - ₹4,500"},
        {"name": "Transitions Gen 8", "features": "அதிவேகமாக நிறம் மாறும் லென்ஸ்.", "price": "₹5,500 - ₹9,000"},
        {"name": "Eyezen", "features": "மொபைல் அதிகம் பயன்படுத்துபவர்களுக்கான சிறப்பு லென்ஸ்.", "price": "₹3,200+"}
    ],
    "Local / Economy Lenses": [
        {"name": "Basic Blue Cut", "features": "சாதாரண கணினி பாதுகாப்பு லென்ஸ்.", "price": "₹800 - ₹1,500"},
        {"name": "ARC Coating Lens", "features": "பிரதிபலிப்பு இல்லாத லென்ஸ்.", "price": "₹600 - ₹1,200"}
    ]
}

# 3. டிஸ்ப்ளே பகுதி
tab1, tab2, tab3 = st.tabs(["💎 Zeiss", "🔬 SLR/Essilor", "💰 Economy"])

with tab1:
    st.header("Zeiss Premium Lenses")
    for lens in lens_data["Zeiss Lenses"]:
        with st.container():
            st.markdown(f"""<div class='lens-card'>
                <h3>{lens['name']}</h3>
                <p>{lens['features']}</p>
                <p class='price-tag'>தோராய விலை: {lens['price']}</p>
                </div>""", unsafe_allow_html=True)
            if st.button(f"பற்றி கேட்க: {lens['name']}", key=lens['name']):
                speak(f"{lens['name']} பற்றி. {lens['features']}. இதன் விலை {lens['price']} முதல் தொடங்குகிறது.")

with tab2:
    st.header("SLR / Essilor Lenses")
    for lens in lens_data["SLR / Essilor Lenses"]:
        with st.container():
            st.markdown(f"""<div class='lens-card'>
                <h3>{lens['name']}</h3>
                <p>{lens['features']}</p>
                <p class='price-tag'>தோராய விலை: {lens['price']}</p>
                </div>""", unsafe_allow_html=True)
            if st.button(f"பற்றி கேட்க: {lens['name']}", key=lens['name']):
                speak(f"{lens['name']} பற்றி. {lens['features']}. இதன் விலை {lens['price']} முதல் தொடங்குகிறது.")

with tab3:
    st.header("Economy Options")
    for lens in lens_data["Local / Economy Lenses"]:
        with st.container():
            st.markdown(f"""<div class='lens-card'>
                <h3>{lens['name']}</h3>
                <p>{lens['features']}</p>
                <p class='price-tag'>தோராய விலை: {lens['price']}</p>
                </div>""", unsafe_allow_html=True)

st.divider()
st.info("குறிப்பு: விலைகள் பவர் (Power) மற்றும் பிரேம்களைப் பொறுத்து மாறுபடலாம்.")
