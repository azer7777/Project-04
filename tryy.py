import pandas

class Matches:
    def __init__(self, player_1, player_2, score_1, score_2):
        self.player_01 = [player_1, score_1]
        self.player_02 = [player_2, score_2]
        self.match = (self.player_01, self.player_02)
        
    def create_matches_list(self, matches_list):
        matches_list.append(self.match)
        return matches_list 





t =  [ 
       { "player 1": ["player_1", 1],
         "player 2": ["player_2", 2]
        
       }
    ]
        
round_name = "round_name" + "           "
player_01 = ["player_1", 2]
player_02 = ["player_2", 0]
match = (player_01, player_02)

roundi = [{round_name: [match]}]


print(pandas.DataFrame(roundi))


