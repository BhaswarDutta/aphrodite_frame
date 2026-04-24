import streamlit as st

st.set_page_config(page_title="Aphrodite Frame", page_icon="🖼️", layout="centered")

# Header
st.title("Aphrodite Frame")
st.caption("Make your images Instagram-ready without cropping")

st.divider()

# Main container (acts like your card)
with st.container():
    st.subheader("Upload Image")

    uploaded_file = st.file_uploader("Choose an image", type=["png", "jpg", "jpeg"])

    st.divider()

    st.subheader("Preview")

    if uploaded_file:
        st.image(uploaded_file, use_container_width=True)
    else:
        st.info("Upload an image to see preview")

    st.divider()

    st.subheader("Aspect Ratio")

    ratio = st.radio(
        "Select ratio", ["1:1 (Square)", "4:5 (Portrait)"], horizontal=True
    )

    st.divider()

    process = st.button("Process Image")

    st.divider()

    st.subheader("Download")

    st.button("Download Image", disabled=True)
