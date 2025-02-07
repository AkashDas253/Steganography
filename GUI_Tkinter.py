import cv2
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os
from encrypt import encode_message
from decrypt import decode_message
from utils import xor_encrypt_decrypt

class SteganographyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Steganography")
        self.root.geometry("400x300")
        
        tk.Label(root, text="Image Steganography", font=("Arial", 16, "bold")).pack(pady=10)

        tk.Button(root, text="Encrypt Message", width=20, command=self.open_encrypt_window).pack(pady=10)
        tk.Button(root, text="Decrypt Message", width=20, command=self.open_decrypt_window).pack(pady=10)

    def open_encrypt_window(self):
        EncryptWindow()

    def open_decrypt_window(self):
        DecryptWindow()

class EncryptWindow:
    def __init__(self):
        self.win = tk.Toplevel()
        self.win.title("Encrypt Message")
        self.win.geometry("500x600")

        tk.Label(self.win, text="Select an Image", font=("Arial", 12, "bold")).pack(pady=5)
        self.img_label = tk.Label(self.win)
        self.img_label.pack()

        tk.Button(self.win, text="Choose Image", command=self.load_image).pack(pady=5)

        tk.Label(self.win, text="Enter Secret Message:").pack(pady=2)
        self.message_entry = tk.Entry(self.win, width=50)
        self.message_entry.pack(pady=5)

        tk.Label(self.win, text="Enter Password:").pack(pady=2)
        self.password_entry = tk.Entry(self.win, width=50, show="*")
        self.password_entry.pack(pady=5)

        tk.Button(self.win, text="Choose Save Location", command=self.choose_save_path).pack(pady=5)

        tk.Button(self.win, text="Encrypt & Save", command=self.encrypt_image).pack(pady=10)

        self.save_path = None

    def load_image(self):
        self.filepath = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if self.filepath:
            img = Image.open(self.filepath)
            img = img.resize((200, 200), Image.Resampling.LANCZOS)
            self.img = ImageTk.PhotoImage(img)
            self.img_label.config(image=self.img)

    def choose_save_path(self):
        self.save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])

    def encrypt_image(self):
        if not hasattr(self, 'filepath'):
            messagebox.showerror("Error", "Please select an image first!")
            return

        if not self.save_path:
            messagebox.showerror("Error", "Please select a save location!")
            return

        message = self.message_entry.get()
        password = self.password_entry.get()

        if not message or not password:
            messagebox.showerror("Error", "Message and password cannot be empty!")
            return

        encrypted_msg = xor_encrypt_decrypt(message, password)
        img = cv2.imread(self.filepath)

        if img is None:
            messagebox.showerror("Error", "Failed to load image!")
            return

        encoded_img = encode_message(img, encrypted_msg)
        cv2.imwrite(self.save_path, encoded_img, [cv2.IMWRITE_PNG_COMPRESSION, 0])

        messagebox.showinfo("Success", f"Message encrypted and saved to {self.save_path}")

class DecryptWindow:
    def __init__(self):
        self.win = tk.Toplevel()
        self.win.title("Decrypt Message")
        self.win.geometry("500x400")

        tk.Label(self.win, text="Select Encrypted Image", font=("Arial", 12, "bold")).pack(pady=5)
        self.img_label = tk.Label(self.win)
        self.img_label.pack()

        tk.Button(self.win, text="Choose Image", command=self.load_image).pack(pady=5)

        tk.Label(self.win, text="Enter Password:").pack(pady=2)
        self.password_entry = tk.Entry(self.win, width=50, show="*")
        self.password_entry.pack(pady=5)

        tk.Button(self.win, text="Decrypt Message", command=self.decrypt_image).pack(pady=10)

        self.result_label = tk.Label(self.win, text="", font=("Arial", 12, "bold"))
        self.result_label.pack(pady=10)

    def load_image(self):
        self.filepath = filedialog.askopenfilename(filetypes=[("Image Files", "*.png")])
        if self.filepath:
            img = Image.open(self.filepath)
            img = img.resize((200, 200), Image.Resampling.LANCZOS)
            self.img = ImageTk.PhotoImage(img)
            self.img_label.config(image=self.img)

    def decrypt_image(self):
        if not hasattr(self, 'filepath'):
            messagebox.showerror("Error", "Please select an image first!")
            return

        password = self.password_entry.get()
        if not password:
            messagebox.showerror("Error", "Please enter the password!")
            return

        img = cv2.imread(self.filepath)
        if img is None:
            messagebox.showerror("Error", "Failed to load image!")
            return

        extracted_encrypted_msg = decode_message(img)
        decrypted_msg = xor_encrypt_decrypt(extracted_encrypted_msg, password)

        self.result_label.config(text=f"Decrypted Message: {decrypted_msg}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SteganographyApp(root)
    root.mainloop()
