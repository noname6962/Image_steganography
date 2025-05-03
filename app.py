import streamlit as st
from PIL import Image
import html
import os
import io
import dekodowanie
import kodowanie
import crypto

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
uploaded_file = st.file_uploader("Upload Image", accept_multiple_files=False)

if uploaded_file:
    try:
        #makes extentions lowercase befor streamlit check extention so it doesnt panic
        ext = os.path.splitext(uploaded_file.name)[1].lower()
        if ext not in [".png", ".jpg", ".jpeg"]:
            st.error("Only PNG and JPG/JPEG files are supported.")

        else:
            #process uploaded file
            img = Image.open(uploaded_file)
            img.verify()  # Check for corruption
            uploaded_file.seek(0)  # Reset file pointer after verify
            img = Image.open(uploaded_file).convert("RGB")
            st.image(img, caption="Uploaded Image", use_container_width=True)
            st.success("✅ Image successfully loaded.")

            #max encoding message lenght
            max_chars = (img.width // 16) * (img.height // 16)
            if max_chars < 1:
                st.warning("⚠️ Image is too small to encode even a single character.")

            col1, col2 = st.columns(2)
            is_png = ext == ".png"
            #decoding section
            with col1:
                #if not png decode button is disabled
                decode_disabled = not is_png
                if decode_disabled:
                    st.button("🔓 Decode (PNG only)", disabled=True)
                    st.caption("🔒 Decoding is only supported for PNG files.")

                else:
                    #passwword for xor encryption
                    password = st.text_input("Enter password for decryption", type="password")

                    if st.button("🔓 Decode"):
                        try:
                            decoded = dekodowanie.dekodowanie(img.copy())
                            if not password:
                                st.warning("⚠️ Please enter a password to decrypt.")
                            else:
                                decrypted = crypto.xor_decrypt(decoded, password)
                                st.subheader("Decrypted Message:")
                                st.code(html.escape(decrypted.replace("\\n", "\n")))

                        except Exception as e:
                            st.error("❌ Decoding failed:" + str(e))

            #encoding section
            with col2:
                #input box
                text_to_encode = html.escape(st.text_area("Enter text to encode:"))
                password = st.text_input("Enter password for encryption", type="password")

                if st.button("🔐 Encode"):
                    max_chars = (img.width // 16) * (img.height // 16)
                    if len(text_to_encode) > max_chars:
                        st.error("Max message length for this image: " + str(max_chars) + " characters")
                    elif not text_to_encode:
                        st.warning("⚠️ Please enter some text to encode.")
                    else:
                        try:
                            #processing img
                            text_to_encode = crypto.xor_encrypt(text_to_encode, password)
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

                        except Exception as e:
                            st.error("Encoding Failed: " + str(e))

    except Exception as e:
        st.error("failed to proccess image: " + str(e))
