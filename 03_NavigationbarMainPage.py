import streamlit as st
from streamlit_navigation_bar import st_navbar
import os

import pages as pg

page = st_navbar(["Home", "Documentation", "Examples", "Community", "About"],
                #  options={"use_padding": False}
                )
st.write(page)

