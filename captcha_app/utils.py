import random
import string
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont

def generate_captcha():
    # Random text for CAPTCHA
    captcha_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    
    # Create an image with a white background
    image = Image.new('RGB', (150, 50), color=(255, 255, 255))
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()

    # Draw the text on the image
    draw.text((40, 20), captcha_text, font=font, fill=(0, 0, 0))
    
    # Save the image to a BytesIO object
    image_io = BytesIO()
    image.save(image_io, 'PNG')
    image_io.seek(0)
    return captcha_text, image_io
