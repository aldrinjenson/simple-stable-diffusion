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
import streamlit.components.v1 as components

load_dotenv()

st.set_page_config(
    page_title="Stable Diffusion - MEC",
    page_icon="✨",
)


def add_sidebar_content():
    st.sidebar.markdown(
    """
    ### Tips for Better Images:
    - Use descriptive prompts. Example: "Ship sailing through stormy seas with thunder and lightning. Realistic."
    - Provide maximum details and descriptions in the prompt for better image generation.
    - Generating more images at once may increase the processing time.
    - Response times may vary during peak usage periods.
    - Right-click an image and select "Save AS" to download it locally
    - Please use this tool responsibly.
    
    For more information about stable diffusion-based image generation, visit [stable-diffusion-art.com](https://stable-diffusion-art.com/).
    
    #### Credits:
    - [Stable Diffusion WebUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui/) by AUTOMATIC1111
    - [Titty Jacob](https://www.linkedin.com/in/titty-jacob-8795374/) for all the support
    
    Made with ❤️ for MEC by [Aldrin Jenson](https://www.linkedin.com/in/aldrinjenson/)
    """
    )

    st.markdown()

    # st.markdown(
    #     '<style>#MainMenu {visibility: hidden;} footer {visibility: hidden;} footer:after{visibility: visible; content: "Aldrin Jenson - CSB MEC 2019"}</style>', unsafe_allow_html=True)
    # custom_js = """
    # <script>
    # document.addEventListener("DOMContentLoaded", function() {
    #     // Select the footer element
    #     var footer = document.querySelector("footer");
    #     console.log(footer)

    #     // Create a new anchor element
    #     var anchor = document.createElement("a");
    #     anchor.href = "https://www.example.com";

    #     // Create a new span element
    #     var span = document.createElement("span");
    #     span.className = "content";
    #     span.textContent = "Aldrin Jenson - CSB MEC'19 batch";

    #     // Append the span element to the anchor element
    #     anchor.appendChild(span);

    #     // Remove existing content from the footer
    #     footer.innerHTML = "";

    #     // Append the anchor element to the footer
    #     footer.appendChild(anchor);
    # });
    # </script>
    # """
    # components.html(custom_js)
    # # Render the custom JavaScript using st.markdown()
    # st.markdown(custom_js, unsafe_allow_html=True)




def generate_images(prompt, batch_size):
    url = os.getenv("API_URL")
    negative_prompt = os.getenv("NEGATIVE_PROMPT")

    payload = {
        "prompt": prompt,
        "steps": 20,
        "negative_prompt": negative_prompt,
        "batch_size": batch_size,
    }

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

    return []


def getDownloadHref (image):
    image_bytes = io.BytesIO()
    image.save(image_bytes, format='PNG')
    image_bytes = image_bytes.getvalue()
    encoded_image = base64.b64encode(image_bytes).decode("utf-8")

    random_number = random.randint(1000, 9999)
    filename = f"image{random_number}.png"
    href = f'<a href="data:image/png;base64,{encoded_image}" download="{filename}" style="text-decoration: none; padding: 8px 16px; background-color: transparent; color: #eee; border: 1px solid #333; border-radius: 4px;">Save image ⬇</a>'
    return href


def main():
    st.sidebar.title("Instructions and Details")
    add_sidebar_content()

    st.title("SD - Text to Image Generation")
    st.write("Web application that uses the technique of [Stable Diffusion](https://en.wikipedia.org/wiki/Stable_Diffusion) to generate images from descriptive text prompts. Hosted by [Govt. Model Engineering College](https://www.mec.ac.in/).")

    col1, col2 = st.columns([5, 1])
    with col1:
        prompt = st.text_input("Prompt",placeholder="Eg: A rainbow coloured hot air balloon floating up in to the bright sunny sky")
    with col2:
        batch_size = st.selectbox("Number of Images", [1, 2, 3, 4], index=1)

    if st.button("Generate Images"):
        if not prompt:
            prompt = "Little red riding hood. Ultra-realistic"
        if prompt:
            with st.spinner(f"Generating {batch_size} {'image' if batch_size == 1 else 'images'}..."):
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
                            href = getDownloadHref(images[i+1])
                            st.markdown(href, unsafe_allow_html=True)
        else:
            st.warning("Please enter a prompt.")

    

if __name__ == "__main__":
    main()
