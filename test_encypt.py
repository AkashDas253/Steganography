import cv2
import numpy as np
from utils import xor_encrypt_decrypt
from encrypt import encode_message

# Hardcoded inputs
password = "MySecretKey"
msg = "This is a message!"
input_image_path = "test_image/pic_to_hide_data.jpg"
output_image_path = "test_image/pic_to_get_data.jpg"  

# Load the image
img = cv2.imread(input_image_path)
if img is None:
    raise ValueError(f"Image not found! Ensure the file path '{input_image_path}' is correct.")

# Encryption
encrypted_msg = xor_encrypt_decrypt(msg, password)
encoded_img = encode_message(img.copy(), encrypted_msg)

# Save as PNG (lossless compression)
cv2.imwrite(output_image_path, encoded_img, [cv2.IMWRITE_PNG_COMPRESSION, 0])
print(f"Message encrypted and stored in '{output_image_path}'.")