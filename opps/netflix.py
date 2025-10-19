from abc import ABC, abstractmethod 

class Content(ABC):
    def __init__(self, id, title, gener, duration, release_year):
        self.id = id
        self.title = title 
        self.gener = gener 
        self.duration = duration
        self.release_year = release_year 
    

    @abstractmethod
    def get_content(self):
        pass 

class Rate:
    def __init__(self, content, user, rate):
        self.content = content 
        self.rate = rate 
        self.user = user


class Movie(Content):
    def __init__(self, id, title, gener, duration, release_year)
        super().__init__(id, title, gener, duration, release_year)


    def get_content(self):
        pass
    
class TvShow(Content):
    def __init__(self, id, title, gener, duration, release_year, episode_id)
        super().__init__(id, title, gener, duration, release_year)
        self.episode_id = episode_id
    
    def get_content(self):
        pass

class Plan:
    def __init__(self, no_of_devices, streaming_quality, monthly_cost):
        self.no_of_devices = no.of.devices
        self.streaming_quality = streaming_quality 
        self.monthly_cost = monthly_cost 

    
class User:
    def __init__(self, id, name, plan):
        self.id = id 
        self.name = name 
        self.plan = plan 

    def rate_content(self, content, rate):
        pass 

class UserWatching:
    def __init__(self, content, user):
        self.content = context 
        self.user = user 

    def pause(self):
        pass

    def  play(self):

    def resume(self);
    pass     







