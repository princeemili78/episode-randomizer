
import requests
import pandas as pd

class TvShow:
    """Creates instance of TV show you want to watch

    :param title: title of the TV show
    """

    def __init__(self, show_name):
        self.show_name = show_name
        self.show_json = self.get_show_json()
        self.title_id = self.get_title_id()
        self.episodes_json = self.get_episodes_json()



# Add string for show name to the end of the api address to show json  
    def get_show_json(self):
        r = requests.get("https://api.tvmaze.com/singlesearch/shows?q=" + self.show_name)
        
        return r.json()
    
    def get_title_id(self):
        id = self.show_json["id"]
        return id
# Get JSON for episodes data. needs dif URL
    def get_episodes_json(self):
        r = requests.get("https://api.tvmaze.com/shows/" + str(self.title_id) + "/episodes")
        return r.json()



        


