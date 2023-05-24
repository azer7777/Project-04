import pandas

a = [
    {
        "Family_name": "sdgrfgf",
        "First_name": "dgrdg",
        "Date_of_birth": "12/08/2008"
    },
    {
        "Family_name": "dht",
        "First_name": "fthj",
        "Date_of_birth": "02/02/2004"
    }
]
    

if "Family_" in pandas.DataFrame(a):
    print(pandas.DataFrame(a).sort_values("Family_name"))
else:
    print(pandas.DataFrame(a))


