

class Rounds:
    def __init__(self, start_date_time, end_date_time, current_round_nb, matchs_list):
        self.round_name = "Round" + " " + str(current_round_nb) + ":"
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time
        self.matchs_list = matchs_list    
    
    def get_round_info_serialized(self):
        round_info_serialized = {"Round_name": self.round_name, 
                                 "Start_date_time": self.start_date_time, 
                                 "End_date_time": self.end_date_time, 
                                 "Matchs_list": self.matchs_list}
        return round_info_serialized
    
    def create_round_list(self, rounds_list):
        rounds_list.append(self.round_name)
        rounds_list.append(self.matchs_list)
        return rounds_list


 
              