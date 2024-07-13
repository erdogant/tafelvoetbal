import streamlit as st
from datetime import datetime
# import datetime
import requests
# from streamlit_theme import st_theme
from datetime import time as dttime
import streamlit.components.v1 as components


# %%
def ethical_adds():
    # Your HTML and JavaScript code
    html_code = """
    <br>
    <center>
        <script async src="https://media.ethicalads.io/media/client/ethicalads.min.js"></script>
        <div data-ea-publisher="erdogantgithubio" data-ea-type="text"></div>
    </center>
    """

    # Embedding the HTML code in the Streamlit app
    components.html(html_code, height=200)
    
# %%
def check_internet_connection(website='https://www.google.com'):
    """Check internet connection."""
    try:
        response = requests.get(website)
        return response.status_code == 200 or response.status_code == 502
    except requests.ConnectionError:
        return False

def timestamp(dt_format='ts'):
    return datetime.now().strftime(datetime_format(dt_format))


def datetime_format(dt_format='full'):
    """
    Return the datetime format based on the input dt_format.

    Parameters:
    dt_format (str): The format type to return. Default is 'full'.
        'full' : "%d-%m-%Y %H:%M"
        'ts'   : "%d_%m_%Y_%H%M"
        'date' : "%d-%m-%Y"
        'time' : "%H:%M"

    Returns:
    str: The formatted datetime string.

    Example:
    >>> datetime_format('full')
    'dd-mm-yyyy hh:mm:ss'
    """
    if dt_format=='ts':
        return "%d_%m_%Y_%H%M"
    if dt_format=='tsec':
        return "%d_%m_%Y_%H%M%S"
    if dt_format=='full':
        return "%d-%m-%Y %H:%M"
    elif dt_format=='date':
        return "%d-%m-%Y"
    elif dt_format=='time':
        return "%H:%M"


# %%
# def theme_color():
#     theme = st_theme()
#     return theme


def save_and_refresh_button():

    with st.container(border=True):
        cols = st.columns(4, gap="small")
        with cols[0]:
            save_button_tabs = st.button("Save score!", type='primary')

            # Set the name if not exists
            if save_button_tabs:
                st.warning('*Save button')

            # Store
            if save_button_tabs:
                pass
                # getdatetime = datetime.now().strftime(datetime_format('full'))
                # st.session_state['DATA']['GENERAL']['NAME'] = st.session_state['scoreplan'].replace('.json', '')
                # # Dump the score
                # if st.session_state['DBTYPE']['scoreplan'] == 'firestore':
                #     # Dump to firestore
                #     scoreplan = clean_collection_name_firestore(st.session_state['scoreplan'])
                #     # Dump in firestore
                #     db = st.session_state['STORAGE']['firestore']['client']
                #     db.create_entry(document='scoreplan', values={scoreplan: st.session_state['DATA']}, overwrite=False)

                st.success('*saved:* ***', icon="✅")

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