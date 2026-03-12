
import streamlit as st

st.title("வணக்கம்! 👓")
st.header("எங்கள் கடைக்கு வரவேற்பு")

# கடையின் படம் (இது வேலை செய்ய shop.jpg என்ற பெயரில் படம் இருக்க வேண்டும்)
try:
    st.image("shop.jpg", caption="எங்கள் டிஜிட்டல் ஆப்டிகல்ஸ்", use_container_width=True)
except:
    st.warning("கடையின் படம் (shop.jpg) இன்னும் அப்லோட் செய்யப்படவில்லை.")

st.write("---")

# லென்ஸ் விபரங்கள்
col1, col2 = st.columns(2)

with col1:
    st.subheader("Blue Cut Lens")
    try:
        st.image("bluecut.jpg")
    except:
        st.info("bluecut.jpg படம் இல்லை.")

with col2:
    st.subheader("Photochromic")
    try:
        st.image("photo.jpg")
    except:
        st.info("photo.jpg படம் இல்லை.")
