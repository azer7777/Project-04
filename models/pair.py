import random
from models.save_load import SaveLoad
from models.match import Matches

class Pair():
    def __init__(self, tournament_name, current_round_nb, score_1, score_2, winner_name):
        self.tournament_name = tournament_name
        self.current_round_nb = current_round_nb
        self.score_1 = score_1
        self.score_2 = score_2
        self.winner_name = winner_name
        
    def get_players_list(self):
        players_list = []
        players_data = SaveLoad.load_only(file_name=("tournaments_players/" + self.tournament_name))
        index = 0
        for loop in players_data:
            player_name = (list(map((players_data[index]).get, ['Family_name'])))[0]
            players_list.append(player_name)
        index += 1
        return players_list
    
    def shuffle_players(self, players_list):
        if self.current_round_nb == 1:
            random.shuffle(players_list)
        else:
            pass
        return players_list
     
    def get_score(self, player_1, player_2):
        if self.current_round_nb == 1:
            self.score_1 = 0
            self.score_2 = 0
        elif player_1 == self.winner_name:
            self.score_1 += 1
        elif player_2 == self.winner_name:
            self.score_2 += 1
        else:
            self.score_1 += 0.5
            self.score_2 += 0.5
        return player_1, player_2, self.score_1, self.score_2
        
    def get_match_list(self):
        players_list = Pair.get_players_list(self)
        Pair.shuffle_players(self, players_list)
        index_1 = 0
        index_2 = 1
        for loop in range(int(len(players_list) / 2)):
                pair = Pair.get_score(self, players_list[index_1], players_list[index_2])
                matches__init__ = Matches(pair[0], pair[1], pair[2], pair[3])
                match_list = matches__init__.create_match_list()
                index_1 += 1
                index_2 += 1
        return match_list

            
            
        