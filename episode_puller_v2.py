import requests
import random



class Episode:
    """Creates episode objects
    :param episode_info: dictionary for each episode from API
    :ivar name: name of episode
    :ivar rating: IMDb rating for episode

    """
    def __init__(self, episode_info):
        self.episode_info = episode_info
        self.season_and_number = f"S{self.episode_info["season"]}E{self.episode_info["number"]}"
        self.season = self.episode_info["season"]
        self.name = self.episode_info["name"]
        self.rating = self.episode_info["rating"]["average"]
        self.type = episode_info["type"]



class TvShow:
    """Creates instance of TV show you want to watch

    :param show_name: title of the TV show
    :ivar show_json: json for entire show returned
    :ivar title_id: ID for show on TVAPI
    :ivar seasons: List of seasons object corresponding to number of seasons in show
    """

    def __init__(self, show_name):
        self.show_name = show_name
        self.show_json = self.get_show_json()
        self.title_id = self.get_title_id()
        self.all_episodes = self.get_all_episodes()
        self.num_seasons = self.all_episodes[-1].season



# Add string for show name to the end of the api address to show json  
    def get_show_json(self):
        r = requests.get("https://api.tvmaze.com/singlesearch/shows?q=" + self.show_name)
        
        return r.json()
    
    def get_title_id(self):
        id = self.show_json["id"]
        return id


    def get_all_episodes(self):
        episodes_json = requests.get(f"https://api.tvmaze.com/shows/{self.title_id}/episodes").json()
        
        return [Episode(e) for e in episodes_json]
        
# Return random episode 
    def random_episode(self, rating=0, seasons=None):
        if latest_season is None:
            seasons = [num for num in range(self.num_seasons)]

        # Create list of episodes that satisfy the user's requirements by filtering with a list comprehension
        valid_episodes = [e for e in self.all_episodes if e.rating != None and e.season in seasons]
        if len(valid_episodes) == 0:
            return "Ur rating is too high fuck nigga, lower ur standards"
        episode = random.choice(valid_episodes)

        return f"{episode.season_and_number} {episode.name}"
        