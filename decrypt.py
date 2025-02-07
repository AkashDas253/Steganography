import cv2
import numpy as np

def decode_message(img):
    """Decodes the hidden message from the image."""
    h, w, _ = img.shape

    # Retrieve message length
    msg_len_bytes = bytes([img[i, 0, 0] for i in range(4)])  # Retrieve the first 4 bytes
    msg_len = int.from_bytes(msg_len_bytes, byteorder='big')

    message = []
    msg_index = 0
    for row in range(h):
        for col in range(w):
            for channel in range(3):  # RGB channels
                if row == 0 and col < 4:  # Skip length bytes
                    continue
                if msg_index < msg_len:
                    message.append(chr(img[row, col, channel]))
                    msg_index += 1
                else:
                    return ''.join(message)
    return ''.join(message)
