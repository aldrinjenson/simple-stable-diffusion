import streamlit as st


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


def replace_streamlit_footer():
    st.markdown(
        '<style>#MainMenu {visibility: hidden;} footer {visibility: hidden;} footer:after{visibility: hidden; content: "Aldrin Jenson - CSB MEC 2019"}</style>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div style="position: fixed; bottom: 0; left: 50%; transform: translateX(-50%); padding: 10px; border-radius: 5px; text-align: center; width: 90%;">
            <span style="font-size: 15px; color:#fafafa66;">Made by 
                <a href="https://linkedin.com/in/aldrinjenson">Aldrin Jenson</a>
                , CSB - MEC'19
            </span>
        </div>
        """,
        unsafe_allow_html=True,
    )


def streamlit_cleanup():
    center_align_full_screen_image()
    replace_streamlit_footer()


def getDownloadHref(image):
    image_bytes = io.BytesIO()
    image.save(image_bytes, format="PNG")
    image_bytes = image_bytes.getvalue()
    encoded_image = base64.b64encode(image_bytes).decode("utf-8")

    random_number = random.randint(1000, 9999)
    filename = f"image{random_number}.png"
    href = f'<a href="data:image/png;base64,{encoded_image}" download="{filename}" style="text-decoration: none; padding: 8px 16px; background-color: transparent; color: #eee; border: 1px solid #333; border-radius: 4px;">Save image ⬇</a>'
    return href
