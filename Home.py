import streamlit as st
import random
import time
import json
import requests
import io
import base64
from PIL import Image
import os
from dotenv import load_dotenv
from utils import streamlit_cleanup, getDownloadHref, set_sidebar_contents

load_dotenv()

st.set_page_config(
    page_title="MEC Diffusion",
    page_icon="✨",
)


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
            st.error("Failed to generate images.")

    except requests.exceptions.RequestException as e:
        st.error("Failed to generate images. Error: " + str(e))

    except ValueError as e:
        st.error("Failed to parse response. Error: " + str(e))

    except:
        st.error("Failed to generate images.")

    return []


def main():
    set_sidebar_contents()
    streamlit_cleanup()

    st.title("MEC Diffusion - Text to Image Generation WebApp")
    st.write(
        "Web application that uses the technique of [Stable Diffusion](https://en.wikipedia.org/wiki/Stable_Diffusion) to generate images from descriptive text prompts. Hosted by [Govt. Model Engineering College](https://www.mec.ac.in/)."
    )
    st.write("For instructions and more details, visit [this link](/Details).")

    col1, col2 = st.columns([5, 1])
    with col1:
        prompt = st.text_input(
            "Prompt",
            placeholder="Eg: A rainbow coloured hot air balloon floating up in to the bright sunny sky",
        )
    with col2:
        batch_size = st.selectbox("Number of Images", [1, 2, 3, 4], index=1)

    if st.button("Generate Images"):
        if not prompt:
            prompt = "Government model engineering college"
        if prompt:
            with st.spinner(
                f"Generating {batch_size} {'image' if batch_size == 1 else 'images'}..."
            ):
                images = generate_images(prompt, batch_size)
                st.success("Images generated successfully!")

                for i in range(0, len(images), 2):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.image(images[i], use_column_width=True)
                        href = getDownloadHref(images[i])
                        st.markdown(href, unsafe_allow_html=True)

                    with col2:
                        if i + 1 < len(images):
                            st.image(images[i + 1], use_column_width=True)
                            href = getDownloadHref(images[i + 1])
                            st.markdown(href, unsafe_allow_html=True)
        else:
            st.warning("Please enter a prompt.")


if __name__ == "__main__":
    main()
