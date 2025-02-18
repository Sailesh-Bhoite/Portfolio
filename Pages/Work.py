import streamlit as st
from pathlib import Path

image_path = f"{Path(__file__).parent.parent}/Icons"

st.title('My Works')

works = [
    {
        'title': "Crammer's Rule",
        'desc': "Python implementation of Crammer's rule.",
        'repo_link': "https://github.com/Sailesh-Bhoite/The-Crammers-Rule",
        'video_link': "https://www.linkedin.com/posts/sailesh-bhoite_i-was-just-wondering-how-could-be-solving-activity-7296687229521793025-_ewe?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEgWZHsBTswwPEbC-Z3cAWUiezWgCnj6xf4",
        'demo_link': None,
        'demo_image': "Crammers_Rul_demo.png",
    },
    {
        'title': "Number Guessing Game",
        'desc': "A number guessing game, which generates a random number and asks you to guess it. <br> It is made by using 'Tkinter' library in python.",
        'repo_link': "https://github.com/Sailesh-Bhoite/The-Number-Guessing-Game",
        'video_link': "https://www.linkedin.com/posts/sailesh-bhoite_hello-connections-i-recently-made-a-number-activity-7226112230319153152-2K-q?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEgWZHsBTswwPEbC-Z3cAWUiezWgCnj6xf4",
        'demo_link': None,
        'demo_image': "Number_Gue_demo.png",
    },
    {
        'title': "Scientific Calculator",
        'desc': "A Scientific Calculator which is made with 'Tkinter' module in python. <br> Calculations are done with the help of 'math' module.",
        'repo_link': "https://github.com/Sailesh-Bhoite/The-Scientific-Calculator",
        'video_link': "https://www.linkedin.com/posts/sailesh-bhoite_hello-connections-heres-another-mini-activity-7228543221620965376-F_z5?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEgWZHsBTswwPEbC-Z3cAWUiezWgCnj6xf4",
        'demo_link': None,
        'demo_image': "Scientific_Cal_demo.png",
    },
    {
        'title': "Graph Plotter",
        'desc': "A graph plotter, which plots graph depending on your selected graph type and data points. <br> Made with 'Tkinter' and 'Matplotlib' Module.",
        'repo_link': "https://github.com/Sailesh-Bhoite/Graph-Plotter",
        'video_link': "https://www.linkedin.com/posts/sailesh-bhoite_techmindsmarathon-techminds-activity-7267065711779328000-Dac8?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEgWZHsBTswwPEbC-Z3cAWUiezWgCnj6xf4",
        'demo_link': None,
        'demo_image': "Graph_Plo_demo.png",
    },
    {
        'title': "Student Data Dashboard",
        'desc': "A 'Tkinter' app that takes data from a database and represent them in various visualizations.",
        'repo_link': "https://github.com/Sailesh-Bhoite/Student-Data-Dashboard",
        'video_link': "https://www.linkedin.com/posts/sailesh-bhoite_techmindsmarathon-techminds-activity-7286268584534626304-uFkJ?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEgWZHsBTswwPEbC-Z3cAWUiezWgCnj6xf4",
        'demo_link': None,
        'demo_image': "Student_DB_demo.png",
    },
    {
        'title': "Folder Organizer",
        'desc': "Just pass your not-so-organized folder's path to it and it will organize your folder by classifying your files into different categories like Documents, PDFs, Text Files, Images, Spreadsheets, Presentations, Videos and Others.",
        'repo_link': "https://github.com/Sailesh-Bhoite/Folder-Organizer",
        'video_link': "https://www.linkedin.com/posts/sailesh-bhoite_techminds-techmindmarathon-activity-7264321473874444288-Getl?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEgWZHsBTswwPEbC-Z3cAWUiezWgCnj6xf4",
        'demo_link': None,
        'demo_image': "Folder_Org_demo.png",
    },
    {
        'title': "Currency Convertor",
        'desc': "This is a Django website that can be used to convert currencies of different countries. <br><b>My first interaction with API</b>",
        'repo_link': "https://github.com/Sailesh-Bhoite/Currency-Convertor",
        'video_link': "https://www.linkedin.com/posts/sailesh-bhoite_techmindsmarathon-techminds-activity-7289552747534651393-cM6b?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEgWZHsBTswwPEbC-Z3cAWUiezWgCnj6xf4",
        'demo_link': None,
        'demo_image': "Currency_Conv_demo.png",
    },
    {
        'title': "Hospital Database Management Website",
        'desc': "A Django Hospital Database Management System website.<br> 𝐊𝐞𝐲 𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬: 𝐀𝐩𝐩𝐨𝐢𝐧𝐭𝐦𝐞𝐧𝐭 𝐁𝐨𝐨𝐤𝐢𝐧𝐠, 𝐀𝐩𝐩𝐨𝐢𝐧𝐭𝐦𝐞𝐧𝐭 𝐇𝐢𝐬𝐭𝐨𝐫𝐲, 𝐃𝐨𝐜𝐭𝐨𝐫 𝐏𝐨𝐫𝐭𝐚l, 𝐔𝐬𝐞𝐫 𝐒𝐞𝐬𝐬𝐢𝐨𝐧𝐬.",
        'repo_link': "https://github.com/Fantastic-III/Hospital-Management",
        'video_link': "https://www.linkedin.com/posts/sailesh-bhoite_%F0%9D%90%84%F0%9D%90%B1%F0%9D%90%9C%F0%9D%90%A2%F0%9D%90%AD%F0%9D%90%A2%F0%9D%90%A7%F0%9D%90%A0-%F0%9D%90%8C%F0%9D%90%A2%F0%9D%90%A5%F0%9D%90%9E%F0%9D%90%AC%F0%9D%90%AD%F0%9D%90%A8%F0%9D%90%A7%F0%9D%90%9E-%F0%9D%90%80-activity-7286766868546146304-1JZ1?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEgWZHsBTswwPEbC-Z3cAWUiezWgCnj6xf4",
        'demo_link': None,
        'demo_image': "Hospital_DB_demo.png",
    },
    {
        'title': "Car Sales Data Visualization",
        'desc': "A 'Streamlit' website that visualizes a dataset it to gain some important insights.",
        'repo_link': "https://github.com/Sailesh-Bhoite/Car-Sales-Data-Visualization",
        'video_link': "https://www.linkedin.com/posts/sailesh-bhoite_techminds-techmindsmarathon-activity-7293486152148254722-4TpA?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEgWZHsBTswwPEbC-Z3cAWUiezWgCnj6xf4",
        'demo_link': "https://car-sales-data-visualization.streamlit.app/",
        'demo_image': "Car_DV_demo.png",
    },
]

