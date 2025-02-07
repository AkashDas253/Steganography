# **🔐 Image Steganography App**  

A **steganography** project using **Streamlit** and **Tkinter** for GUI, enabling users to **hide and extract secret messages** in images with password encryption.


🚀 **Live Demo**: [Click Here to Open the App](https://steganography-2kbidmxbgmrqmmpnu3i9sb.streamlit.app/)  

---

## **📌 Features**  
✔ **GUI Options**: Choose between **Streamlit** (`GUI_Streamlit.py`) and **Tkinter** (`GUI_Tkinter.py`).  
✔ **Encrypt Messages**: Hide a secret message inside an image securely.  
✔ **Decrypt Messages**: Retrieve hidden messages from encrypted images.  
✔ **Password Protection**: Ensures **only authorized** users can retrieve messages.  
✔ **Test Scripts**: Includes test files for encryption and decryption.  
✔ **Download Encrypted Images**: Save your steganographic image after encoding.  

---

## **📂 Project Structure**  
```
📁 graphy
│── 📄 .gitignore              # Git ignored files
│── 📁 .venv                   # Virtual environment (optional)
│── 📁 dump                    # Temporary storage (optional)
│── 📁 test_image              # Sample images for testing
│── 📁 __pycache__             # Compiled Python files
│── 📄 encrypt.py              # Encryption logic
│── 📄 decrypt.py              # Decryption logic
│── 📄 utils.py                # XOR encryption utility
│── 📄 GUI_Streamlit.py        # Streamlit-based GUI
│── 📄 GUI_Tkinter.py          # Tkinter-based GUI
│── 📄 test.py                 # Test script
│── 📄 test_encrypt.py         # Encryption unit test
│── 📄 test_decrypt.py         # Decryption unit test
│── 📄 requirements.txt        # Dependencies
│── 📄 README.md               # Project documentation
```

---

## **📥 Installation**  
1. **Clone the Repository**  
   ```
   git clone https://github.com/AkashDas253/Steganography
   cd Steganography
   ```

2. **Create a Virtual Environment (Optional but Recommended)**  
   ```
   python -m venv .venv
   source .venv/bin/activate    # On macOS/Linux
   .venv\Scripts\activate       # On Windows
   ```

3. **Install Dependencies**  
   ```
   pip install -r requirements.txt
   ```

---

## **🚀 Usage**  

### **Streamlit GUI**  
Run the **Streamlit app**:  
```
streamlit run GUI_Streamlit.py
```
- Open browser → **Use the interface to encrypt & decrypt messages.**

### **Tkinter GUI**  
Run the **Tkinter app**:  
```
python GUI_Tkinter.py
```
- A window will open → **Use buttons to encrypt & decrypt messages.**

### **Test Encryption & Decryption**  
Run test scripts:  
```
python test_encrypt.py
python test_decrypt.py
```

---

## **⚙ Dependencies**  
Make sure you have the following installed:
```
streamlit
opencv-python-headless
numpy
pillow
```

---

## **🔧 Deployment (Streamlit Cloud)**  
1. Push the repository to **GitHub**.  
2. Go to **[Streamlit Cloud](https://streamlit.io/cloud)**.  
3. Click **"New App"** → Connect your GitHub repository.  
4. Select `GUI_Streamlit.py` as the main script.  
5. **Deploy!** 🚀  

---

## **📜 License**  
This project is **open-source** under the **MIT License**.

---

## **💡 Credits**  
Developed by **Akash Das**  
GitHub: [Your GitHub Profile](https://github.com/AkashDas253/Steganography)  

---
