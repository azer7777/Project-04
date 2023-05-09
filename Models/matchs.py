class matchs:
    def __init__(self, player, score):
        self.player = player
        self.score = score
        self.list_player = []
        self.list_score = []
        
    def create_match(self): 
        self.match = (self.list_player, self.list_score)
        