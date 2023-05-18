from views.entries import Entries

class Menu:
    def main_menu():
        print()
        print("""      Welcome to chess applictaion      """)
        print("""               Main menu                """)
        print()
        option = int(input("""
                          1 : Player             2 : Tournament      
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
                          1 : add a player             2 : display all players
                          3 : main menu                          
                               Enter a matching number to choose an option : """))
        if option == 1:
            Entries.get_player_entries()
        elif option == 2:
            pass
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
                          1 : create a tournament         2 : display all tournaments
                          3 : select a tournament         4 : main menu
                               Enter a matching number to choose an option : """))
        if option == 1:
            Entries.get_tournament_entries()
        elif option == 2:
            pass
        elif option == 3:
                name = input("""Enter a tournament name : """)
                # to do : display the selected tournament from the json_tournament_data_base
                option = int(input("""
                           1 : modifie the tournament            2 : display the registred players
                           3 : display all rounds and matches    4 : main menu      
                               Enter a matching number to choose an option : """))
                if option == 1:
                    pass
                elif option == 2:
                    pass
                elif option == 3:
                    pass
                elif option == 4:
                    Menu.main_menu()
                else:
                    print("You can only enter a matching number !")
                    Menu.tournament_menu()
        elif option == 4:
            Menu.main_menu()  
        else:
            print("You can only enter a matching number !")
            Menu.tournament_menu()
        return      





Menu.main_menu()