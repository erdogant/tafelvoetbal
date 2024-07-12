"""Main page.

# Name        : tafelvoetbal.py
# Author      : E.Taskesen
# Contact     : erdogant@gmail.com
# github      : https://github.com/erdogant/tafelvoetbal
# Licence     : See licences

"""
from helper import timestamp
import streamlit as st
import os

# %%
def tab_scoreboard():
    if st.session_state['NEWGAME'] is None:
        newgame = 'Create New Game!'
    else:
        newgame = st.session_state['NEWGAME']

    cols = st.columns([1, 3, 1], gap="small")
    with cols[1]:
        st.title(newgame)

    with st.container():
        # Create the layout for the top row (top-left and top-right)
        top_cols = st.columns([1, 2, 1], gap="small")

        with top_cols[0]:
            st.caption('Team 1')
        with top_cols[1]:
            st.session_state['SCORE1'] = st.number_input(label="Score team 1", label_visibility="collapsed", min_value=0, max_value=10, step=1)
        with top_cols[1]:
            st.image(os.path.join(st.session_state['FIG_PATH'], 'tafelvoetbal_top.png'))
        with top_cols[2]:
            st.caption('Team 2')

        top_cols_players = st.columns([1, 2, 1], gap="small")
        with top_cols_players[0]:
            team1_player1 = st.selectbox(label="Speler 1", label_visibility="collapsed", options=st.session_state['PLAYERS'], index=None)
        with top_cols_players[1]:
            st.image(os.path.join(st.session_state['FIG_PATH'], 'tafelvoetbal_middle_top.png'))
        with top_cols_players[2]:
            team1_player2 = st.selectbox(label="Speler 2", label_visibility="collapsed", options=st.session_state['PLAYERS'], index=None)

        mid_cols = st.columns([1, 2, 1], gap="small")
        with mid_cols[1]:
            st.image(os.path.join(st.session_state['FIG_PATH'], 'tafelvoetbal_middle_middle.png'))

        down_cols_players = st.columns([1, 2, 1], gap="small")
        with down_cols_players[0]:
            team2_player1 = st.selectbox(label="Speler 3", label_visibility="collapsed", options=st.session_state['PLAYERS'], index=None)
        with down_cols_players[1]:
            st.image(os.path.join(st.session_state['FIG_PATH'], 'tafelvoetbal_middle_bottom.png'))
        with down_cols_players[2]:
            team2_player2 = st.selectbox(label="Speler 4", label_visibility="collapsed", options=st.session_state['PLAYERS'], index=None)

        bottom_cols = st.columns([1, 2, 1], gap="small")
        with bottom_cols[1]:
            st.image(os.path.join(st.session_state['FIG_PATH'], 'tafelvoetbal_bottom.png'))
        with bottom_cols[1]:
            st.session_state['SCORE2'] = st.number_input(label="Score team 2", label_visibility="collapsed", min_value=0, max_value=10, step=1)

        if team1_player1 is not None:
            st.session_state['DATA']['team1']['player1'] = team1_player1
        if team2_player1 is not None:
            st.session_state['DATA']['team1']['player2'] = team2_player1
        if team1_player2 is not None:
            st.session_state['DATA']['team2']['player1'] = team1_player2
        if team2_player2 is not None:
            st.session_state['DATA']['team2']['player2'] = team2_player2

        if st.session_state['SCORE1'] > st.session_state['DATA']['team1']['score']:
            st.session_state['DATA']['team1']['score'] = st.session_state['SCORE1']
            st.session_state['DATA']['team1']['timestamp'].append({st.session_state['SCORE1']: timestamp('tsec')})
        if st.session_state['SCORE2'] > st.session_state['DATA']['team2']['score']:
            st.session_state['DATA']['team2']['score'] = st.session_state['SCORE2']
            st.session_state['DATA']['team2']['timestamp'].append({st.session_state['SCORE2']: timestamp('tsec')})
