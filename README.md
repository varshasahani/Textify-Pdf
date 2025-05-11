# Textify-Pdf
# Textify

Textify is a Django-based application that allows users to upload receipts in PDF format, extract text from them using OCR (Optical Character Recognition), and validate the extracted data. The application also provides a dashboard to view valid and invalid receipts.

---

## Features

- Upload receipts in PDF format.
- Extract text from uploaded files using Tesseract OCR.
- Validate extracted data (e.g., merchant name, date, total amount).
- View valid and invalid receipts in a user-friendly interface.
- Store extracted data in a database for future reference.

---

## Prerequisites

Before setting up the project, ensure you have the following installed:

1. **Python** (version 3.8 or higher)
2. **pip** (Python package manager)
3. **Django** (version 4.0 or higher)
4. **Tesseract OCR** (for text extraction)
5. **Poppler** (for converting PDFs to images)

---

## Installation

Follow these steps to set up the project:

### 1. Clone the Repository

```bash
git clone https://github.com/varshasahani/Textify-Pdf.git
cd Textify

2. Set Up a Virtual Environment
Create and activate a virtual environment:

python3 -m venv virtualenv
source virtualenv/bin/activate  # On Windows: virtualenv\Scripts\activate
3. Install Dependencies
Install the required Python packages:

pip install -r requirements.txt
4. Install Tesseract OCR
Mac:
brew install tesseract
Ubuntu/Debian:
sudo apt install tesseract-ocr
Windows: Download and install Tesseract from Tesseract GitHub.
5. Install Poppler
Mac:
brew install poppler
Ubuntu/Debian:
sudo apt install poppler-utils
Windows: Download and install Poppler from Poppler for Windows, and add it to your systems PATH.
6. Configure the Database
Run the following commands to set up the database:

python manage.py makemigrations
python manage.py migrate
7. Run the Development Server
Start the Django development server:

python manage.py runserver
Visit http://127.0.0.1:8000/ in your browser to access the application.

Usage
Upload a Receipt
Navigate to the upload page.
Select a receipt file (PDF format) and click "Upload."
The application will extract text from the file and validate the data.

View Receipts
Navigate to the "All Receipts" page.
View valid receipts with extracted data.
View invalid receipts with reasons for invalidation.

Dependencies
The project uses the following Python packages:

Django: Web framework
pytesseract: Python wrapper for Tesseract OCR
pdf2image: Convert PDFs to images
Pillow: Image processing library
Install all dependencies using:

pip install -r requirements.txt
Troubleshooting
Common Issues
Tesseract Not Found:

Ensure Tesseract is installed and its path is correctly set in ocr_utils.py:
pytesseract.pytesseract.tesseract_cmd = r'/path/to/tesseract'
Poppler Not Found:

Ensure Poppler is installed and added to your systems PATH.
Database Errors:

Run migrations to sync the database schema:
python manage.py makemigrations
python manage.py migrate
