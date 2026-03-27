import streamlit as st
from episode_puller_v2 import TvShow


show_name = st.text_input("Name of Tv Show")

show = TvShow(show_name)

page_bg_img = '''
<style>
body {
background-image: url(show.picture);
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

st.write(str(show.title_id))