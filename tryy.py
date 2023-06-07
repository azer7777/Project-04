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
]
e = [['efef', 3], ['iklki', 3], ['sdgrfgf', 0], ['drgdg', 1], ['grfgrf', 0.5], ['sdgsthg', 0.5], ['dht', 0], ['gfhj', 1]]
def get_next_pair(list):
    new_list = list.copy()
    new_list.sort(key = lambda x: x[1], reverse=True)
    index_1 = 0
    index_2 = 1
    for i in range((int(len(new_list) / 2) - 1)):
        if new_list[index_1] == list[index_1] and new_list[index_2] == list[index_2]:
            new_list[index_2], new_list[index_2 + 1] = new_list[index_2 + 1], new_list[index_2]
        index_1 += 2
        index_2 += 2   
    return new_list, list
        
    

t = get_next_pair(e)

print(t[0])