import pandas
from models.save_load import SaveLoad
from models.tournament import Tournament

a = [
    [
        [
            [
                "sdgsthg",
                0
            ],
            [
                "dht",
                0
            ]
        ],
        [
            [
                "efef",
                0
            ],
            [
                "iklki",
                0
            ]
        ],
        [
            [
                "gfhj",
                0
            ],
            [
                "grfgrf",
                0
            ]
        ],
        [
            [
                "drgdg",
                0
            ],
            [
                "sdgrfgf",
                0
            ]
        ]
    ]
]



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
            index_match += 1
        return match_list, index_round
    
    
    
def next_match_list(self):
        print(pandas.DataFrame(match))           
        winner_name = Entries.get_winner_name()
        player_score = Pair.get_score(player_1_name, player_2_name, player_1_score, player_2_score, winner_name)
        create_matchi = Matches.create_match(player_score[0], player_score[1], player_score[2], player_score[3])
        match_list.append(create_matchi)
        