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
import os

# %%
def tab_scoreboard():
    with st.container():
        # Create the layout for the top row (top-left and top-right)
        top_cols = st.columns([1, 2, 1], gap="small")

        with top_cols[0]:
            player1 = st.selectbox(label="Speler 1", label_visibility="collapsed", options=['naam1', 'naam2'], index=0)
        with top_cols[2]:
            player2 = st.selectbox(label="Speler 2", label_visibility="collapsed", options=['naam1', 'naam2'], index=0)
        with top_cols[1]:
            player2 = st.number_input(label="Score team 1", label_visibility="collapsed", min_value=0, max_value=10, step=1)

        # Display the image in the middle
        with top_cols[1]:
            # st.image('./data/tafelvoetbal.png')
            st.image('https://raw.githubusercontent.com/erdogant/tafelvoetbal/main/tafelvoetbal/data/tafelvoetbal.png')

        # Create the layout for the bottom row (bottom-left and bottom-right)
        bottom_cols = st.columns([1, 2, 1], gap="small")

        with bottom_cols[0]:
            player3 = st.selectbox(label="Speler 3", label_visibility="collapsed", options=['naam1', 'naam2'], index=0)
        with bottom_cols[2]:
            player4 = st.selectbox(label="Speler 4", label_visibility="collapsed", options=['naam1', 'naam2'], index=0)
        with bottom_cols[1]:
            player2 = st.number_input(label="Score team 2", label_visibility="collapsed", min_value=0, max_value=10, step=1)

