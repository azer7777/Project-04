class Matchs:
    def __init__(self, player_1, player_2, score_1, score_2):
        self.player_01 = [player_1, score_1]
        self.player_02 = [player_2, score_2]
        self.match = (self.player_01, self.player_02)
        
    def create_matchs_list(self, matchs_list):
        matchs_list.append(self.match)
        return matchs_list        
                        
    def get_match_info_serialized(self):
        match_info_serialized = {"Match": self.match}
        return match_info_serialized
    

            
        

    

    
