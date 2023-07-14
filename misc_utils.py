import base64
from PIL import Image
import io
import random


def getDownloadHref(base64_image_url):
    random_number = random.randint(1000, 9999)
    filename = f"image{random_number}.png"
    href = f'<a href="data:application/octet-stream;base64,{base64_image_url}" download="{filename}" style="text-decoration: none; padding: 8px 16px; background-color: transparent; color: #eee; border: 1px solid #333; border-radius: 4px;">Save image ⬇</a>'
    return href
