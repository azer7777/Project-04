import json


class Player:
    def __init__(self, family_name, first_name, date_of_birth):
        self.family_name = family_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        
    def get_player_info_serialized(self):
        player_info_serialized = [{"Family_name": family_name,
                                  "First_name": first_name,
                                  "Date_of_birth": date_of_birth}]
        
        return player_info_serialized


family_name = "dzeede"
first_name = "dfgdfg"
date_of_birth = "zaah"


matchi = Player(family_name, first_name, date_of_birth)
matcho = matchi.get_player_info_serialized()


filename = "data_players"
with open(filename, 'w') as json_file:
    json.dump(matcho, json_file, 
                        indent=4,  
                        separators=(',',': '))