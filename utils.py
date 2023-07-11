import streamlit as st
import random


def center_align_full_screen_image():
    st.markdown(
        """
    <style>
        button[title^=Exit]+div [data-testid=stImage]{
            text-align: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 100%;
        }
    </style>
    """,
        unsafe_allow_html=True,
    )


def remove_streamlit_footer():
    st.markdown(
        '<style>#MainMenu {visibility: hidden;} footer {visibility: hidden;} footer:after{visibility: hidden; content: "Aldrin Jenson - CSB MEC 2019"}</style>',
        unsafe_allow_html=True,
    )


def replace_streamlit_footer():
    remove_streamlit_footer()
    st.markdown(
        """
        <div style="position: fixed; bottom: 0; left: 50%; transform: translateX(-50%); padding: 10px; border-radius: 5px; text-align: center; width: 90%;">
            <span style="font-size: 15px; color:#fafafa66;">Made by 
                <a href="https://linkedin.com/in/aldrinjenson">Aldrin Jenson</a>, CSB - MEC'19
            </span>
        </div>
        """,
        unsafe_allow_html=True,
    )


def streamlit_cleanup():
    center_align_full_screen_image()
    replace_streamlit_footer()


def set_sidebar_contents():
    st.sidebar.title("MEC Diffusion✨")
    st.sidebar.markdown(
        """
    Generate images from thin air, using just your text prompts!
    
    Bring your imaginations to life✨

    ## Credits:
    - [Stability-AI/StableDiffusion](https://github.com/Stability-AI/StableDiffusion) 
    - [Stable Diffusion WebUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui/) by AUTOMATIC1111
    - [Titty Jacob Sir](https://www.linkedin.com/in/titty-jacob-8795374/) for all the support
    """
    )
    pass
