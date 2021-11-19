from app.controllers.controllers import  create_new, get_all, get_one
from app.exceptions.exceptions import InvalidKeys


class Anime():
    
    def __init__(self, anime: str, released_date: str, seasons: int) -> None:
        self.anime = anime.lower().title()
        self.released_date = released_date
        self.seasons = seasons

    
    @staticmethod
    def get_all_animes():
        return get_all()

    def create_anime(self):
        data = self.__dict__
      
        
        create_new(data)
        return data
    
    @staticmethod
    def check_data(data):
        correct_keys = ["anime", "released_date", "seasons"]
        data_keys = data.keys()
        errors_keys = list(set(data_keys) - set(correct_keys))

        if errors_keys:
           raise InvalidKeys({'available_keys': correct_keys, 'wrong_keys_sended': errors_keys})
       

    @staticmethod
    def get_one_anime(data):
        data_int = int(data)
        return get_one(data_int)
    
    
        
        