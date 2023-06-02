import pandas
import random
from models.save_load import SaveLoad
from models.match import Matches
from views.entries import Entries

class Pair():
    def __init__(self, tournament_name, current_round_nb):
        self.tournament_name = tournament_name
        self.current_round_nb = current_round_nb
        
    def get_players_list(self):
        players_list = []
        players_data = SaveLoad.load_only(file_name=("tournaments_players/" + self.tournament_name))
        index = 0
        for loop in players_data:
            player_name = (list(map((players_data[index]).get, ['Family_name'])))[0]
            players_list.append(player_name)
            index += 1
        return players_list
    
    
    def initial_match_list(self):
        players_list = Pair.get_players_list(self)
        Pair.shuffle_players(self, players_list)
        index_1 = 0
        index_2 = 1
        for loop in range(int(len(players_list) / 2)):
            matches__init__ = Matches(players_list[index_1], players_list[index_2], score_1=0, score_2=0)
            match_list = matches__init__.create_match_list()                           
            index_1 += 1
            index_2 += 1
        return match_list


    def result_match_list(self):
        rounds_matches = SaveLoad.load_only(file_name=("rounds_matches/" + self.tournament_name))
        index_round = (self.current_round_nb) - 1
        index_match = 0
        index_player_1 = 0
        index_player_2 = 1
        index_player_name = 0
        index_player_score = 1
        rounda = ((round_matches)[index_round])
        match = (rounda[index_match])        
        player_1_name = ((match[index_player_1])[index_player_name])
        player_2_name = ((match[index_player_2])[index_player_name])
        player_1_score = ((match[index_player_1])[index_player_score])
        player_2_score = ((match[index_player_2])[index_player_score])       
        round_matches = (len(rounds_matches[index_round]))
        for loop in range(round_matches):
            print(pandas.DataFrame(match))
            index_match += 1
            winner_name = Entries.get_winner_name()
            player_score = Pair.get_score(player_1_name, player_2_name, player_1_score, player_2_score, winner_name)
            matches__init__ = Matches(player_score[0], player_score[1], player_score[2], player_score[3])
            match_list = matches__init__.create_match_list()
        return match_list, index_round
    
    def next_match_list(self):
        pass

    
    
    
    
    def shuffle_players(self, players_list):
        if self.current_round_nb == 1:
            random.shuffle(players_list)
        else:
            pass
        return players_list
     
    def get_score(self, player_1, player_2, score_1, score_2, winner_name):
        if player_1 == winner_name:
            score_1 += 1
        elif player_2 == winner_name:
            score_2 += 1
        else:
            score_1 += 0.5
            score_2 += 0.5
        return player_1, player_2, score_1, score_2
      
        
    def get_match_list(self):
        if self.current_round_nb == 0:
            match_list = Pair.initial_match_list(self)
        else:
            pass                
        return match_list


               
            
        