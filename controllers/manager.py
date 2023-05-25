import pandas
from models.player import Player
from models.save_load import SaveLoad
from views.entries import Entries
from models.tournament import Tournament
class Manager:
    def add_player():
        player_entries = Entries.get_player_entries()
        serialized_data = Player(player_entries[0], player_entries[1], player_entries[2]).serialize_player_data()
        SaveLoad.save(serialized_data, file_name="registred_players")
        print("""    Player successfully added""")
        return
    
    def display_all_players():
        SaveLoad.load(file_name="registred_players")    
        return
    
    def create_tournament():
        tournament_entries = Entries.get_tournament_entries()
        tournament__init__ = Tournament(tournament_entries[0], tournament_entries[1], tournament_entries[2], tournament_entries[3], tournament_entries[4], tournament_entries[5], tournament_entries[6], tournament_entries[7])
        tournament_info_serialized = tournament__init__.get_tournament_info_serialized()
        tournament_players_serialized = (tournament__init__.get_tournament_players_serialized())
        SaveLoad.save(tournament_info_serialized, file_name="tournaments_info")
        SaveLoad.save(tournament_players_serialized, file_name=("tournaments_players/" + tournament_entries[0]))
        print("""    Tournament successfully added""")
        return        
    
    def display_all_tournaments():
        SaveLoad.load(file_name="tournaments_info")
        return
    
    def select_a_tournament():
        Manager.display_all_tournaments()
        tournament_index = int(input("Select a tournament from  the above list by entring a matching number : "))
        selected_tournament = SaveLoad.load_only(file_name="tournaments_info")[tournament_index]
        print("""       
                       Selected tournament : 
                                                    """)
        print(pandas.DataFrame([selected_tournament]))
        filename = selected_tournament["Tournament_name"]
        return filename
    
    def display_tournament_players():
        SaveLoad.load()
        
 



