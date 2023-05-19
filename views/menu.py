

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
                          1 : Add a player             2 : Display all players
                          3 : Main menu                          
                               Enter a matching number to choose an option : """))
        if option == 1:
            Manager.add_player()
            print("""    Player successfully added""")
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
                          1 : Create a tournament         2 : Display all tournaments
                          3 : Select a tournament         4 : Main menu
                               Enter a matching number to choose an option : """))
        if option == 1:
            
            print("""    Tounament succesfully created""")
        elif option == 2:
            pass
        elif option == 3:
                name = input("""Enter a tournament name : """)
                # to do : display the selected tournament from the json_tournament_data_base
                option = int(input("""
                           1 : Modifie the tournament            2 : Display the registred players
                           3 : Display all rounds and matches    4 : Main menu      
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





