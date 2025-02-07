import cv2
import numpy as np

def encode_message(img, encrypted_msg):
    """Encodes the encrypted message into the image along the diagonal"""
    h, w, _ = img.shape
    msg_len = len(encrypted_msg)

    if msg_len > min(h, w) * 3 - 4:  # Reserve first 4 diagonal positions for length
        raise ValueError("Message too long for the given image.")

    # Convert message length to 4-byte format and store it in diagonal pixels
    msg_len_bytes = msg_len.to_bytes(4, byteorder='big')
    for i in range(4):
        img[i, i, 0] = msg_len_bytes[i]  # Store length in blue channel of diagonal pixels

    # Store message along the diagonal
    msg_index = 0
    for i in range(4, min(h, w)):  # Start after the length bytes
        for channel in range(3):  # Iterate over RGB channels
            if msg_index < msg_len:
                img[i, i, channel] = ord(encrypted_msg[msg_index])  # Store ASCII values
                msg_index += 1
            else:
                return img
    return img
