import streamlit as st
from pathlib import Path

image_path = f"{Path(__file__).parent.parent}\\Icons"

with st.container(border=True):
    col1, col2 = st.columns(2, vertical_alignment="center")
    with col1:
        st.title("Sailesh Bhoite")
        st.markdown("<h5>I'm on a journey to become a data scientist, fueled by a love for Python and a desire to build impactful applications. As I continue to discover and develop my skills, I am excited to take on new challenges and contribute to meaningful projects. Welcome to my portfolio, where I showcase my work, achievements, and ongoing exploration in the field of data science.</h5>", unsafe_allow_html=True)
    with col2:
        st.image(f"{image_path}/Profile.jpg")

with st.container(border=True):
    st.image(f"{image_path}/DS_Img.jpg")
