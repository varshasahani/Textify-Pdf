import pytesseract
from PIL import Image, ImageOps
from pdf2image import convert_from_path
import re

pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'

def extract_text_from_pdf(pdf_path):
    # Convert PDF to images
    images = convert_from_path(pdf_path)
    extracted_text = ""
    for i, image in enumerate(images):
        # Preprocess the image
        image = ImageOps.grayscale(image)
        image = ImageOps.autocontrast(image)
        text = pytesseract.image_to_string(image, lang='eng')
        extracted_text += text
    return extracted_text

def parse_receipt_data(text):
    # Example: Extract merchant name, date, and total amount using regex
    merchant_name = re.search(r"Merchant:\s*(.+)", text)
    purchased_at = re.search(r"Date:\s*(\d{4}-\d{2}-\d{2})", text)
    total_amount = re.search(r"Total:\s*\$?(\d+\.\d{2})", text)

    return {
        "merchant_name": merchant_name.group(1) if merchant_name else None,
        "purchased_at": purchased_at.group(1) if purchased_at else None,
        "total_amount": total_amount.group(1) if total_amount else None,
    }