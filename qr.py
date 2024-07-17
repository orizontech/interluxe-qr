import json
import qrcode
from urllib.parse import urlencode


def generate_qr_code(url, product, output_file):
    query_string = urlencode(product)
    full_url = f"{url}?{query_string}"

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(full_url)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save(output_file)
    print(f"QR code saved to {output_file}")


# URL of the generic product template
base_url = "https://orizontech.github.io/interluxe-qr/product.html"

# Load product data from JSON file
with open('products.json') as json_file:
    products = json.load(json_file)

# Generate QR codes for each product
for product in products:
    file_name = f"{product['title'].replace(' ', '_').lower()}_qr.png"
    generate_qr_code(base_url, product, file_name)
