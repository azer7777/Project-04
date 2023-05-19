class Entries:
    def get_player_entries():
        family_name = input("""Enter family name :""")
        first_name = input("""Enter first name :""")
        date_of_birth = input("""Enter date of birth :""") 
        return family_name,first_name,date_of_birth
    
    def get_tournament_entries():
        name = input("Enter tournament name :")
        place = input("Enter tournament place :")
        start_date = input("Enter tournament start date :")
        end_date = input("Enter tournament end date (if in progress press Entrer) :")
        current_round_nb = int(input("Enter current round number :"))
        registred_players_list = input("Enter registred players family name and firs name :")
        description = input("Enter description :")
        return name, place, start_date, end_date, current_round_nb, registred_players_list, description




