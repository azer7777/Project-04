class Rounds:
    def __init__(self, start_date_time, end_date_time, current_round_nb, matchs_list):
        self.round_name = "Round"+ current_round_nb
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time
        self.matchs_list = matchs_list    
    
    def get_round_info_serialized(self):
        round_info_serialized = {"Round_name": self.round_name, 
                                 "Start_date_time": self.start_date_time, 
                                 "End_date_time": self.end_date_time, 
                                 "Matchs_list": self.matchs_list}
        return round_info_serialized
    
    # choose players randomly             