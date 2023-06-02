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



def hend_match_list():
        rounds_matches = a
        index_round = 0
        index_match = 0
        index_player_1 = 0
        index_player_2 = 1
        index_player_name = 0
        index_player_score = 1
        rounda = ((rounds_matches)[index_round])
        match = (rounda[index_match])        
       
        round_matches = (len(rounds_matches[index_round]))

        for loop in range(round_matches):
            print(pandas.DataFrame(rounda[index_match]))            
            winner_name = input()
            index_match += 1
        return

hend_match_list()     