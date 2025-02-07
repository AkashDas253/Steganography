import cv2
import numpy as np

from utils import xor_encrypt_decrypt
from encrypt import encode_message
from decrypt import decode_message

# Hardcoded inputs
password = "MySecretKey"
msg = "This is a hidden message from test!"
input_image_path = "test_image/pic_to_hide_data.png"
output_image_path = "test_image/pic_to_get_data.png"

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

# Decryption
extracted_encrypted_msg = decode_message(encoded_img)
decrypted_msg = xor_encrypt_decrypt(extracted_encrypted_msg, password)

print("Decrypted message:", decrypted_msg)
