"""Local parameters for tafelvoetbal.

"""
import streamlit as st
import copy
from tab_sidebar import clean_dict

# %%
def set_default_local_params():
    if 'FIG_PATH' not in st.session_state: st.session_state['FIG_PATH'] = r'https://raw.githubusercontent.com/erdogant/tafelvoetbal/main/tafelvoetbal/data/'
    if 'PLAYERS' not in st.session_state: st.session_state['PLAYERS'] = []
    if 'DATA' not in st.session_state: st.session_state['DATA'] = clean_dict()
    if 'ACCOUNT' not in st.session_state: st.session_state['ACCOUNT'] = None
    if 'client' not in st.session_state: st.session_state['client'] = None
    if 'NEWGAME' not in st.session_state: st.session_state['NEWGAME'] = None
    if 'SCORE1' not in st.session_state: st.session_state['SCORE1'] = 0
    if 'SCORE2' not in st.session_state: st.session_state['SCORE2'] = 0

