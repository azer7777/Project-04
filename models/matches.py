import pandas
from models.save_load import SaveLoad
from models.pair import Pair
from views.entries import Entries

class Matches():
    def __init__(self, tournament_name, current_round_nb):
        self.tournament_name = tournament_name
        self.current_round_nb = current_round_nb
       
    def create_match(player_1_name, player_2_name, player_1_score, player_2_score):
        player_01 = [player_1_name, player_1_score]
        player_02 = [player_2_name, player_2_score]
        match = (player_01, player_02)
        return match
    
    def create_next_match(player_1, player_2):
        match = (player_1, player_2)
        return match
                    
    def initial_match_list(self):
        players_list = Pair.shuffled_player_list(self.tournament_name)
        index_1 = 0
        index_2 = 1
        matches_list = []
        for i in range(int(len(players_list) / 2)):
            create_match= Matches.create_match(players_list[index_1], players_list[index_2], score_1=0, score_2=0)
            matches_list.append(create_match)                           
            index_1 += 2
            index_2 += 2
        return matches_list

    def match_list(self):
        all_rounds_matches = SaveLoad.load_only(file_name=("rounds_matches/" + self.tournament_name))
        index_round = (self.current_round_nb) - 1
        index_match = 0
        index_player_1 = 0
        index_player_2 = 1
        index_player_name = 0
        index_player_score = 1
        one_round = ((all_rounds_matches)[index_round])      
        nb_of_matches = (len(all_rounds_matches[index_round]))
        match_list = []
        for i in range(nb_of_matches):
            match = (one_round[index_match])        
            player_1_name = ((match[index_player_1])[index_player_name])
            player_2_name = ((match[index_player_2])[index_player_name])
            player_1_score = ((match[index_player_1])[index_player_score])
            player_2_score = ((match[index_player_2])[index_player_score])
            print(pandas.DataFrame(match))           
            winner_name = Entries.get_winner_name()
            player_score = Pair.get_score(player_1_name, player_2_name, player_1_score, player_2_score, winner_name)
            create_matchi = Matches.create_match(player_score[0], player_score[1], player_score[2], player_score[3])
            match_list.append(create_matchi)
            index_match += 1
        return match_list, index_round
    
    
    
    def next_match_list(self):
        pass
       
    def get_match_list(self):
        if self.current_round_nb == 1:
            match_list = Matches.initial_match_list(self)
        else:
            pass                
        return match_list


               
            
        