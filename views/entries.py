
from models.tournament import Tournament
from models.save_load import SaveLoad
class Entries:
    def get_player_entries():
        family_name = input("""Enter family name :""")
        first_name = input("""Enter first name :""") 
        date_of_birth = Tournament.check_date_format()                
        return (family_name, first_name, date_of_birth)
    
    def get_tournament_entries():
        name = input("Enter tournament name :")
        place = input("Enter tournament place :")
        nb_of_players = int(input("""Enter the number of players (must be even) : """))
        Manager.display_all_players()
        tournament_players_list = []
        for loop in range(nb_of_players):
            selection_index = input("Select a player from  the above list by entring a matching number : ")
            user_selection = SaveLoad.load_only(file_name="players_data")[selection_index]
            tournament_players_list.append(user_selection)
            return tournament_players_list
        current_round_nb = int(input("Enter current round number :"))
        description = input("Enter description :")
        start_date = input("Enter tournament start date :")
        end_date = input("Enter tournament end date (if in progress press Entrer) :")        
        return (name, place, start_date, end_date, current_round_nb, tournament_players_list, description)




