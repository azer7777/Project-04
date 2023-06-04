import time

class Rounds:
    def __init__(self, current_round_nb, match_list):
        self.round_name = "Round" + " " + str(current_round_nb)
        self.current_round_nb = current_round_nb
        date_time = time.strftime("%d %m %Y %H:%M")
        self.start_date_time = date_time
        self.end_date_time = "In progress"            
        self.match_list = match_list
    
    def get_round_maches_serialized(self):
        round_serialized = self.match_list
        return round_serialized
               
    def get_round_info_serialized(self):
        round_info_serialized = {
                                 "Round_name": self.round_name, 
                                 "Start_date_time": self.start_date_time, 
                                 "End_date_time": self.end_date_time, 
                                }
        return round_info_serialized
    


 
              