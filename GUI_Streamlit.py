import streamlit as st
import cv2
import numpy as np
from PIL import Image
from encrypt import encode_message
from decrypt import decode_message
from utils import xor_encrypt_decrypt
import io

# === Hide Default Streamlit Taskbar ===
hide_streamlit_style = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# === Initialize Session State for Page Navigation ===
if "page" not in st.session_state:
    st.session_state.page = "encrypt"  # Default page

# === Custom Navigation Bar ===
def set_page(page_name):
    st.session_state.page = page_name

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🔒 Encrypt Message"):
        set_page("encrypt")
with col2:
    if st.button("🔑 Decrypt Message"):
        set_page("decrypt")
with col3:
    st.markdown(
        '<a href="https://github.com/greedyknapsack/Educare_Internship" target="_blank"><button style="background-color:#003366;color:white;padding:8px 15px;border:none;border-radius:5px;cursor:pointer;">🌍 GitHub Repo</button></a>',
        unsafe_allow_html=True
    )

st.markdown("---")

# === Display Content Based on Selected Page ===
if st.session_state.page == "encrypt":
    st.header("🔒 Encrypt a Message into an Image")

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

elif st.session_state.page == "decrypt":
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
