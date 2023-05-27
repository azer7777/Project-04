import time

class Rounds:
    def __init__(self, current_round_nb, matchs_list):
        self.round_name = "Round" + " " + str(current_round_nb) + ":"
        self.current_round_nb = current_round_nb
        date_time =  time.strftime("%d %m %Y %H:%M")
        if self.current_round_nb == 1:
            self.start_date_time = date_time            
        elif self.current_round_nb == 4:
            self.end_date_time = date_time
        self.matchs_list = matchs_list
            
   
    def get_round_info_serialized(self):
        round_info_serialized = {
                                 "Round_name": self.round_name, 
                                 "Start_date_time": self.start_date_time, 
                                 "End_date_time": self.end_date_time, 
                                }
        return round_info_serialized
    


 
              