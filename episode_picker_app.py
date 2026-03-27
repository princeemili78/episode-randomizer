import streamlit as st
from episode_puller_v2 import TvShow

# textbox for user to input show name
show_name = st.text_input("Name of Tv Show")

# create instance of tv show using user input
show = TvShow(show_name)


st.write(str(show.title_id))