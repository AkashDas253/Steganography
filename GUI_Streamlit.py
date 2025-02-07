import streamlit as st
import cv2
import numpy as np
from PIL import Image
from encrypt import encode_message
from decrypt import decode_message
from utils import xor_encrypt_decrypt
import io

# Streamlit App Configuration
st.set_page_config(page_title="🔐 Image Steganography", layout="centered")

# Title
st.title("🔐 Image Steganography App")
st.write("Hide and retrieve secret messages inside images securely.")

# Sidebar Navigation
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Choose an Option", ["🔒 Encrypt Message", "🔑 Decrypt Message"])

# Encryption Page
if menu == "🔒 Encrypt Message":
    st.header("🔒 Encrypt a Message into an Image")

    # File Upload
    uploaded_file = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])
    message = st.text_area("Enter the Secret Message")
    password = st.text_input("Enter a Password", type="password")

    if uploaded_file and message and password:
        if st.button("🔐 Encrypt and Save Image"):
            try:
                # Convert uploaded file to NumPy array
                image_bytes = uploaded_file.read()
                image_array = np.frombuffer(image_bytes, np.uint8)
                img = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

                if img is None:
                    st.error("Invalid image file. Please upload a valid image.")
                else:
                    # Encrypt message
                    encrypted_msg = xor_encrypt_decrypt(message, password)
                    encoded_img = encode_message(img.copy(), encrypted_msg)

                    # Convert to PIL image for display
                    encoded_pil = Image.fromarray(cv2.cvtColor(encoded_img, cv2.COLOR_BGR2RGB))
                    st.image(encoded_pil, caption="🔍 Encrypted Image", use_container_width=True)

                    # Save the encrypted image
                    img_encoded_bytes = cv2.imencode(".png", encoded_img)[1].tobytes()
                    st.download_button("📥 Download Encrypted Image", img_encoded_bytes, file_name="encrypted_image.png")

            except Exception as e:
                st.error(f"Error: {e}")

# Decryption Page
if menu == "🔑 Decrypt Message":
    st.header("🔑 Decrypt a Message from an Image")

    uploaded_file = st.file_uploader("Upload an Encrypted Image", type=["png", "jpg", "jpeg"])
    password = st.text_input("Enter the Password", type="password")

    if uploaded_file and password:
        if st.button("🔓 Decrypt Message"):
            try:
                # Convert uploaded file into a bytes stream
                image_bytes = uploaded_file.read()
                image_array = np.frombuffer(image_bytes, np.uint8)
                img = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

                if img is None:
                    st.error("Invalid image file. Please upload a valid encrypted image.")
                else:
                    # Decode message
                    extracted_encrypted_msg = decode_message(img)
                    decrypted_msg = xor_encrypt_decrypt(extracted_encrypted_msg, password)

                    st.success(f"✅ Decrypted Message: {decrypted_msg}")

            except Exception as e:
                st.error(f"Error: {e}")
