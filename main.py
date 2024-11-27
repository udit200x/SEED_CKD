import streamlit as st

from streamlit_option_menu import option_menu
import os
import home, about, login, contact, test

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"]{{
background-image: url("https://images.unsplash.com/photo-1478760329108-5c3ed9d495a0?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTl8fGRhcmt8ZW58MHx8MHx8fDA%3D");
background-size: 180%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
background-size: cover;
}}

[data-testid="stSidebar"] > div:first-child {{
background-image: url("https://images.unsplash.com/photo-1637775297458-7443ffd545b2?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8YmxhY2t8ZW58MHx8MHx8fDA%3D");
background-position: center; 
background-repeat: no-repeat;
background-attachment: fixed;
background-size: cover;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}


[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)




class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        # app = st.sidebar(
        with st.sidebar:        
            app = option_menu(
                menu_title='CKD Prediction ',
                options=['Home','Login','CKD Risk Predictor','About','Contact'],
                icons=['house-fill','person-circle','graph-up','info-circle-fill','chat-fill'],
                menu_icon='file-earmark-medical-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
        "nav-link-selected": {"background-color": "#02ab21"},}
                
                )

        
        if app == "Home":
            home.app()
        if app == "Login":
            login.app()    
        if app == "CKD Risk Predictor":
            test.app()        
        if app == 'About':
            about.app()    
        if app=='Contact':
            contact.app()    
             
          
             
    run()            