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
        tournament__init__ = Tournament(tournament_entries[0], tournament_entries[1], tournament_entries[2], tournament_entries[3], tournament_entries[4], tournament_entries[5], tournament_entries[6], tournament_entries[7])
        tournament_info_serialized = tournament__init__.get_tournament_info_serialized()
        tournament_players_serialized = tournament__init__.get_tournament_players_serialized()
        SaveLoad.save(tournament_info_serialized, file_name="tournament_info_data")
        SaveLoad.save(tournament_players_serialized, file_name="tournament_players_data")
        print("""    Toutnament successfully added""")
        return        
    
    def display_all_tournaments():
        SaveLoad.load_tournaments(file_name="tournament_info_data")
        return
 