for work in works:
    st.markdown("""---""")
    # Main container
    with st.expander(label=f'{work['title']}'):
        # Description container
        with st.container(border=True):
            st.markdown(
                f"""
                <div style="display: flex; justify-content: center; align-items: center; min-height: 100px; ">
                    <p style="text-align: center;">{work['desc']}</p>
                </div>
                """,
                unsafe_allow_html=True)

        if work['demo_image']:
            with st.container(border=True):
                st.image(f"{image_path}/{work['demo_image']}")

        # GitHub and Video Link container
        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                with st.container(border=True):
                    st.markdown(
                        f"""
                        <div style="display: flex; justify-content: center; align-items: center; min-height: 100px; ">
                            <a href="{work['repo_link']}">Source Code</a>
                        </div>
                        """,
                        unsafe_allow_html=True)
            with col2:
                with st.container(border=True):
                    st.markdown(
                        f"""
                        <div style="display: flex; justify-content: center; align-items: center; min-height: 100px; ">
                            <a href="{work['video_link']}">Demo Video</a>
                        </div>
                        """,
                        unsafe_allow_html=True)

        # Demo Link container
        if work['demo_link']:
            with st.container(border=True):
                st.markdown(
                    f"""
                    <div style="display: flex; justify-content: center; align-items: center; min-height: 100px;">
                        <a href="{work['demo_link']}">Live Demo</a>
                    </div>
                    """,
                    unsafe_allow_html=True)

st.markdown("""---""")
