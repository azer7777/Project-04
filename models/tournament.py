
from models.save_load import SaveLoad
import random

class Tournament:
    def __init__(self, name, place, tournament_players_list, start_date, end_date, current_round_nb, rounds_list, description,nb_of_rounds=4):
        self.name = name
        self.place = place
        self.tournament_players_list = tournament_players_list
        self.star_date = start_date
        self.end_date = end_date
        self.current_round_nb = current_round_nb
        self.description = description
        self.nb_of_rounds = nb_of_rounds
        self.rounds_list = rounds_list
              
    def create_tournament_players_list():
        nb_of_players = int(input("""Enter the number of players (must be even) : """))
        while (nb_of_players % 2) != 0:
            print("Must be even !")
            print("Try again")
            nb_of_players = int(input("""Enter the number of players (must be even) : """))
        SaveLoad.load(file_name="players_data")
        tournament_players_list = []
        for loop in range(nb_of_players):
            selection_index = int(input("Select a player from  the above list by entring a matching number : "))
            user_selection = (SaveLoad.load_only(file_name="players_data"))[selection_index]
            tournament_players_list.append(user_selection)
                        
        return tournament_players_list
    
    def shuffle_tournament_players_randomly(self):
        shuffled_players_list = random.shuffle(self.tournament_players_list)
        return shuffled_players_list
        
    def get_tournament_info_serialized(self):
        tournament_info_serialized = {
                                         "Tournament_name": self.name, 
                                         "Place": self.place,
                                         "Nb_of_rounds": self.nb_of_rounds,
                                         "Current_round_nb": self.current_round_nb,
                                         "Rounds_list": self.rounds_list,
                                         "Description": self.description, 
                                         "Start_date": self.star_date,
                                         "End_date": self.end_date                                                                                   
                                     }    
        return tournament_info_serialized
    
    def get_tournament_players_serialized(self):
        tournament_players_serialized = self.tournament_players_list                                                                                 
    
        return tournament_players_serialized