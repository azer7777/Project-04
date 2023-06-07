from models.save_load import SaveLoad


class Tournament:
    def __init__(
        self, name, place, tournament_players_list, start_date, end_date, current_round_nb, description, nb_of_rounds=4
    ):
        self.name = name
        self.place = place
        self.tournament_players_list = tournament_players_list
        self.star_date = start_date
        self.end_date = end_date
        self.current_round_nb = current_round_nb
        self.description = description
        self.nb_of_rounds = nb_of_rounds

    def create_tournament_players_list():
        input_message = """Enter the number of players (must be even) : """
        nb_of_players = Tournament.check_integer(input_message)
        while (nb_of_players % 2) != 0:
            print("Must be even !")
            print("Try again")
            nb_of_players = Tournament.check_integer(input_message)
        SaveLoad.load(file_name="registred_players")
        tournament_players_list = []
        for i in range(nb_of_players):
            player_name = input("Select a player from  the above list by entring a family name : ")
            selection = SaveLoad.selected_archive("Family_name", player_name, file_name="registred_players")
            while selection is None:
                print("Invalid family name !")
                print("Try again")
                player_name = input("Select a player from  the above list by entring a family name : ")
                selection = SaveLoad.selected_archive("Family_name", player_name, file_name="registred_players")
            tournament_players_list.append(selection)
            print("   Player selected")
        return tournament_players_list

    def get_tournament_info_serialized(self):
        tournament_info_serialized = {
            "Tournament_name": self.name,
            "Place": self.place,
            "Nb_of_rounds": self.nb_of_rounds,
            "Current_round_nb": self.current_round_nb,
            "Description": self.description,
            "Start_date": self.star_date,
            "End_date": self.end_date,
        }
        return tournament_info_serialized

    def get_tournament_players_serialized(self):
        tournament_players_serialized = self.tournament_players_list
        return tournament_players_serialized

    def get_current_round_nb(tournament_name):
        selected_tournament = SaveLoad.selected_archive(
            "Tournament_name", tournament_name, file_name="tournaments_info"
        )
        current_round_nb = selected_tournament["Current_round_nb"]
        return current_round_nb

    def check_round_statute(tournament_name, current_round_nb):
        round_name = "Round" + " " + str(current_round_nb)
        selected_round = SaveLoad.selected_archive(
            "Round_name", round_name, file_name=("rounds_info/" + tournament_name)
        )
        statute = selected_round["End_date_time"]
        return statute

    def check_integer(input_message):
        user_input = ""
        while user_input is not int:
            try:
                user_input = int(input(input_message))
                break
            except ValueError:
                print("Must be integer !")
                print("Try again")
        return user_input
