import random
from models.save_load import SaveLoad


class Pair:
    def shuffled_player_list(tournament_name):
        players_list = []
        players_data = SaveLoad.load_only(file_name=("tournaments_players/" + tournament_name))
        index = 0
        for i in players_data:
            player_name = (list(map((players_data[index]).get, ["Family_name"])))[0]
            players_list.append(player_name)
            index += 1
        random.shuffle(players_list)
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

    def get_next_ranking(list):
        new_list = list.copy()
        new_list.sort(key=lambda x: x[1], reverse=True)
        index_1 = 0
        index_2 = 1
        for i in range((int(len(new_list) / 2) - 1)):
            if new_list[index_1] == list[index_1] and new_list[index_2] == list[index_2]:
                new_list[index_2], new_list[index_2 + 1] = new_list[index_2 + 1], new_list[index_2]
            index_1 += 2
            index_2 += 2
        return new_list
