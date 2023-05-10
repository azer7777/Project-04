class matchs:
    def __init__(self, player, score):
        self.player = player
        self.score = score
        self.list_player = []
        self.list_score = []
        
    
    def save_match_info_serialized(self):
        match_info_serialized = {"match": (self.list_player, self.score)}
        return match_info_serialized