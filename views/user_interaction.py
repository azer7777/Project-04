class UserInteractions:
    def get_player_entries():
        print("Enter family name :")
        family_name = input()
        print("Enter first name :")
        first_name = input()
        print("Enter date of birth :")
        date_of_birth = input() 
        return family_name,first_name,date_of_birth
    
    def get_tournament_entries():
        print("Enter tournament name :")
        name = input()
        print("Enter tournament place :")
        place = input()
        print("Enter tournament start date :")
        start_date = input()
        print("Enter tournament end date (if in progress press Entrer) :")
        end_date = input()
        print("Enter current round number :")
        current_round_nb = input()
        print("Enter registred players family name and firs name :")
        registred_players_list = input()
        print("Enter description :")
        description = input()
        return name,place,start_date, end_date, current_round_nb,registred_players_list,description


a = UserInteractions.get_tournament_entries()

