from models.player import Player
from models.save_load import SaveLoad
from views.entries import Entries
from models.tournament import Tournament
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
    
    def create_tournament():
        tournament_entries = Entries.get_tournament_entries()
        serialized_data = Tournament(tournament_entries[0], tournament_entries[1], tournament_entries[2], tournament_entries[3], tournament_entries[4], tournament_entries[5], tournament_entries[6]).get_tournament_info_serialized()
        SaveLoad.save(serialized_data, file_name="tournament_data")
        print("""    Toutnament successfully added""")
        return        

 



