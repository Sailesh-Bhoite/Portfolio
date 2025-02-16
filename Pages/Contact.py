import streamlit as st
from pathlib import Path

image_path = f"{Path(__file__).parent.parent}/Icons"

with st.container(border=True):
    st.title("Contact Me")
    st.write("Feel free to reach out to me!")

with st.container(border=True):

    with st.container(border=True):
        col_icon, col_label = st.columns([1, 20])

        with col_icon:
            st.image(f"{image_path}/Email-Icon.png", width=70)
        with col_label:
            st.markdown("[Email]('saileshlanguage@gmail.com')")

    with st.container(border=True):
        col_icon, col_label = st.columns([1, 20])

        with col_icon:
            st.image(f"{image_path}/GitHub-Icon.png", width=70)

        with col_label:
            st.markdown("[GitHub](https://github.com/Sailesh-Bhoite)")

    with st.container(border=True):
        col_icon, col_label = st.columns([1, 20])

        with col_icon:
            st.image(f"{image_path}/LinkedIn-Icon.png", width=70)

        with col_label:
            st.markdown("[LinkedIn](https://www.linkedin.com/in/sailesh-bhoite/)")

    with st.container(border=True):
        col_icon, col_label = st.columns([1, 20])

        with col_icon:
            st.image(f"{image_path}/Hackerrank-Icon.jpg", width=70)

        with col_label:
            st.markdown("[HakerRank](https://www.hackerrank.com/profile/saileshbht)")
