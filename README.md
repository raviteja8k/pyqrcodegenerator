# QR Code Generator

A simple Flask application to generate QR codes from a given URL using the `qrcode` library.

## Requirements

- Python 3.x
- Flask
- `qrcode` library
- `Pillow` library (for image processing)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the required libraries:
   ```bash
   pip install Flask qrcode[pil]
   ```

## Usage

Run the Flask application:
```bash
flask run
```
Then, navigate to `http://127.0.0.1:5000` in your web browser and provide a URL to generate a QR code.
