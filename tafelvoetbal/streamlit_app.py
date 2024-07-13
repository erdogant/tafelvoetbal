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
from tab_players import tab_players
from tab_statistics import tab_statistics
from tab_sidebar import tab_sidebar
from helper import ethical_adds

import warnings
warnings.filterwarnings("ignore")
set_default_local_params()


# %% Main
def main():
    # Create tabs
    welcome_message = 'Tafelvoetbal! 🚀'
    # Set tabs after logging in
    tabs = st.tabs(['Game', 'Account/ Players', 'Statistics'])

    # Tabs
    with tabs[0]:
        tab_scoreboard()
    with tabs[1]:
        tab_players()
    with tabs[2]:
        tab_statistics()

    # Ethical adds
    ethical_adds()
    # Create the left-sidebar
    tab_sidebar(welcome_message)


# %% Main
if __name__ == "__main__":
    st.set_page_config(layout="centered", page_title="Tafelvoetbal", page_icon="🚀")
    main()
