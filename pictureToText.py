from PIL import Image 
from pytesseract import pytesseract 
from PIL import ImageGrab
import hashlib
import pyperclip
import time
import cv2
import numpy as np

# Defining paths to tesseract.exe 
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


# Capture image from clipboard
def get_clipboard_image():
    try:
        image = ImageGrab.grabclipboard()  # This grabs whatever is in the clipboard
        if image:
            
            # Providing the tesseract executable 
            # location to pytesseract library 
            pytesseract.tesseract_cmd = path_to_tesseract        
            
            #text = "Give me the solution without extra details." + pytesseract.image_to_string(threshold,  lang="math_ocr", config="--psm 11 --oem 3"
            text = "Give me the solution without extra details." + pytesseract.image_to_string(image) 
            
            # Displaying the extracted text 
            print(text[:-1])
            pyperclip.copy(text)
            
            #sleeep
            time.sleep(0.5)                
        else:
            time.sleep(0.5)   
            #print("No image found in clipboard.")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
while(True):
    get_clipboard_image()
