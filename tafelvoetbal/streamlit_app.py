"""Main page for SkyWalk.

# --------------------------------------------------
# Name        : tafelvoetbal.py
# Author      : E.Taskesen
# Contact     : erdogant@gmail.com
# github      : https://github.com/erdogant/tafelvoetbal
# Licence     : See licences
# --------------------------------------------------

"""

import streamlit as st
from local_params import set_default_local_params
from tab_scoreboard import tab_scoreboard
from tab_spelers import tab_spelers
from tab_settings import tab_settings
from tab_sidebar import tab_sidebar
# import extra_streamlit_components as stx
from helper import save_and_refresh_button

import warnings
warnings.filterwarnings("ignore")

# Set local parameters
set_default_local_params()



# %% Main
def main():
    # Create tabs
    welcome_message = 'Tafelvoetbal! 🚀'

    # Set tabs after logging in
    tabs = st.tabs(['Scoreboard', 'Spelers','Settings'])

    # Tabs
    with tabs[0]:
        tab_scoreboard()
    with tabs[1]:
        tab_spelers()
    with tabs[2]:
        tab_settings()

    # Create the left-sidebar
    tab_sidebar(welcome_message)
    # Save and refresh button
    save_and_refresh_button()



# %% Main
if __name__ == "__main__":
    st.set_page_config(layout="centered", page_title="Tafelvoetbal", page_icon="🚀")
    main()
