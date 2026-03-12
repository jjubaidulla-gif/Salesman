import streamlit as st
from gtts import gTTS

st.set_page_config(page_title="Digit Eyes AI Assistant", page_icon="👓", layout="wide")

# 1. ஸ்டைலிங் (CSS) - இது வெப்சைட்டை அழகாக மாற்றும்
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #007bff; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("👓 டிஜிட்டல் ஆப்டிகல்ஸ் - AI விற்பனை உதவியாளர்")

# 2. வாய்ஸ் அசிஸ்டண்ட் செயல்பாடு
def speak(text):
    try:
        tts = gTTS(text=text, lang='ta')
        tts.save("response.mp3")
        st.audio("response.mp3", format="audio/mp3", autoplay=True)
    except:
        st.warning("ஆடியோ பிளே செய்வதில் சிறிய சிக்கல் உள்ளது.")

# கடையின் படம் மற்றும் அறிமுகம்
col_img, col_txt = st.columns([1, 1])
with col_img:
    try:
        st.image("shop.jpg", use_container_width=True)
    except:
        st.info("shop.jpg படம் இல்லை.")
with col_txt:
    st.subheader("சிறந்த முறையில் கண்களைப் பரிசோதிக்கவும், தரமான லென்ஸ்களைப் பெறவும் வாருங்கள்!")
    st.write("எங்கள் AI உதவியாளர் உங்களுக்கு சரியான கண்ணாடியைத் தேர்ந்தெடுக்க உதவுவார்.")

st.divider()

# 3. கஸ்டமர் விபரங்கள் பெறுதல்
st.subheader("🎁 சிறப்புத் தள்ளுபடி பெற பதிவு செய்யுங்கள்")
with st.form("customer_form"):
    name = st.text_input("உங்கள் பெயர்:")
    phone = st.text_input("மொபைல் எண்:")
    if st.form_submit_button("தள்ளுபடி கூப்பன் பெறுக"):
        if name and phone:
            st.success(f"வாழ்த்துகள் {name}! உங்கள் தள்ளுபடி கூப்பன் தயார்.")
        else:
            st.warning("தயவுசெய்து விபரங்களை நிரப்பவும்.")

st.divider()

# 4. AI லென்ஸ் அட்வைசர்
st.subheader("🤖 உங்களுக்கு எந்த லென்ஸ் தேவை?")
options = {
    "கணினி லென்ஸ்": "உங்களுக்கு ப்ளூ கட் லென்ஸ் சிறந்தது. இது கணினித் திரையில் இருந்து வரும் கதிர்களைத் தடுக்கும்.",
    "வெயில் லென்ஸ்": "வெயிலில் கருப்பாக மாறும் போட்டோகுரோமிக் லென்ஸ் உங்களுக்கு வசதியாக இருக்கும்.",
    "அனைத்தும் தெரிந்த லென்ஸ்": "தூரம் மற்றும் கிட்டம் இரண்டையும் ஒரே கண்ணாடியில் பார்க்க புரோகிரசிவ் லென்ஸ் சிறந்தது."
}

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("💻 கணினி பயன்பாடு"):
        msg = options["கணினி லென்ஸ்"]
        st.info(msg)
        speak(msg)
with col2:
    if st.button("☀️ அதிக வெயில்"):
        msg = options["வெயில் லென்ஸ்"]
        st.info(msg)
        speak(msg)
with col3:
    if st.button("👓 தூரம் & கிட்டம்"):
        msg = options["அனைத்தும் தெரிந்த லென்ஸ்"]
        st.info(msg)
        speak(msg)

st.divider()

# 5. வாட்ஸ்அப் இணைப்பு பட்டன்
# உங்கள் கடை போன் நம்பரை 911234567890 என்பதற்கு பதில் இங்கே மாற்றவும்
whatsapp_num = "911234567890" 
st.markdown(f"""
    <a href="https://wa.me/{whatsapp_num}?text=வணக்கம், எனக்கு ஒரு கண்ணாடி தேவைப்படுகிறது" target="_blank">
    <button style="width:100%; height:50px; background-color:#25D366; color:white; border:none; border-radius:10px; font-size:18px; cursor:pointer;">
    💬 வாட்ஸ்அப்பில் எங்களை அழைக்க
    </button></a>
    """, unsafe_allow_html=True)
