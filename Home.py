import streamlit as st
from src.st_utils import streamlit_cleanup, set_sidebar_contents
from src.misc_utils import getDownloadHref, getRandomQuote
from src.image_generator import generate_images


st.set_page_config(
    page_title="MEC Diffusion",
    page_icon="✨",
)


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

    randomQuote = getRandomQuote()
    if st.button("Generate Images", type="primary"):
        if not prompt:
            prompt = "Little red riding hood, ultrarealistic"
        if not prompt:
            st.warning("Please enter a prompt.")
            return

        with st.spinner(
            f"Generating {batch_size} {'image' if batch_size == 1 else 'images'}...\n\n {randomQuote}"
        ):
            notif = st.empty()
            images = generate_images(prompt, batch_size)
            if images:
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
                notif.success("Images generated successfully!")
            else:
                st.warning("Please try again after some time")


if __name__ == "__main__":
    main()
