# Import necessary libraries
import qrcode  # Library to generate QR codes
import sys     # Library for system-specific parameters and functions

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

# Main function to execute the script
if __name__ == "__main__":
    # Ask the user to provide a URL
    url = input("Please enter a URL to generate a QR code: ")  # Prompt user for URL

    # Check if a URL is provided
    if not url:
        print("No URL provided. Exiting...")  # Print message if no URL is entered
        sys.exit(1)  # Exit the program with an error code

    generate_qr_code(url)  # Call the function to generate QR code
