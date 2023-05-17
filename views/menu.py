class Menu:
    def main_menu():
        print("Welcome to chess applictaion")
        print("Player menu")
        print()
        option = int(input("""
                          1 : Player             2 : Tournament      
                               Enter a matching number to choose an option : """))
        if option == 1:
            pass
        if option == 2:
            pass
        else:
            print("You can only enter a matching number")
            
    def player_menu():
        print("Player menu")
        print()
        option = int(input("""
                          1 : add a player             2 : display all players                          
                               Enter a matching number to choose an option : """))
        if option == 1:
            pass
        else:
            print("You can only enter a matching number")
    
    def tournament_menu():
        print("Player menu")
        print()
        option = int(input("""
                          1 : create a tournament         2 : display all tournaments
                          3 : select a tournament         
                               Enter a matching number to choose an option : """))
        if option == 1:
            pass
        if option == 2:
            pass
        if option == 3:
                name = input("""Enter a tournament name : """)
                #display the selected tournament from the json_tournament_data_base
                option = int(input("""
                           1 : modifie the tournament         2 : display the registred players
                           3 : display all rounds and matches          
                               Enter a matching number to choose an option : """))
                if option == 1:
                    pass
                if option == 2:
                    pass
                if option == 3:
                    pass
                else:
                    print("You can only enter a matching number")

        else:
            print("You can only enter a matching number")        





a = Menu.tournament_menu()