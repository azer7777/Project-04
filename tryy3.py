import json
import random
from models.pair import Pair
from models.save_load import SaveLoad
from models.matches import Matches

u = [(["d", 10], ["z", 22]), (["j", 55], ["l", 33])]




def end_match_list():
        all_rounds_matches = SaveLoad.load_only(file_name=("rounds_matches/" + "dddd"))
        index_round = 0
        index_match = 0
        index_player_1 = 0
        index_player_2 = 1
        index_player_name = 0
        index_player_score = 1
        rounda = ((all_rounds_matches)[index_round])      
        round_matches = (len(all_rounds_matches[index_round]))
        match_list = []
        for i in range(round_matches):            
            match = (rounda[index_match])        
            player_1_name = ((match[index_player_1])[index_player_name])
            player_2_name = ((match[index_player_2])[index_player_name])
            player_1_score = ((match[index_player_1])[index_player_score])
            player_2_score = ((match[index_player_2])[index_player_score])
            player_01 = [player_1_name, player_1_score]
            player_02 = [player_2_name, player_2_score]
            match_list.append(player_01)
            match_list.append(player_02)
            index_match += 1
        return match_list
    
u = end_match_list()

u.sort(key = lambda x: x[1], reverse=True)
print(u)