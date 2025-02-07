import cv2
import numpy as np

def encode_message(img, encrypted_msg):
    """Encodes the encrypted message into the image safely"""
    h, w, _ = img.shape
    msg_len = len(encrypted_msg)

    if msg_len > h * w * 3 - 4:  # Reserve first 4 bytes for length
        raise ValueError("Message too long for the given image.")

    # Store message length in the first 4 pixels
    msg_len_bytes = msg_len.to_bytes(4, byteorder='big')
    idx = 0
    for i in range(4):
        img[i, 0, 0] = msg_len_bytes[i]  # No +32, store exact bytes

    # Store message in pixel values
    msg_index = 0
    for row in range(h):
        for col in range(w):
            for channel in range(3):  # RGB channels
                if row == 0 and col < 4:  # Skip first 4 pixels
                    continue
                if msg_index < msg_len:
                    img[row, col, channel] = ord(encrypted_msg[msg_index])  # Store ASCII values
                    msg_index += 1
                else:
                    return img
    return img
