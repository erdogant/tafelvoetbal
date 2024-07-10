import streamlit as st
from datetime import datetime
from streamlit_theme import st_theme

# %%
def theme_color():
    theme = st_theme()
    return theme


def save_and_refresh_button():

    with st.container(border=True):
        cols = st.columns(4, gap="small")
        with cols[0]:
            save_button_tabs = st.button("Save score!", type='primary')

            # Set the name if not exists
            if save_button_tabs and st.session_state['FLIGHTPLAN_NAME'] == '':
                st.warning('*Flightplan was not initially created. The default name is therefore set to [%s]* ***' %(st.session_state['FLIGHTPLAN_NAME']))

            # Store
            if save_button_tabs:
                pass
                # getdatetime = datetime.now().strftime(datetime_format('full'))
                # st.session_state['DATA']['GENERAL']['NAME'] = st.session_state['FLIGHTPLAN_NAME'].replace('.json', '')
                # # Dump the flightplan
                # if st.session_state['DBTYPE']['flightplans'] == 'firestore':
                #     # Dump to firestore
                #     name_flightplan_wrapped = clean_collection_name_firestore(st.session_state['FLIGHTPLAN_NAME'])
                #     # Dump in firestore
                #     db = st.session_state['STORAGE']['firestore']['client']
                #     db.create_entry(document='flightplans', values={name_flightplan_wrapped: st.session_state['DATA']}, overwrite=False)

                st.success('*Flightplan saved:* ***' + st.session_state['FLIGHTPLAN_NAME'] + '***', icon="✅")

        with cols[1]:
            refresh_button = st.button('Refresh page!', help='Always update the page to make sure all **new** information is processed.')
            if refresh_button:
                st.rerun()

        with cols[2]:
            submit_logout = st.button("Logout")
            if submit_logout:
                # Show message
                st.info('**Logout.. cleaning variables..**', icon="✅")
                # Set user session state
                st.session_state['USER'] = {'id': None, 'subscription': False, 'password': False, 'dbstatus': False, 'logged_in': False}
                # Clear cache
                st.cache_resource.clear()
                st.cache_data.clear()
                # time.sleep(3)
                # Rerun
                st.rerun()