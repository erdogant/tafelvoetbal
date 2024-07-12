"""Sidebar.

# Name        : tafelvoetbal.py
# Author      : E.Taskesen
# Contact     : erdogant@gmail.com
# github      : https://github.com/erdogant/tafelvoetbal
# Licence     : See licences

"""

import streamlit as st
from helper import timestamp
import os
from dbase import Dbase
import time
import json


# %%
def tab_sidebar(welcome_message):

    st.sidebar.title('Tafelvoetbal')

    # Load
    with st.sidebar.form(key='Account'):
        accountname = st.text_input(label='Load team members from account', help='Load team members using your account name.', value=st.session_state['ACCOUNT'])
        load_account_data = st.form_submit_button("Load Players")

        if load_account_data and len(accountname) > 0:
            # Get client data
            db = Dbase(dbtype='firestore', projectname='tafelvoetbal-db', collection=accountname)
            if db.status == 'success':
                user_data = db.get_entry()
                if (user_data is None):
                    st.error(f'{accountname} does not exists. Create one first.')
                    return
                else:
                    # Get data
                    data = db.get_entry()
                    # Set session states
                    users = data['USERS']
                    st.session_state['PLAYERS'] = [*users.keys()]
                    # Store in session
                    st.session_state['client'] = db
                    st.session_state['ACCOUNT'] = accountname
                    # Show message
                    st.success(f'{accountname} loaded')
                    time.sleep(3)
                    st.rerun()


    with st.sidebar.form(key ='sidebar_save'):
        cols = st.columns([1, 1], gap="small")
        with cols[0]:
            new_button = st.form_submit_button("New Game!", type='primary', help='Clear all players and scores and start again.')
        with cols[1]:
            save_button_tabs = st.form_submit_button("Save Game!", help='After saving the game, it can not be saved again!')

        # New
        if new_button:
            new_game()
        # Save
        if save_button_tabs:
            save_game()

# %%
def save_game():
    if st.session_state['NEWGAME'] is None:
        st.error('Create new game first!')
        return
    if st.session_state['SCORE1'] == 0 and st.session_state['SCORE2'] == 0:
        st.error('A game without goals is not saved.')
        return

    if st.session_state['ACCOUNT'] is not None and st.session_state['client'] is not None:
        # Set savetime
        st.session_state['DATA']['metadata']['savetime'] = timestamp(dt_format='ts')
        # Convert to json
        json_data = json.dumps(st.session_state['DATA'])
        # Initialize db
        db = st.session_state['client']
        # Store 
        db.create_entry(document='MATCH', values={st.session_state['DATA']['datetime']: json_data}, overwrite=False)
        # db.update(document='MATCH', values={st.session_state['DATA']['datetime']: json_data})
        # Show finish
        st.success(f'Game {st.session_state["NEWGAME"]} is Saved!', icon="✅")
        st.info(f'Game cleaned for the next round.')

        # Set to defaults
        st.session_state['NEWGAME'] = None
        st.session_state['DATA'] = clean_dict()
        time.sleep(3)
        st.rerun()
    else:
        st.error('Load account first')


def new_game():
    if st.session_state['SCORE1'] > 0 or st.session_state['SCORE2'] > 0:
        st.error('Set the team scores to 0 first.')
        return

    # from local_params import clean_dict
    datetime = timestamp(dt_format='ts')
    st.session_state['DATA'] = clean_dict()
    st.session_state['NEWGAME'] = datetime
    st.success('New Game!', icon="✅")
    st.balloons()
    time.sleep(3)
    st.rerun()

def clean_dict():
    return {'datetime': timestamp(dt_format='ts'),
     'metadata': {'savetime': None},
     'team1': {'player1': None, 'player2': None, 'score': 0, 'timestamp': []},
     'team2': {'player1': None, 'player2': None, 'score': 0, 'timestamp': []},
     }