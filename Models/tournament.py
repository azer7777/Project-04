import random
class Tournament:
    def __init__(self, name, place, start_end_date, current_round_nb, registred_players_list, rounds_list, description,nb_of_rounds=4):
        self.name = name
        self.place = place
        self.star_end_date = start_end_date
        self.current_round_nb = current_round_nb
        self.description = description
        self.nb_of_rounds = nb_of_rounds
        self.rounds_list = rounds_list
        self.registred_players_list = registred_players_list
    
    def shuffle_tournament_players_randomly(self):
        shuffled_players_list = random.shuffle(self.registred_players_list)
        return shuffled_players_list
    
    
        
    def get_tournament_info_serialized(self):
        tournament_info_serialized = {"Name": self.name, 
                                      "Place": self.place, 
                                      "Start_end_date": self.star_end_date, 
                                      "Current_round_nb": self.current_round_nb, 
                                      "Rounds_list": self.rounds_list, 
                                      "Registred_players_list": self.registred_players_list, 
                                      "Description": self.description, 
                                      "Nb_of_rounds": self.nb_of_rounds}    
        return tournament_info_serialized