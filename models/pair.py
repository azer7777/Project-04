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
    
    def get_score(player_1, player_2, score_1, score_2, winner_name=None):
        if player_1 == winner_name:
            score_1 += 1
        elif player_2 == winner_name:
            score_2 += 1
        else:
            score_1 += 0.5
            score_2 += 0.5
        return score_1, score_2
        

            
            
        