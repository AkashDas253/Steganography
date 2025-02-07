import cv2
import numpy as np

from utils import xor_encrypt_decrypt
from decrypt import decode_message

# Hardcoded inputs
password = "MySecretKey"

input_image_path = "test_image/pic_to_get_data.jpg"

# Load the image
img = cv2.imread(input_image_path)
if img is None:
    raise ValueError(f"Image not found! Ensure the file path '{input_image_path}' is correct.")

# Decryption
extracted_encrypted_msg = decode_message(img)
decrypted_msg = xor_encrypt_decrypt(extracted_encrypted_msg, password)

print("Decrypted message:", decrypted_msg)
