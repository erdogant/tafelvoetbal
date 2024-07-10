"""Local parameters for tafelvoetbal.

"""

import streamlit as st
import copy

# %%
def set_default_local_params():
    if 'FIG_DIR' not in st.session_state: st.session_state['FIG_DIR'] = None

