"""Sidebar SkyWalk.

* Copyright (C) 2024-2025, E.Taskesen - All Rights Reserved
* Unauthorized copying of this file, via any medium is strictly prohibited Proprietary and confidential
* Written by Erdogan Taskesen, <erdogant@gmail.com>, April 2024

"""

import streamlit as st
# from streamlit_theme import st_theme
import os


# %%
def tab_sidebar(welcome_message):
    
    st.sidebar.title('Tafelvoetbal')

    # Load
    with st.sidebar.form(key ='sidebar_aircraft'):
        user_select = st.selectbox(label="Kies afdeling",
                                           label_visibility="visible",
                                           options=['DI-Lab'],
                                           placeholder='select',
                                           index=0)

        button_aircraft = st.form_submit_button("Load")


    # %% SAVE
    with st.sidebar.form(key ='sidebar_save'):
        save_button_tabs = st.form_submit_button("Save Score!")
        if save_button_tabs:
            save_score()

# %%
def save_score():
    st.success('Saved', icon="✅")

