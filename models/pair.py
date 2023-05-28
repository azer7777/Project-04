import random

class Pair():
    def shuffle_tournament_players_randomly(self):
        shuffled_players_list = random.shuffle(self.tournament_players_list)
        return shuffled_players_list
    
    def get_pairs(current_round_nb):
        if current_round_nb == 1:
            Pair.shuffle_tournament_players_randomly()
        else:
            pass
        return