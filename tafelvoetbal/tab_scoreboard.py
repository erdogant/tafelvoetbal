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

        with top_cols[1]:
            player2 = st.number_input(label="Score team 1", label_visibility="collapsed", min_value=0, max_value=10, step=1)
        with top_cols[1]:
            st.image('https://raw.githubusercontent.com/erdogant/tafelvoetbal/main/tafelvoetbal/data/tafelvoetbal_top.png')

        top_cols_players = st.columns([1, 2, 1], gap="small")
        with top_cols_players[0]:
            player1 = st.selectbox(label="Speler 1", label_visibility="collapsed", options=['naam1', 'naam2'], index=0)
        with top_cols_players[1]:
            st.image('https://raw.githubusercontent.com/erdogant/tafelvoetbal/main/tafelvoetbal/data/tafelvoetbal_middle_top.png')
        with top_cols_players[2]:
            player2 = st.selectbox(label="Speler 2", label_visibility="collapsed", options=['naam1', 'naam2'], index=0)

        mid_cols = st.columns([1, 2, 1], gap="small")
        with mid_cols[1]:
            st.image('https://raw.githubusercontent.com/erdogant/tafelvoetbal/main/tafelvoetbal/data/tafelvoetbal_middle_middle.png')

        down_cols_players = st.columns([1, 2, 1], gap="small")
        with down_cols_players[0]:
            player3 = st.selectbox(label="Speler 3", label_visibility="collapsed", options=['naam1', 'naam2'], index=0)
        with down_cols_players[1]:
            st.image('https://raw.githubusercontent.com/erdogant/tafelvoetbal/main/tafelvoetbal/data/tafelvoetbal_middle_bottom.png')
        with down_cols_players[2]:
            player4 = st.selectbox(label="Speler 4", label_visibility="collapsed", options=['naam1', 'naam2'], index=0)

        bottom_cols = st.columns([1, 2, 1], gap="small")
        with bottom_cols[1]:
            st.image('https://raw.githubusercontent.com/erdogant/tafelvoetbal/main/tafelvoetbal/data/tafelvoetbal_bottom.png')

        with bottom_cols[1]:
            score2 = st.number_input(label="Score team 2", label_visibility="collapsed", min_value=0, max_value=10, step=1)

        # Display the image in the middle
        # with top_cols[1]:
        #     st.image('https://raw.githubusercontent.com/erdogant/tafelvoetbal/main/tafelvoetbal/data/tafelvoetbal_middle.png')

        # # Create the layout for the bottom row (bottom-left and bottom-right)
        # bottom_cols = st.columns([1, 2, 1], gap="small")

        # with bottom_cols[0]:
        #     player3 = st.selectbox(label="Speler 3", label_visibility="collapsed", options=['naam1', 'naam2'], index=0)
        # with bottom_cols[2]:
        #     player4 = st.selectbox(label="Speler 4", label_visibility="collapsed", options=['naam1', 'naam2'], index=0)
        # with bottom_cols[1]:
        #     player2 = st.number_input(label="Score team 2", label_visibility="collapsed", min_value=0, max_value=10, step=1)

