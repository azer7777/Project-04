import pandas
from models.save_load import SaveLoad
from models.tournament import Tournament

a = [
    [
        [
            [
                "dht",
                0
            ],
            [
                "drgdg",
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
        ],
        [
            [
                "sdgrfgf",
                0
            ],
            [
                "gfhj",
                0
            ]
        ]
    ],
    [
        [
            [
                "sdgrfgf",
                0
            ],
            [
                "gfhj",
                0
            ]
        ],
        [
            [
                "gfhj",
                0
            ],
            [
                "dht",
                0
            ]
        ],
        [
            [
                "dht",
                0
            ],
            [
                "drgdg",
                0
            ]
        ]
    ]
]



    


index_round = 0
index_match = 0
index_player = 0
index_name_score = 0


player_1 = (((a[index_round])[index_match])[index_player])
player_2 = (((a[0])[0])[1])
score_1 = ((((a[index_round])[index_match])[index_player])[index_name_score])
score_2 = (((a[0])[0])[0])

match_1 = ((a[index_round])[index_match])
round_1 = (a[index_round])




def get_current_round_nb(tournament_name):
    selected_tournament = Tournament.selected_tournament(tournament_name)
    current_round_nb = selected_tournament['Current_round_nb']
    return current_round_nb