import os
import streamlit as st
from streamlit_navigation_bar import st_navbar
import pages as pg


st.set_page_config(initial_sidebar_state="collapsed")



pages = ["Home", "Library", "Tutorials", "Development", "Download"]
parent_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(parent_dir, "sample.svg")
styles = {
    "nav": {
        # "background-color": "rgb(237, 167, 62)",
        "justify-content": "center",
    },
    "img": {
        "padding-right": "35px",
    },
    "div": {
        "max-width": "32rem",
    },
    "span": {
        "border-radius": "0.5rem",
        "color": "rgb(237, 247, 247)",#49, 51, 63
        "margin": "0 0.125rem",
        "padding": "14px",
    },
    "active": {
        "background-color": "rgba(255, 255, 255, 0.25)","padding": "14px"
    },
    "hover": {
        "background-color": "rgba(255, 255, 255, 0.35)",
    },
}

options = {
    "show_menu": False,
    "show_sidebar": False,
}

page = st_navbar(pages,logo_path=logo_path, styles=styles)
st.write(page)

with st.sidebar:
    st.write("Sidebar")
