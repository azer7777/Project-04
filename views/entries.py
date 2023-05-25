
from models.tournament import Tournament
from models.save_load import SaveLoad
import datetime
class Entries:
    def get_player_entries():
        family_name = input("""Enter family name :""")
        first_name = input("""Enter first name :""") 
        date_of_birth = Entries.check_date_format("date_of_birth")                
        return (family_name, first_name, date_of_birth)
    
    def get_tournament_entries():
        name = input("Enter tournament name :")
        place = input("Enter tournament place :")
        tournament_players_list = Tournament.create_tournament_players_list()
        current_round_nb = int(input("Enter current round number :"))
        round_list = "to do"
        description = input("Enter description :")
        start_date = Entries.check_date_format("tournament start date")        
        end_date = Entries.check_date_format("tournament end date or press Enter if in progress")                
        return (name, place, tournament_players_list, start_date, end_date, current_round_nb, round_list, description)
    
    def check_date_format(subject):
        date = input(("""Enter {} (format "DD/MM/YYYY") :""").format(subject))        
        if date != "":
            while True:
                try:
                    date == (datetime.datetime.strptime(date, "%d/%m/%Y")).date()
                    break 
                except(ValueError):           
                    print("Inccorect date format !")
                    print("Try again")
                    date = input(("""Enter {} (format "DD/MM/YYYY") :""").format(subject))
        return date
    
    def get_selected_tournament_name():
        tournament_name = input("Select a tournament by entering its name :")
        return tournament_name
    






