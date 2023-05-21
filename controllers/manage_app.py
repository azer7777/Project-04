from models.player import Player
from models.save_load import SaveLoad
from views.entries import Entries

class Manager:
    def add_player():
        player_entries = Entries.get_player_entries()
        player_info_serialized = Player(player_entries[0], player_entries[1], player_entries[2]).save_player_to_json_file()
        SaveLoad.save(player_info_serialized, file_name="players_data")
        return
        
        
    

 



