import cv2
import numpy as np
import argparse
from utils import xor_encrypt_decrypt
from decrypt import decode_message

def main():
    parser = argparse.ArgumentParser(description="Decrypt a message from an image.")
    parser.add_argument("password", type=str, help="Password for decryption")
    parser.add_argument("input_image_path", type=str, help="Path to the input image")

    args = parser.parse_args()

    # Load the image
    img = cv2.imread(args.input_image_path)
    if img is None:
        raise ValueError(f"Image not found! Ensure the file path '{args.input_image_path}' is correct.")

    # Decryption
    extracted_encrypted_msg = decode_message(img)
    decrypted_msg = xor_encrypt_decrypt(extracted_encrypted_msg, args.password)

    print("Decrypted message:", decrypted_msg)

if __name__ == "__main__":
    main()