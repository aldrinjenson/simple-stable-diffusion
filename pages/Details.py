import streamlit as st
from utils import remove_streamlit_footer, set_sidebar_contents

st.set_page_config(
    page_title="MEC Diffusion | About",
    page_icon="✨",
)

remove_streamlit_footer()
set_sidebar_contents()

st.markdown(
    """
    # About MEC Diffusion
    ## What is MEC Diffusion?
    MEC Diffusion is a cutting-edge text-to-image generation web application that utilizes the Stable Diffusion technique to generate images from text prompts.


    ## Project Objective
    The aim of MEC Diffusion is to make the incredible technology of Stable Diffusion accessible to a wider audience. Running Stable Diffusion locally typically requires a modern computer with substantial GPU capabilities. By hosting this web app on an NVIDIA Quadro GPU at Govt. Model Engineering College, Kochi, we provide users with an opportunity to explore Stable Diffusion for free. The user interface is intentionally designed to be simple and user-friendly by pre-configuring most hyperparameters for easy startup.

    ## How does Stable Diffusion work? 
    Stable Diffusion is a technique used in machine learning to generate high-quality images from textual prompts. To learn more about Stable Diffusion, you can refer to the [wikipedia article](https://en.wikipedia.org/wiki/Stable_Diffusion).

    ## Technical Specifications
    - MEC Diffusion is hosted on an NVIDIA Quadro GPU at Govt. Model Engineering College, Kochi.
    - The image generation process is powered by an open-source model called OpenJourney, which is trained on images generated by the MidJourney bot.

    ## Tips for Generating Better Images:
    - Use descriptive prompts to guide the image generation process. For example, provide specific details like "A ship sailing through stormy seas with thunder and lightning, rendered in a realistic style."
    - Include maximum details and descriptions in your prompts for more accurate and high-quality image generation.
    - Generating multiple images simultaneously may increase processing time.
    - Please note that response times may vary during peak usage periods.
    - For more information about Stable Diffusion-based image generation, you can visit [stable-diffusion-art.com](https://stable-diffusion-art.com/).

    ## Additional Information:
    - Please be aware that due to increased server load or network issues, image generation may occasionally take longer than usual.
    - For users seeking more control over the generation process, including the ability to adjust parameters like seed value, CFG scale value, sampling steps, and sampling method, we recommend trying the [Stable Diffusion WebUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui/) version.
    - We would like to emphasize that this is a powerful tool, and we urge users to utilize it responsibly.

    ## Project Availability:
    - MEC Diffusion will remain available as long as the GPU resources of the college are not required for other purposes. In cases where the resources need to be reallocated, users may experience temporary downtime.

    ## Project Authorship:
    - MEC Diffusion was developed by Aldrin Jenson, a student from the 2019 batch of Model Engineering College.
    - While the primary Stable Diffusion WebUI was previously hosted on the college GPU for several months, we have created this version from scratch to provide a more streamlined experience for newcomers.
    - The web application is implemented in Python using the Streamlit framework and utilizes server-side rendering.

    ## Credits:
    - [Stability-AI/StableDiffusion](https://github.com/Stability-AI/StableDiffusion)
    - [Stable Diffusion WebUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui/) by AUTOMATIC1111
    - Special thanks to [Titty Jacob Sir](https://www.linkedin.com/in/titty-jacob-8795374/) for the invaluable support provided throughout the development process.

    We kindly request everyone to use this tool responsibly.
    """
)


st.markdown(
    "<div style='text-align:center; padding-top:5%;'>Made with ❤️ by <a href='https://www.linkedin.com/in/aldrinjenson/'>Aldrin Jenson</a></div>",
    unsafe_allow_html=True,
)
