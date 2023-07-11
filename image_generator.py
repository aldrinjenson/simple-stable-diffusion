import streamlit as st
from dotenv import load_dotenv
import os
import requests
import json
import io
import base64
from PIL import Image

load_dotenv()


def generate_images(prompt, batch_size):
    url = os.getenv("API_URL")
    negative_prompt = os.getenv("NEGATIVE_PROMPT")

    payload = {
        "prompt": prompt,
        "steps": 20,
        "negative_prompt": negative_prompt,
        "batch_size": batch_size,
    }

    try:
        response = requests.post(url=url, json=payload)

        if response.status_code == 200:
            data = response.json()
            images = data.get("images", [])
            decoded_images = []

            for image in images:
                img_data = base64.b64decode(image)
                img = Image.open(io.BytesIO(img_data))
                decoded_images.append(img)

            return decoded_images
        else:
            st.error(
                "Failed to generate images. Server is not reachable at the moment."
            )

    except requests.exceptions.RequestException as e:
        st.error(
            "Failed to generate images. The server may be down or not reachable at the moment"
        )

    except:
        st.error("Failed to generate images.")

    return None
