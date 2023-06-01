import json
from models.rounds import Rounds
from models.save_load import SaveLoad
from models.tournament import Tournament
u = [(["d", 10], ["z", 22]), (["j", 55], ["l", 33])]

selected_tournament = (Tournament.selected_tournament("zzzz"))


def update(selected_element):
    with open("database/" + "tournaments_info") as fp:
        data_list = json.load(fp)
    selection_index = data_list.index(selected_element)
    data_list[selection_index].update({'Current_round_nb': 79})    
    with open("database/" + "tournaments_info", 'w') as json_file:
        json.dump(data_list, json_file,
                      indent=4,
                      separators=(',',': '))


# 1