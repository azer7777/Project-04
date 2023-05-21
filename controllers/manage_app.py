from models.player import Player
from models.save_load import SaveLoad
from views.entries import Entries

class Manager:
    def add_player():
        player_entries = Entries.get_player_entries()
        serialized_data = Player(player_entries[0], player_entries[1], player_entries[2]).serialize_player_data()
        SaveLoad.save(serialized_data, file_name="players_data")
        print("""    Player successfully added""")
        return
    
    def display_all_players():
        SaveLoad.load(file_name="players_data")    
        return
    

 



