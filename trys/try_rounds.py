

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



print("Enter player 1 score:")
score_1 = int(input())
print("Enter player 2 score:")
score_2 = int(input())
matchs_list = []
matcho = match.Matches("player_1", "player_2", score_1, score_2)
matcho_list = matcho.create_matchs_list(matchs_list)
rounds_list = []
current_round_nb = 1
roundi = Rounds("start_date_time", "end_date_time", current_round_nb, matcho_list)
rounda = roundi.create_round_list(rounds_list = [])

for i in rounda:
    print(i)