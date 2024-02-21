from PIL import Image
import pytesseract
import os

# Set the path to the Tesseract executable (change this based on your installation)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def image_to_text_and_save(image_path, output_txt_path):
    # Open the image file
    image = Image.open(image_path)

    # Perform OCR to extract text
    extracted_text = pytesseract.image_to_string(image)

    # Save the extracted text to a .txt file
    with open(output_txt_path, 'w', encoding='utf-8') as txt_file:
        txt_file.write(extracted_text)

# Example usage
image_path = r'C:\Users\mehed\SixProject\Files\test.jpg'
output_txt_path = r'output.txt'

image_to_text_and_save(image_path, output_txt_path)
