import  random
class Pair:
    def shuffle_players(current_round_nb, players_list):
        if current_round_nb == 1:
            random.shuffle(players_list)
        else:
            pass
        return players_list
     
    def get_score(player_1, player_2, score_1, score_2, winner_name):
        if player_1 == winner_name:
            score_1 += 1
        elif player_2 == winner_name:
            score_2 += 1
        else:
            score_1 += 0.5
            score_2 += 0.5
        return player_1, player_2, score_1, score_2                  

    

            
        

    

    
