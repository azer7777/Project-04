import json

class Player:
    def __init__(self, family_name, first_name, date_of_birth):
        self.family_name = family_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.player_name = family_name + first_name
    
    def create_registred_players_list(self, registred_players_list):
        registred_players_list.append(self.player_name)
        return registred_players_list
    
    
        
    def load_player_to_json_file(self):
        player_info_serialized = [{"Family_name": self.family_name, 
                                 "First_name": self.first_name, 
                                 "Date_of_birth": self.date_of_birth}]
        filename = "players_data"
        with open(filename, 'w') as json_file:
            json.dump(player_info_serialized, json_file, 
                        indent=4,  
                        separators=(',',': '))
        return
            