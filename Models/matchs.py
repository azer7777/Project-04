#    02

class Matchs:
    def __init__(self, player_1, player_2, score_1, score_2):
        self.player_01 = [player_1, score_1]
        self.player_02 = [player_2, score_2]
         
    def create_match(self):
        self.match = (self.player_01, self.player_02)
        return self.match
                
    def get_match_info_serialized(self):
        match_info_serialized = {"Match": self.match}
        return match_info_serialized