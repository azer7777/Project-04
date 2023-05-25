import pandas

a = [
    {
        "Tournament_name": "sthtrh",
        "Place": "htrhth",
        "Nb_of_rounds": 4,
        "Current_round_nb": 1,
        "Rounds_list": "to do",
        "Description": "rhtrhtrh",
        "Start_date": "02/02/2004",
        "End_date": ""
    },
    {
        "Tournament_name": "sthsfh",
        "Place": "fshftgh",
        "Nb_of_rounds": 4,
        "Current_round_nb": 1,
        "Rounds_list": "to do",
        "Description": "shthh",
        "Start_date": "02/02/01",
        "End_date": ""
    },
    {
        "Tournament_name": "drgdrg",
        "Place": "dgg",
        "Nb_of_rounds": 4,
        "Current_round_nb": 1,
        "Rounds_list": "to do",
        "Description": "drg",
        "Start_date": "02/02/2001",
        "End_date": "04/01/2003"
    },
    {
        "Tournament_name": "thtrhrfth",
        "Place": "fdhggfh",
        "Nb_of_rounds": 4,
        "Current_round_nb": 1,
        "Rounds_list": "to do",
        "Description": "fbgtgh",
        "Start_date": "02/04/2007",
        "End_date": ""
    }
]
    
name = "thtrhrfth"
res = next((sub for sub in a if sub['Tournament_name'] == name), None)
print(pandas.DataFrame([res]))


