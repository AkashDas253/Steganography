import cv2
import numpy as np
import argparse
from utils import xor_encrypt_decrypt
from encrypt import encode_message

def main():
    parser = argparse.ArgumentParser(description="Encrypt a message into an image.")
    parser.add_argument("password", type=str, help="Password for encryption")
    parser.add_argument("message", type=str, help="Message to encrypt")
    parser.add_argument("input_image_path", type=str, help="Path to the input image")
    parser.add_argument("output_image_path", type=str, help="Path to save the output image")

    args = parser.parse_args()

    # Load the image
    img = cv2.imread(args.input_image_path)
    if img is None:
        raise ValueError(f"Image not found! Ensure the file path '{args.input_image_path}' is correct.")

    # Encryption
    encrypted_msg = xor_encrypt_decrypt(args.message, args.password)
    encoded_img = encode_message(img.copy(), encrypted_msg)

    # Save as PNG (lossless compression)
    cv2.imwrite(args.output_image_path, encoded_img, [cv2.IMWRITE_PNG_COMPRESSION, 0])
    print(f"Message encrypted and stored in '{args.output_image_path}'.")

if __name__ == "__main__":
    main()