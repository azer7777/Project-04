import pandas
import time
from models.player import Player
from models.save_load import SaveLoad
from views.entries import Entries
from models.tournament import Tournament
from models.rounds import Rounds
from models.matches import Matches

class Manager:
    def add_player():
        player_entries = Entries.get_player_entries()
        serialized_data = Player(player_entries[0], player_entries[1], player_entries[2]).serialize_player_data()
        SaveLoad.save(serialized_data, file_name="registred_players")
        print("""    Player successfully added""")
        return
    
    def display_all_players():
        SaveLoad.load(file_name="registred_players", title="regestred players")    
        return
    
    def create_tournament():
        tournament_entries = Entries.get_tournament_entries()
        tournament__init__ = Tournament(tournament_entries[0], tournament_entries[1], tournament_entries[2],
                                        tournament_entries[3], tournament_entries[4], tournament_entries[5],
                                        tournament_entries[6])
        tournament_info_serialized = tournament__init__.get_tournament_info_serialized()
        tournament_players_serialized = (tournament__init__.get_tournament_players_serialized())
        SaveLoad.save(tournament_info_serialized, file_name="tournaments_info")
        SaveLoad.save_tournament_players(tournament_players_serialized,
                                         file_name=("tournaments_players/" + tournament_entries[0]))
        print("""    Tournament successfully added""")
        return        
    
    def display_all_tournaments():
        SaveLoad.load(file_name="tournaments_info", title="tournaments")
        return
        
    def select_tournament(tournament_name):
        selection = SaveLoad.selected_archive("Tournament_name", tournament_name, file_name="tournaments_info")
        if selection == None:
            print("Invalid tournament name !")
            tournament_name = None
        else:
            print("""       
                           Selected tournament : 
                                                     """)
            print(pandas.DataFrame([selection]))
        return tournament_name
    
    def display_tournament_players(tournament_name):
        SaveLoad.load(file_name=("tournaments_players/" + tournament_name), title="tournament players")
        return
    
    def create_round(tournament_name):
        current_round_nb = ((Tournament.get_current_round_nb(tournament_name)) + 1)
        matches__init__ = Matches(tournament_name, current_round_nb)
        if current_round_nb == 1:
            match_list = matches__init__.initial_match_list()
        else:
            statute = Tournament.check_round_statute(tournament_name, (current_round_nb - 1))
            if statute == "In progress":
                print("You must end the round in progress ! ")
                return
            match_list = matches__init__.match_list(Matches.next_match_list)       
        rounds__init__ = Rounds(current_round_nb, match_list)
        round_maches_seiralized = rounds__init__.get_round_maches_serialized()
        round_info_serialized = rounds__init__.get_round_info_serialized()
        SaveLoad.save(round_maches_seiralized, file_name=("rounds_matches/" + tournament_name))
        SaveLoad.save(round_info_serialized, file_name=("rounds_info/" + tournament_name))
        tournament_changes = {'Current_round_nb': current_round_nb}
        SaveLoad.update("Tournament_name", tournament_name, tournament_changes, file_name="tournaments_info")
        print("""    Round {} successfully created
                        Tournament updated       """.format(current_round_nb))
        return       
        
    def end_round(tournament_name):
        current_round_nb = Tournament.get_current_round_nb(tournament_name)
        statute = Tournament.check_round_statute(tournament_name, current_round_nb)
        if statute != "In progress":
            print("No round in progress ! ")
            return
        index_round = (current_round_nb - 1)
        matches__init__ = Matches(tournament_name, current_round_nb)
        match_list = matches__init__.match_list(Matches.end_match_list)
        SaveLoad.update_round(match_list, index_round, file_name=("rounds_matches/" + tournament_name))
        end_date_time = time.strftime("%d %m %Y %H:%M")
        round_name = "Round" + " " + str(current_round_nb)
        round_changes = {"End_date_time": end_date_time}
        SaveLoad.update("Round_name", round_name, round_changes, file_name=("rounds_info/" + tournament_name)) 
        print("""    Round {} successfully terminated """.format(current_round_nb))    
        if current_round_nb == 4:
            end_time =  time.strftime("%d/%m/%Y")
            tournament_changes = {'End_date': end_time}
            SaveLoad.update("Tournament_name", tournament_name, tournament_changes, file_name="tournaments_info")
            print(""""    Tournament updated """)
        return    
        
    def display_rounds(tournament_name):
        SaveLoad.load(file_name=("rounds_info/" + tournament_name), title="Rounds")
        return
    
    def display_matches(tournament_name):
        round_nb = 1
        all_rounds = SaveLoad.load_only(file_name=("rounds_matches/" + "eeee"))
        if all_rounds == None:
            return
        for one_round in all_rounds:
            print()
            print("               Round" + " " + str(round_nb))
            print()
            print(pandas.DataFrame(one_round)) 
            round_nb += 1
        return

        
        
        
    

        
        
  
        
 



