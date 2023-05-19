from models.player import Player
from views.entries import Entries

class Manager:
    def add_player():
        player_entries = Entries.get_player_entries()
        Player(player_entries[0], player_entries[1], player_entries[2]).load_player_to_json_file()
        return
        
        
    

 



