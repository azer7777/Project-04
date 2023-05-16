class Player:
    def __init__(self, family_name, first_name, date_of_birth):
        self.family_name = family_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.player_name = family_name + first_name
    
    def create_registred_players_list(self, registred_players_list):
        registred_players_list.append(self.player_name)
        return registred_players_list
    
    
        
    def get_player_info_serialized(self):
        player_info_serialized = {"Family_name": self.family_name, 
                                 "First_name": self.first_name, 
                                 "Date_of_birth": self.date_of_birth}
        return player_info_serialized
            