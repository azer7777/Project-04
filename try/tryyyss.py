    def try_select_tournament():
        Manager.display_all_tournaments()
        tournament_index = int(input("Select a tournament from  the above list by entring a matching number : "))
        selected_tournament = SaveLoad.load_only(file_name="tournaments_info")[tournament_index]
        print("""       
                       Selected tournament : 
                                                    """)
        print(pandas.DataFrame([selected_tournament]))
        tournament_name = selected_tournament["Tournament_name"]
        return tournament_name