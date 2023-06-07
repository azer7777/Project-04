import datetime
from models.tournament import Tournament


class Entries:
    def get_player_entries():
        print()
        family_name = input("""    Enter family name : """)
        first_name = input("""    Enter first name :""")
        date_of_birth = Entries.check_date_format("date_of_birth")
        chess_national_id = Entries.get_chess_national_id()
        return (family_name, first_name, date_of_birth, chess_national_id)

    def get_tournament_entries():
        print()
        name = input("""    Enter tournament name :""")
        place = input("""    Enter tournament place :""")
        tournament_players_list = Tournament.create_tournament_players_list()
        current_round_nb = 0
        description = input("""    Enter description :""")
        start_date = Entries.check_date_format("tournament start date")
        end_date = "In progress"
        return (name, place, tournament_players_list, start_date, end_date, current_round_nb, description)

    def get_chess_national_id():
        two_letters = input("Enter chess national id first two letters : ")
        five_numbers = input("Enter chess national id five last numbers : ")
        while (
            (len(two_letters) != 2)
            and (two_letters is not str)
            or (len(five_numbers) != 5)
            and (five_numbers is not int)
        ):
            print("Invalid ID")
            print("Try again")
            two_letters = input("Enter chess national id first two letters : ")
            five_numbers = input("Enter chess national id five last numbers : ")
        chess_national_id = (two_letters).upper() + str(five_numbers)
        return chess_national_id

    def check_date_format(subject):
        date = input(("""    Enter {} (format "DD/MM/YYYY") : """).format(subject))
        if date != "":
            while True:
                try:
                    date == (datetime.datetime.strptime(date, "%d/%m/%Y")).date()
                    break
                except ValueError:
                    print("    Inccorect date format !")
                    print("    Try again")
                    date = input(("""    Enter {} (format "DD/MM/YYYY") : """).format(subject))
        return date

    def get_selected_tournament_name():
        tournament_name = input(
            """   
                                    
                                        Select a tournament by entering its name : """
        )
        return tournament_name

    def get_winner_name():
        winner_name = input(
            """ 
                                   Enter the above match winner name (press "Enter" if a draw) : """
        )
        return winner_name
