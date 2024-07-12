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
from helper import timestamp
from dbase import Dbase
import time


# %%
def tab_players():
    # Show players
    manage_players()
    # Show accounts
    manage_accounts()


# %%
def manage_players():
    st.write('Speler')
    with st.form(key='Store user', border=True):

        cols = st.columns([1, 1], gap="small")
        with cols[0]:
            input_name = st.text_input(label='Naam', help='Name')
        with cols[1]:
            input_team = st.text_input(label='Account name', disabled=True, placeholder=st.session_state['ACCOUNT'])

        cols = st.columns([1, 1], gap="small")
        with cols[0]:
            input_organisatie = st.text_input(label='Organisatie', help='Organisatie')
        with cols[1]:
            input_department = st.text_input(label='Afdeling', help='Afdeling')

        with cols[0]:
            user_functie = st.selectbox(label="Wannabe", label_visibility="visible", options=['Data Engineer', 'Data Scientist', 'BI Specialist', 'Data Steward', 'Modelleur', 'Batman', 'UX', 'Software Ontwikkelaar', 'Superman', 'Product Owner', 'Scrum Master', 'Wolverine', 'Front-End ontwikkelaar', 'Anders'], placeholder='select', index=None, help='Als ik later groot ben dan wil ik worden')
        with cols[1]:
            input_leeftijd = st.number_input(label='Gevoelsleeftijd', min_value=18, max_value=65, step=1, help='The age I feel like.')

        with cols[0]:
            user_drinks = st.selectbox(label="Type", label_visibility="visible", options=['Coffee', 'Thee', 'Water'], index=None)
        with cols[1]:
            pass

        cols = st.columns([1, 1, 1], gap="small")
        with cols[0]:
            push_store = st.form_submit_button('Add new player', type='primary')
        with cols[1]:
            check_overwrite = st.checkbox('Overwrite', value=False)

        if push_store:
            if st.session_state['client'] is None:
                st.error('You need to load a team first using your account name.')
            elif input_name != '':
                # Check whether user data exists already
                db = st.session_state['client']
                # Get user data
                user_data = db.get_entry(document='USERS', values=input_name)

                if (user_data is None or check_overwrite):
                    st.info(f'{input_name} is stored in account {st.session_state["ACCOUNT"]}.')
                    # if user_data is None:
                    db.update(document='USERS', values={input_name: {'department': input_department,
                                                                     'organisation': input_organisatie,
                                                                     'function': user_functie,
                                                                     'age': input_leeftijd,
                                                                     'drinks': user_drinks,
                                                                     }}, verbose=True)
                    # Get data
                    data = db.get_entry()
                    # Set session states
                    st.session_state['PLAYERS'] = [*data['USERS'].keys()]
                    time.sleep(3)
                    st.rerun()
                else:
                    st.error(f'{input_name} already exists.')
            else:
                st.error(f'Load team account first or set a correct name.')


# %%
def manage_accounts():
    with st.expander('Accounts', expanded=True):
        with st.form(key='Accounts', border=False):

            cols = st.columns([1, 1], gap="small")
            with cols[0]:
                input_accountname = st.text_input(label='Account name', help='Create new account and store the team members and scores!')

            cols = st.columns([1, 1, 1], gap="small")
            with cols[0]:
                push_store = st.form_submit_button('Create new account', type='primary')

            if push_store:
                if len(input_accountname.strip()) >= 3:
                    # Check whether user data exists already
                    db = Dbase(dbtype='firestore', projectname='tafelvoetbal-db', collection=input_accountname)

                    # Check status
                    if db.status == 'success':
                        # Check whether user data exists already
                        user_data = db.get_entry()

                    if (user_data is None):
                        st.info(f'{input_accountname} is stored/updated in database.')
                        # Set info
                        db.create_entry(document='MATCH', overwrite=True)
                        db.create_entry(document='USERS', overwrite=True)
                        db.create_entry(document='settings', overwrite=True)
                        # Store the client for later usage
                        st.session_state['client'] = db
                        st.session_state['ACCOUNT'] = input_accountname.strip().lower()
                        st.session_state['PLAYERS'] = []
                        time.sleep(3)
                        st.rerun()
                    else:
                        st.error(f'{input_accountname} already exists. Choose another one.')
                else:
                    st.error(f'{input_accountname} is not valid. Shoud be more then 3 characters.')
