import streamlit as st

pages = [
    st.Page("Pages/Home.py", title="Home - About Me", icon=":material/home:"),
    st.Page("Pages/Education.py", title="My Education", icon=":material/school:"),
    st.Page("Pages/Skills.py", title="My Skills", icon=":material/workspace_premium:"),
    st.Page("Pages/Work.py", title="My Work", icon=":material/business_center:"),
    st.Page("Pages/Contact.py", title="Contact Details", icon=":material/phone:"),
]

nav = st.navigation(pages, position="sidebar")
nav.run()
