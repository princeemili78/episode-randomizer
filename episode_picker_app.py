import streamlit as st
from episode_puller_v2 import TvShow
from episode_puller_v2 import Episode
from episode_puller_v2 import fuzzy_search_result


st.title("Random Episodes", text_alignment="center")
#st.popover("Help", type="tertiary")


if "show" not in st.session_state:
    st.session_state["show"] = ""
    
if "show_name" not in st.session_state:   
    st.session_state["show_name"] = ""
if "episode_generated" not in st.session_state:
    st.session_state["episode_generated"] = False
if "episode" not in st.session_state:
    st.session_state["episode"] = ""
if "rating" not in st.session_state:
    st.session_state["rating"] = None
if "seasons" not in st.session_state:
    st.session_state["seasons"] = []

if st.session_state["episode_generated"] == False:
    # textbox for user to input show name
    show_name = st.text_input("Name of Tv Show", help="Type name of show")
    




    # create instance of tv show using user input
    if show_name != "" and st.session_state["show_name"] != show_name :
        try:
            st.session_state["show"] = TvShow(show_name)
            st.session_state["show_name"] = show_name
        except Exception as e:     
            try:
                st.write(f" Did you mean {fuzzy_search_result(show_name)}")
                st.session_state["show"] = ""
                st.session_state["show_name"] = show_name
            except:
                st.write("Couldn't find a show with that name")
                st.session_state["show"] = ""
                st.session_state["show_name"] = show_name
        



    if isinstance(st.session_state["show"], TvShow):
        st.image(st.session_state["show"].picture)         
        rating = st.number_input("Lowest rating", min_value=0.0, max_value=10.0, value=st.session_state["rating"],format="%0.1f", help="Type the lowest rated episode you'd watch", step=0.5) 
        seasons = st.multiselect("Seasons", options=st.session_state["show"].season_list, default=st.session_state["seasons"], help="Select seasons to choose from", placeholder="Choose seasons")
        if st.button("Generate episode!") == True:
            try:
                episode = st.session_state["show"].random_episode(rating, seasons)
                if isinstance(episode, Episode):
                    st.session_state["episode"] = episode
                    st.session_state["rating"] = rating
                    st.session_state["seasons"] = seasons
                    st.session_state["episode_generated"] = True
                    st.rerun()
            except Exception as e:
                st.write(e)

else:
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Back") == True:
            st.session_state["episode"] = ""
            st.session_state["episode_generated"] = False
            st.rerun()
    st.markdown(f"# {st.session_state["episode"].name}")

    st.components.v1.iframe(f"https://vidsrc-embed.ru/embed/tv/{st.session_state["episode"].imdb_id}/{st.session_state["episode"].season}-{st.session_state["episode"].number}", height=500)

    col3, col4 = st.columns([.69, .31])
    with col3:
        st.markdown(f"{st.session_state["episode"].season_and_number}") 
        st.markdown(f"{st.session_state["episode"].rating}:star:")
    with col4:
        if st.button("Generate another episode!") == True:
                try:
                    episode = st.session_state["show"].random_episode(st.session_state["rating"], st.session_state["seasons"])
                    if isinstance(episode, Episode):
                        st.session_state["episode"] = episode
                        st.session_state["episode_generated"] = True
                except Exception as e:
                    st.write(e)
    col5, col6 = st.columns(2)
    col5.image(st.session_state["episode"].image)  
    col6.markdown(st.session_state["episode"].summary)      
        
    