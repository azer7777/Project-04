import random

class Pair():
    def shuffle_tournament_players(tournament_players, current_round_nb):
        if current_round_nb == 1:
            tournament_players = random.shuffle(tournament_players)
        else:
            pass
        return tournament_players
    
    
    def get_pairs(tournament_players):

        return
    
    def get_score(current_round_nb, player_1, player_2, score_1, score_2, winner_name=""):
        if current_round_nb == 1:
            score_1 = 0
            score_2 = 0
        elif player_1 == winner_name:
            score_1 += 1
        elif player_2 == winner_name:
            score_2 += 1
        else:
            score_1 += 0.5
            score_2 += 0.5
        return score_1, score_2
        

            
            
        