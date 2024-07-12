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
from dbase import Dbase
import json
import pandas as pd
from datetime import datetime

# %%
def tab_statistics():
    st.write('Statistics')
    with st.form(key='Statistics', border=True):
        load_table = st.form_submit_button('Load table')
        df = pd.DataFrame()

        if load_table:
            if st.session_state['client'] is None:
                st.error('No account loaded.')

                return
            db = st.session_state['client']
            # Get data
            data = db.get_entry()
            # Set session states
            json_data = data['MATCH']
            # Convert json data

            rows = []
            for key in json_data.keys():
                data = json.loads(json_data[key])
                row = {
                    'team1_player1': data['team1']['player1'],
                    'team1_player2': data['team1']['player2'],
                    'team2_player1': data['team2']['player1'],
                    'team2_player2': data['team2']['player2'],
                    'score team 1': data['team1']['score'],
                    'score team 2': data['team2']['score'],
                    'total_time_in_minutes': time_difference(data['datetime'], data['metadata']['savetime']),
                    'team1_time_variation_between_goals_in_minutes': time_variation_in_minutes(data['team1']['timestamp']),
                    'team2_time_variation_between_goals_in_minutes': time_variation_in_minutes(data['team2']['timestamp']),
                }
                rows.append(row)
            # Create DataFrame from the list of rows
            df = pd.DataFrame(rows, columns=['team1_player1', 'team1_player2', 'team2_player1', 'team2_player2', 'score team 1', 'score team 2', 'total_time_in_minutes', 'team1_time_variation_between_goals_in_minutes', 'team2_time_variation_between_goals_in_minutes'])
            st.write(df)


def time_variation_in_minutes(timestamps):
    if len(timestamps) == 0:
        return None
    # Define the date format
    date_format = "%d_%m_%Y_%H%M%S"
    # Parse the timestamps to datetime objects
    times = [datetime.strptime(list(ts.values())[0], date_format) for ts in timestamps]
    # Compute the difference between the earliest and latest timestamps
    min_time = min(times)
    max_time = max(times)
    difference = (max_time - min_time).total_seconds() / 60
    # Return
    return difference

def time_difference(timestamp1, timestamp2):
    # Define the date format
    date_format = "%d_%m_%Y_%H%M"
    # Parse the timestamps
    time1 = datetime.strptime(timestamp1, date_format)
    time2 = datetime.strptime(timestamp2, date_format)
    # Compute the difference in seconds
    difference = (time2 - time1).total_seconds()
    # Return
    return difference / 60