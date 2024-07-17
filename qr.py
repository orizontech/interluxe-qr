import qrcode
from PIL import Image


def generate_qr_code(data, output_file):
    """
    Generates a QR code from the given data and saves it to the specified output file.

    :param data: Dictionary containing product details.
    :param output_file: Path to the output file where the QR code will be saved.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save(output_file)


# Example product details
product = {
    "title": "Sunset Overdrive",
    "description": "A beautiful depiction of a sunset over the ocean.",
    "dimension": "24x36 inches",
    "year_of_creation": "2021",
    "price": "$1200",
    "image_url": "http://example.com/images/sunset_overdrive.jpg"
}

# Generate QR code for the product
data = f"""
Title: {product['title']}
Description: {product['description']}
Dimension: {product['dimension']}
Year of Creation: {product['year_of_creation']}
Price: {product['price']}
Image: {product['image_url']}
"""

output_file = "product_qr.png"
generate_qr_code(data, output_file)
print(f"QR code saved to {output_file}")
