a = [
    [
        [
            [
                "sdgrfgf",
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
                1
            ],
            [
                "grfgrf",
                0
            ]
        ],
        [
            [
                "iklki",
                0.5
            ],
            [
                "drgdg",
                0.5
            ]
        ],
        [
            [
                "efef",
                1
            ],
            [
                "gfhj",
                0
            ]
        ]
    ]
]


player_1_score = (((((a)[0])[0])[0])[1])

a.sort(key = lambda x: x[int(player_1_score)])

print(a)


