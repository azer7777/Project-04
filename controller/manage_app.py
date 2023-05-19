from model.player import Player
from views.entries import Entries

class Manager:
    def add_player():
        Entries.get_player_entries()
        Player.load_player_to_json_file()
        
        
    

 


Manager.add_player()
