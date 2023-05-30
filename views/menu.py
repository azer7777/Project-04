from controllers.manager import Manager
from views.entries import Entries

class Menu:
    def main_menu():
        print()
        print("""      Welcome to chess applictaion      """)
        print("""               Main menu                """)
        print()
        option = int(input("""
                          1 : Player_menu             2 : Tournament_menu      
                               Enter a matching number to choose an option : """))
        if option == 1:
            Menu.player_menu() 
        elif option == 2:
            Menu.tournament_menu()
        else:
            print("You can only enter a matching number !")
            Menu.main_menu()
        return
        
    def player_menu():
        print()
        print("""               Player menu                """)
        print()
        option = int(input("""
                          1 : Add a player             2 : Display all players
                          3 : Main menu                          
                               Enter a matching number to choose an option : """))
        if option == 1:
            Manager.add_player()
            Menu.player_menu()
        elif option == 2:
            Manager.display_all_players()
            Menu.player_menu()
        elif option == 3:
            Menu.main_menu()
        else:
            print("You can only enter a matching number !")
            Menu.player_menu()
        return
    
    def tournament_menu():
        print()
        print("""               Tournament menu                """)
        print()
        option = int(input("""
                          1 : Create a tournament         2 : Display all tournaments
                          3 : Select a tournament         4 : Main menu
                               Enter a matching number to choose an option : """))
        if option == 1:
            Manager.create_tournament()
            Menu.tournament_menu()    
        elif option == 2:
            Manager.display_all_tournaments()
            Menu.tournament_menu()
        elif option == 3:
                tournament_name = Entries.get_selected_tournament_name()
                select_tournament = Manager.select_tournament(tournament_name)
                if select_tournament == None:
                    Menu.tournament_menu()
                else:                    
                    option = int(input("""
                               1 : Modifie the tournament           2 : Display the players
                               3 : Display the details              4 : Tournament menu      
                                   Enter a matching number to choose an option : """))
                if option == 1:
                    option = int(input("""
                               1 : Create a round            2 : End current round
                               3 : Tournament menu          
                                   Enter a matching number to choose an option : """))
                    if option == 1:
                        pass
                    elif option == 2:
                        pass
                    elif option == 3:
                        Menu.tournament_menu()
                    else:
                        print("You can only enter a matching number !")
                        Menu.tournament_menu()
                elif option == 2:
                    Manager.display_tournament_players(tournament_name)
                    Menu.tournament_menu()
                elif option == 3:
                    option = int(input("""
                               1 : Display all rounds            2 : Display all matches
                               3 : Display results               4 : Tournament menu      
                                   Enter a matching number to choose an option : """))
                    if option == 1:
                        pass
                    elif option == 2:
                        pass
                    elif option == 3:
                        pass
                    elif option == 4:
                        Menu.tournament_menu()
                    else:
                        print("You can only enter a matching number !")
                        Menu.tournament_menu()
                elif option == 4:
                    Menu.tournament_menu()
                else:
                    print("You can only enter a matching number !")
                    Menu.tournament_menu()
        elif option == 4:
            Menu.main_menu()  
        else:
            print("You can only enter a matching number !")
            Menu.tournament_menu()
        return      





