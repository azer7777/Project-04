from views import entries,menu
from models import tournament,rounds,match,player

class Manager:
    def add_player():
        entries.Entries.get_player_entries()
        player.Player.load_player_to_json_file()
        
        
    

 


Manager.add_player()
