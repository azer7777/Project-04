import json
from models.rounds import Rounds
from models.save_load import SaveLoad
from models.tournament import Tournament
u = [(["d", 10], ["z", 22]), (["j", 55], ["l", 33])]




def update(selected_element):
    with open("database/" + "tournaments_info") as fp:
        data_list = json.load(fp)
    selection_index = data_list.index(selected_element)
    data_list[selection_index].update({'Current_round_nb': 79})    
    with open("database/" + "tournaments_info", 'w') as json_file:
        json.dump(data_list, json_file,
                      indent=4,
                      separators=(',',': '))

def get_current_round_nb(tournament_name):
    selected_tournament = SaveLoad.selected_archive("Tournament_name", tournament_name, file_name="tournaments_info")
    current_round_nb = selected_tournament['Current_round_nb']
    return current_round_nb

def get_players_list():
        players_list = []
        players_data = SaveLoad.load_only(file_name=("tournaments_players/" + "dddd"))
        index = 0
        for loop in players_data:
            player_name = (list(map((players_data[index]).get, ['Family_name'])))[0]
            players_list.append(player_name)
            index += 1
        return players_list
    
e = get_players_list()

print(e)