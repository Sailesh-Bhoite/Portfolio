import streamlit as st
from pathlib import Path

image_path = f"{Path(__file__).parent.parent}\\Icons"

st.title('My Education')
book_stack, content = st.columns([1, 1], vertical_alignment="center")

with book_stack:
    st.image(f"{image_path}\\BookStack.png")

with content:
    with st.container(border=True):
        st.metric(label="2019-2020", value="10th - 88%")
        st.markdown('<h3>Sarhad School and Junior College</h3>', unsafe_allow_html=True)

    with st.container(border=True):
        st.metric(label="2021-2022", value="12th - 86.5%")
        st.markdown('<h3>Sarhad School and Junior College</h3>', unsafe_allow_html=True)

    with st.container(border=True):
        st.metric(label="2022-2023", value="F.E. - 8.98 Pointer")
        st.metric(label="2023-2024", value="S.E. - 9.18 Pointer")
        st.metric(label="2024-2025", value="T.E. - Appearing")
        st.markdown('<h3>JSPM Narhe Technical Campus</h3>', unsafe_allow_html=True)
