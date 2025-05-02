import streamlit as st
from PIL import Image
import os
import io
import dekodowanie
import kodowanie

#app title
st.set_page_config(page_title="Stego Encoder/Decoder", page_icon="🖼️", layout="centered")

#site style
st.markdown("""
    <style>
    .stApp {
        background-color: #121212;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🖼️ Image Text Steganography")
st.caption("Upload a PNG or JPG image. JPG allows only encoding. Output will always be PNG.")

#upload box
uploaded_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

#process uploaded file
if uploaded_file:
    img_format = uploaded_file.type
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption="Uploaded Image", use_container_width=True)

    is_png = img_format == "image/png"
    col1, col2 = st.columns(2)

#decoding section
    with col1:
        #if not png decode button is disabled
        decode_disabled = not is_png
        if decode_disabled:
            st.button("🔓 Decode (PNG only)", disabled=True)
            st.caption("🔒 Decoding is only supported for PNG files.")
        else:
            if st.button("🔓 Decode"):
                decoded = dekodowanie.dekodowanie(img.copy())
                st.subheader("Decoded Text:")
                st.code(decoded.replace("\\n", "\n"))

#coding section
    with col2:
        #input box
        text_to_encode = st.text_area("Enter text to encode:")

        if st.button("🔐 Encode"):
            if text_to_encode:
                #processing img
                encoded_img = kodowanie.kodowanie(text_to_encode, img.copy())
                st.subheader("Modified Image (PNG format):")
                st.image(encoded_img, caption="Image with Encoded Text", use_container_width=True)
                buf = io.BytesIO()
                encoded_img.save(buf, format="PNG")

                #filename handling
                filename = uploaded_file.name
                base_name = os.path.splitext(filename)[0]
                mod_filename = f"{base_name}_mod.png"

                #download button
                st.download_button("💾 Download Encoded Image", data=buf.getvalue(), file_name=mod_filename, mime="image/png")

            else:
                st.warning("Please enter some text to encode.")
