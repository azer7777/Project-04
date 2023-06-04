import json
import random
from models.pair import Pair
from models.save_load import SaveLoad
from models.matches import Matches

u = [(["d", 10], ["z", 22]), (["j", 55], ["l", 33])]




def match_list(function):
        all_rounds_matches = SaveLoad.load_only(file_name=("rounds_matches/" + "dddd"))
        index_round = 0
        index_match = 0
        index_player_1 = 0
        index_player_2 = 1
        index_player_name = 0
        index_player_score = 1
        rounda = ((all_rounds_matches)[index_round])      
        round_matches = (len(all_rounds_matches[index_round]))
        list = []
        for i in range(round_matches):            
            match = (rounda[index_match])        
            player_1_name = ((match[index_player_1])[index_player_name])
            player_2_name = ((match[index_player_2])[index_player_name])
            player_1_score = ((match[index_player_1])[index_player_score])
            player_2_score = ((match[index_player_2])[index_player_score])
            match_list = function(list, player_1_name, player_2_name, player_1_score, player_2_score, round_matches , index_match, match)
            index_match += 1
        return match_list

def next_match(list, player_1_name, player_2_name, player_1_score, player_2_score, round_matches, index_match, match):
        player_01 = [player_1_name, player_1_score]
        player_02 = [player_2_name, player_2_score]
        list.append(player_01)
        list.append(player_02)
        if round_matches > (index_match):
            list.sort(key = lambda x: x[1], reverse=True)
            match_list = []
            index_1 = 0
            index_2 = 1
            for i in range(int(len(list) / 2)):
                create_match = create_next_match(list[index_1], list[index_2])
                match_list.append(create_match)                           
                index_1 += 2
                index_2 += 2
            list = match_list
        return list

def create_next_match(player_1, player_2):
        match = (player_1, player_2)
        return match

def end_match_list(list, player_1_name, player_2_name, player_1_score, player_2_score, round_matches , index_match, match):
        print(match)           
        winner_name = ""
        player_score = Pair.get_score(player_1_name, player_2_name, player_1_score, player_2_score, winner_name)
        create_match = Matches.create_match(player_score[0], player_score[1], player_score[2], player_score[3])
        list.append(create_match)
        return list


   
m = match_list(next_match)

print(m)