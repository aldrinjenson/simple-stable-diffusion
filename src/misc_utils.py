import base64
from PIL import Image
import io
import random
import json


def getDownloadHref(base64_image_url):
    random_number = random.randint(1000, 9999)
    filename = f"image{random_number}.png"
    href = f'<a href="data:application/octet-stream;base64,{base64_image_url}" download="{filename}" style="text-decoration: none; padding: 8px 16px; background-color: transparent; color: #eee; border: 1px solid #333; border-radius: 4px;">Save image ⬇</a>'
    return href


quotes = []
file_path = "src/quotes-1000.json"
with open(file_path, "r") as file:
    print("opening quotes")
    quotes = json.load(file)


def getRandomQuote():
    random_quote = random.choice(quotes)

    quote_text = random_quote["quoteText"].rstrip(".")
    quote_author = random_quote["quoteAuthor"] or "Unknown"

    markdown_quote = f"> {quote_text}\n >-- {quote_author}"

    return markdown_quote
