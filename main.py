# Import necessary libraries
import qrcode  # Library to generate QR codes
from flask import Flask, request, send_file, render_template  # Import Flask and necessary functions

# Create a Flask application
app = Flask(__name__)

# Function to generate QR code from a given URL
def generate_qr_code(url):
    # Create a QR code object
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=10,  # Size of each box in the QR code
        border=4,  # Thickness of the border (minimum is 4)
    )
    
    # Add the URL to the QR code
    qr.add_data(url)
    qr.make(fit=True)  # Optimize the QR code size

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a file
    img.save("qrcode.png")  # Save as 'qrcode.png'
    return "qrcode.png"  # Return the filename for sending

@app.route('/', methods=['GET'])  # Route for the home page
def home():
    return render_template('index.html')  # Render the HTML file instead of using a string

@app.route('/generate', methods=['POST'])  # Create a route for QR code generation
def generate():
    url = request.form.get('url')  # Get URL from form data
    if not url:
        return "No URL provided. Exiting...", 400  # Return error if no URL is provided
    filename = generate_qr_code(url)  # Call the function to generate QR code
    return send_file(filename, mimetype='image/png')  # Send the generated QR code image

# Main function to execute the script
if __name__ == "__main__":
    app.run(debug=True)  # Run the Flask app in debug mode
