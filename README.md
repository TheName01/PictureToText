# Clipboard OCR Automation

This script captures an image from the clipboard, performs Optical Character Recognition (OCR) using Tesseract, and copies the extracted text back to the clipboard.

## Features

- Captures images directly from the clipboard.
- Extracts text using [Tesseract OCR](https://github.com/tesseract-ocr/tesseract).
- Appends a custom prompt to the extracted text. (If not needed delete: "Give me the solution without extra details." +)
- Copies the final string to the clipboard.
- Runs continuously to monitor the clipboard.

## Requirements

- Python 3.x
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) installed and properly configured.
- The following Python packages:
  - `Pillow`
  - `pytesseract`
  - `opencv-python`
  - `numpy`
  - `pyperclip`

Install the Python packages using:

```bash
pip install pillow pytesseract opencv-python numpy pyperclip
