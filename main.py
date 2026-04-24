import io

import streamlit as st
from PIL import Image

from processing import process_image

st.set_page_config(page_title="Aphrodite Frame", page_icon="🖼️", layout="centered")

# ------------------ Session State ------------------
if "processed_image" not in st.session_state:
    st.session_state.processed_image = None

if "last_file" not in st.session_state:
    st.session_state.last_file = None

# ------------------ Header ------------------
st.markdown(
    """
    <h1 style='text-align: center; margin-bottom: 0;'>Aphrodite Frame</h1>
    <p style='text-align: center; color: gray; margin-top: 5px;'>
        Make your images Instagram-ready without cropping
    </p>
    """,
    unsafe_allow_html=True,
)
st.divider()

# ------------------ Upload ------------------
uploaded_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

# Reset processed image if new file
if uploaded_file != st.session_state.last_file:
    st.session_state.processed_image = None
    st.session_state.last_file = uploaded_file

# ------------------ Aspect Ratio ------------------
ratio = st.radio("Aspect Ratio", ["1:1 (Square)", "4:5 (Portrait)"], horizontal=True)

st.divider()

# ------------------ Process ------------------
process_clicked = st.button("Process Image")

if uploaded_file and process_clicked:
    image = Image.open(uploaded_file)
    ratio_key = "1:1" if "1:1" in ratio else "4:5"
    st.session_state.processed_image = process_image(image, ratio_key)

# ------------------ Preview ------------------
st.subheader("Preview")

if st.session_state.processed_image:
    st.image(st.session_state.processed_image, use_container_width=True)
elif uploaded_file:
    st.image(uploaded_file, use_container_width=True)
else:
    st.info("Upload an image to see preview")

st.divider()

# ------------------ Download ------------------
st.subheader("Download")

if st.session_state.processed_image:
    buf = io.BytesIO()
    st.session_state.processed_image.save(buf, format="PNG")
    byte_im = buf.getvalue()

    st.download_button(
        label="Download Image",
        data=byte_im,
        file_name="aphrodite_frame.png",
        mime="image/png",
    )
else:
    st.button("Download Image", disabled=True)
    st.caption("Process an image to enable download")
