import streamlit as st
from pathlib import Path

image_path = f"{Path(__file__).parent.parent}/Icons"

st.title('My Skills')

with st.container(border=True):
    st.header('Programming Languages')
    py, java, cpp = st.columns([1, 1, 1], border=True)

    with py:
        st.write("Python (Proficient)")
        c1, c2 = st.columns([1, 6])
        with c1:
            st.empty()
        with c2:
            st.image(f"{image_path}/Python-Icon.png", width=200)

    with java:
        st.write("Java (Intermediate)")
        c1, c2 = st.columns([0.5, 10])
        with c1:
            st.empty()
        with c2:
            st.image(f'{image_path}/Java-Icon.png', width=200)

    with cpp:
        st.write("C++ (Basic)")
        c1, c2 = st.columns([1, 10])
        with c1:
            st.empty()
        with c2:
            st.image(f"{image_path}/CPP-Icon.png", width=200)


with st.container(border=True):
    st.header('Web Development')
    html, dj = st.columns([1, 1], border=True)

    with html:
        st.write("HTML")
        col_text, col_img = st.columns([1, 10])  # Create two columns inside container
        with col_text:
            st.empty()  # Empty placeholder to center image vertically
        with col_img:
            st.image(f"{image_path}/HTML-Icon.png", width=200)

    with dj:
        st.write("Django")
        col_text, col_img = st.columns([1, 10])  # Create two columns inside container
        with col_text:
            st.empty()  # Empty placeholder to center image vertically
        with col_img:
            st.image(f"{image_path}/Django-Icon.png", width=200)

with st.container(border=True):
    st.header('Libraries and Modules')
    np, pd, plt = st.columns([1, 1, 1], border=True)
    with np:
        st.write("Numpy")
        col_text, col_img = st.columns([1, 10])  # Create two columns inside container
        with col_text:
            st.empty()  # Empty placeholder to center image vertically
        with col_img:
            st.image(f"{image_path}/Numpy-Icon.png", width=200)
    with pd:
        st.write("Pandas")
        col_text, col_img = st.columns([1, 10])  # Create two columns inside container
        with col_text:
            st.empty()  # Empty placeholder to center image vertically
        with col_img:
            st.image(f"{image_path}/Pandas-Icon.png", width=200)
    with plt:
        st.write("Matplotlib")
        col_text, col_img = st.columns([1, 10])  # Create two columns inside container
        with col_text:
            st.empty()  # Empty placeholder to center image vertically
        with col_img:
            st.image(f"{image_path}/Matplotlib-Icon.png", width=200)

    tk, stream = st.columns([1, 1], border=True)
    with tk:
        st.write("Tkinter")
        col_text, col_img = st.columns([1, 10])  # Create two columns inside container
        with col_text:
            st.empty()  # Empty placeholder to center image vertically
        with col_img:
            st.image(f"{image_path}/Tkinter-Icon.png", width=200)

    with stream:
        st.write("Streamlit")
        col_text, col_img = st.columns([1, 10])  # Create two columns inside container
        with col_text:
            st.empty()  # Empty placeholder to center image vertically
        with col_img:
            st.image(f"{image_path}/Streamlit-Icon.png", width=200)


with st.container(border=True):
    st.header('Databases')
    sql, db = st.columns([1, 1], border=True)
    with sql:
        st.write("MySQL")
        col_text, col_img = st.columns([1, 10])  # Create two columns inside container
        with col_text:
            st.empty()  # Empty placeholder to center image vertically
        with col_img:
            st.image(f"{image_path}/MySQL-Icon.png", width=200)

    with db:
        st.write("MongoDB")
        col_text, col_img = st.columns([1, 10])  # Create two columns inside container
        with col_text:
            st.empty()  # Empty placeholder to center image vertically
        with col_img:
            st.image(f"{image_path}/MongoDB-Icon.png", width=200)


with st.container(border=True):
    st.header('Development Tools')
    pycharm, intellij, jupyter = st.columns([1, 1, 1], border=True)
    with pycharm:
        st.write("Pycharm")
        col_text, col_img = st.columns([1, 10])  # Create two columns inside container
        with col_text:
            st.empty()  # Empty placeholder to center image vertically
        with col_img:
            st.image(f"{image_path}/Pycharm-Icon.png", width=200)

    with intellij:
        st.write("Intellij Idea")
        col_text, col_img = st.columns([1, 10])  # Create two columns inside container
        with col_text:
            st.empty()  # Empty placeholder to center image vertically
        with col_img:
            st.image(f"{image_path}/Intellij-Icon.png", width=200)

    with jupyter:
        st.write("Jupyter Notebook")
        col_text, col_img = st.columns([1, 10])  # Create two columns inside container
        with col_text:
            st.empty()  # Empty placeholder to center image vertically
        with col_img:
            st.image(f"{image_path}/Jupyter-Icon.png", width=200)

    cmd, git, github = st.columns([1, 1, 1], border=True)
    with cmd:
        st.write("Command Prompt")
        col_text, col_img = st.columns([1, 10])  # Create two columns inside container
        with col_text:
            st.empty()  # Empty placeholder to center image vertically
        with col_img:
            st.image(f"{image_path}/Cmd-Icon.png", width=200)
    with git:
        st.write("Git")
        col_text, col_img = st.columns([1, 10])  # Create two columns inside container
        with col_text:
            st.empty()  # Empty placeholder to center image vertically
        with col_img:
            st.image(f"{image_path}/Git-Icon.png", width=200)
    with github:
        st.write("GitHub")
        col_text, col_img = st.columns([1, 10])  # Create two columns inside container
        with col_text:
            st.empty()  # Empty placeholder to center image vertically
        with col_img:
            st.image(f"{image_path}/GitHub-Icon.png", width=200)
