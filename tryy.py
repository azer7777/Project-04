import pandas
from models.save_load import SaveLoad


a = [
    [
        [
            [
                "efef",
                1
            ],
            [
                "iklki",
                0
            ]
        ],
        [
            [
                "sdgrfgf",
                0
            ],
            [
                "drgdg",
                1
            ]
        ],
        [
            [
                "grfgrf",
                0.5
            ],
            [
                "sdgsthg",
                0.5
            ]
        ],
        [
            [
                "dht",
                0
            ],
            [
                "gfhj",
                1
            ]
        ]
    ],
    [
        [
            [
                "efef",
                2
            ],
            [
                "drgdg",
                1
            ]
        ],
        [
            [
                "gfhj",
                1.5
            ],
            [
                "grfgrf",
                1.0
            ]
        ],
        [
            [
                "sdgsthg",
                1.0
            ],
            [
                "iklki",
                0.5
            ]
        ],
        [
            [
                "sdgrfgf",
                0.5
            ],
            [
                "dht",
                0.5
            ]
        ]
    ],
    [
        [
            [
                "efef",
                2.5
            ],
            [
                "gfhj",
                2.0
            ]
        ],
        [
            [
                "drgdg",
                1.5
            ],
            [
                "grfgrf",
                1.5
            ]
        ],
        [
            [
                "sdgsthg",
                1.5
            ],
            [
                "iklki",
                1.0
            ]
        ],
        [
            [
                "sdgrfgf",
                1.0
            ],
            [
                "dht",
                1.0
            ]
        ]
    ],
    [
        [
            [
                "efef",
                3.5
            ],
            [
                "gfhj",
                3.0
            ]
        ],
        [
            [
                "drgdg",
                2.5
            ],
            [
                "grfgrf",
                2.5
            ]
        ],
        [
            [
                "sdgsthg",
                2.5
            ],
            [
                "iklki",
                2.0
            ]
        ],
        [
            [
                "sdgrfgf",
                2.0
            ],
            [
                "dht",
                2.0
            ]
        ]
    ]
]

def get_chess_national_id():
    two_letters = input("Enter chess national id first two letters : ")
    five_numbers = input("Enter chess national id five last numbers : ")
    while (len(two_letters) != 2 and two_letters is not str and
           len(five_numbers) != 5 and two_letters is not int) :
        print("Invalid ID")
        print("Try again")
        two_letters = input("Enter chess national id first two letters : ")
        five_numbers = input("Enter chess national id five last numbers : ")
    chess_national_id = (two_letters).upper() + str(five_numbers)
    return chess_national_id
    
r  = get_chess_national_id()

print(r)