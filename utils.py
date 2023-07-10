import streamlit as st

def replace_streamlit_footer():
    st.markdown(
    '<style>#MainMenu {visibility: hidden;} footer {visibility: hidden;} footer:after{visibility: hidden; content: "Aldrin Jenson - CSB MEC 2019"}</style>', unsafe_allow_html=True)
    
    st.markdown(
        """
        <div style="position: fixed; bottom: 0; left: 50%; transform: translateX(-50%); padding: 10px; border-radius: 5px; text-align: center; width: 90%;">
            <span style="font-size: 15px; color:#fafafa66;">Made by 
                <a href="https://linkedin.com/in/aldrinjenson">Aldrin Jenson</a>
                , CSB - MEC'19
            </span>
        </div>
        """,
        unsafe_allow_html=True
    )

    