
import streamlit as st  
from streamlit_option_menu import option_menu




# with st.sidebar:
    # 1 Side bar 
    # selected = option_menu(
    #     menu_title= "Main Menu" ,# if required give name like (menu_title="Main Menu")or it can be kept blank "None"
    #     options=["Home","Projects","Contact"],
    #     icons=["house","collection-play","person-lines-fill"],
    #     menu_icon="cast",
    #     default_index=0,
    # )
    
# 2 horizontal menu 
with st.sidebar:
    selected = option_menu(
        menu_title= None,# if required give name like (menu_title="Main Menu")or it can be kept blank "None"
        options=["Home","Projects","Contact"],
        icons=["house","collection-play","person-lines-fill"],
        # menu_icon="cast",
        default_index=0,
        orientation="horizontal",
    )

if selected == "Home":
    st.title(f"You have selected {selected}")
    
if selected == "Projects":
    st.title(f"You have selected {selected}")
    
if selected == "Contact":
    st.title(f" selected {selected}")

#st.title(" Streamlit Option Menu")