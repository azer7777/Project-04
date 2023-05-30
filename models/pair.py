import random
from models.save_load import SaveLoad
class Pair():
    
    def load_tournament_players(tournament_name):
        players_list = []
        players_data = SaveLoad.load_only(file_name=("tournaments_players/" + tournament_name))
        index = 0
        for loop in players_data:
            player_name = (list(map((players_data[index]).get, ['Family_name'])))[0]
            players_list.append(player_name)
        index += 1
        return players_list
    
    def shuffle_tournament_players(players_list, current_round_nb):
        if current_round_nb == 1:
            random.shuffle(players_list)
        else:
            pass
        return players_list
     
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
        
    def get_pairs(tournament_name, current_round_nb):
        players_list = Pair.load_tournament_players(tournament_name)
        Pair.shuffle_tournament_players(players_list, current_round_nb)
        index_1 = 0
        index_2 = 1
        for loop in range(int(len(players_list) / 2)):
            for loop in range(2):
                Pair.get_score(current_round_nb, players_list[index_1], players_list[index_2], score_1, score_2, winner_name="")

            
            
        