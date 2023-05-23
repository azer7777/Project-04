import random
import datetime
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
    
    def check_date_format():
        date = input("""Enter date of birth (format "DD/MM/YYYY") :""")
        while True:
            try:
                date == (datetime.datetime.strptime(date, "%d/%m/%Y")).date()
                break 
            except(ValueError):           
                print("Inccorect date format !")
                print("Try again")
                date = input("""Enter date (format "DD/MM/YYYY") :""")
        return date       
 
   
    def create_tournament_players_list(user_players_selection):
        tournament_players_list = []
        tournament_players_list.append(user_players_selection)
        return tournament_players_list
    
    def shuffle_tournament_players_randomly(self):
        shuffled_players_list = random.shuffle(self.tournament_players_list)
        return shuffled_players_list
        
    def get_tournament_info_serialized(self):
        tournament_info_serialized = {
                                         "Name": self.name, 
                                         "Place": self.place,
                                         "Tournament_players_list": self.tournament_players_list,
                                         "Nb_of_rounds": self.nb_of_rounds,
                                         "Current_round_nb": self.current_round_nb,
                                         "Rounds_list": self.rounds_list,
                                         "Description": self.description, 
                                         "Start_date": self.star_date,
                                         "End_date": self.end_date                                                                                   
                                     }    
        return tournament_info_serialized