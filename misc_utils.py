import base64
from PIL import Image
import io
import random


def getDownloadHref(image):
    image_bytes = io.BytesIO()
    image.save(image_bytes, format="PNG")
    image_bytes = image_bytes.getvalue()
    encoded_image = base64.b64encode(image_bytes).decode("utf-8")

    random_number = random.randint(1000, 9999)
    filename = f"image{random_number}.png"
    href = f'<a href="data:image/png;base64,{encoded_image}" download="{filename}" style="text-decoration: none; padding: 8px 16px; background-color: transparent; color: #eee; border: 1px solid #333; border-radius: 4px;">Save image ⬇</a>'
    return href
