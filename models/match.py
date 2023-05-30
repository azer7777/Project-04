
matches_list = []

class Matches:
    def __init__(self, player_1, player_2, score_1, score_2):
        self.player_01 = [player_1, score_1]
        self.player_02 = [player_2, score_2]
        self.match = (self.player_01, self.player_02)
        
    def create_match_list(self):
        matches_list.append(self.create_match)       
        return matches_list
               
                        

    

            
        

    

    
