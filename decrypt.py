import cv2
import numpy as np

def decode_message(img):
    """Decodes the hidden message from the image along the diagonal"""
    h, w, _ = img.shape

    # Retrieve message length from the first 4 diagonal pixels
    msg_len_bytes = bytes([img[i, i, 0] for i in range(4)])  # Read from blue channel
    msg_len = int.from_bytes(msg_len_bytes, byteorder='big')

    message = []
    msg_index = 0
    for i in range(4, min(h, w)):  # Start after the length bytes
        for channel in range(3):  # Iterate over RGB channels
            if msg_index < msg_len:
                message.append(chr(img[i, i, channel]))  # Read ASCII values
                msg_index += 1
            else:
                return ''.join(message)
    return ''.join(message)
