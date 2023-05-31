from models.rounds import Rounds
from models.save_load import SaveLoad

u = [(["d", 10], ["z", 22]), (["j", 55], ["l", 33])]

r = Rounds(1, u).get_round_maches_serialized()
a = SaveLoad.save(r, file_name="trydata")
