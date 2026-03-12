import streamlit as st

# இணையதளத்தின் தலைப்பு
st.set_page_config(page_title="டிஜிட்டல் ஆப்டிகல்ஸ்", page_icon="👓")

st.title("வணக்கம்! 👓")
st.header("எங்கள் கடைக்கு வரவேற்பு")

# 1. கடையின் படம் (shop.jpg உங்கள் GitHub-ல் உள்ளது)
try:
    st.image("shop.jpg", caption="எங்கள் டிஜிட்டல் ஆப்டிகல்ஸ்", use_container_width=True)
except:
    st.error("shop.jpg என்ற படம் கிடைக்கவில்லை.")

st.write("---")

# 2. லென்ஸ் விபரங்கள் (lens.jpg உங்கள் GitHub-ல் உள்ளது)
st.subheader("சிறப்பு லென்ஸ் வகைகள்")

col1, col2 = st.columns(2)

with col1:
    try:
        st.image("lens.jpg", caption="Blue Cut Lens")
        st.write("கம்ப்யூட்டர் பார்ப்பவர்களுக்கு சிறந்தது.")
    except:
        st.info("lens.jpg படம் அப்லோட் செய்யப்படவில்லை.")

with col2:
    st.subheader("Photochromic")
    st.write("வெயிலில் கருப்பாக மாறும் லென்ஸ்.")
    st.info("இதற்கான படத்தை photo.jpg என்ற பெயரில் அப்லோட் செய்யவும்.")

# 3. ஆஃபர் பட்டன்
if st.button('இன்றைய ஆஃபர்கள்'):
    st.success("இன்று அனைத்து லென்ஸ்களுக்கும் 20% தள்ளுபடி!")

st.sidebar.info("தொடர்புக்கு: உங்கள் கடை முகவரி இங்கே.")
