import json
from os import path
import pandas
class SaveLoad():
    def save(info_serialized, file_name=""):
        if not path.exists("data/" + file_name):
            with open("data/" + file_name, 'w') as json_file:
                json.dump([info_serialized], json_file, 
                            indent=4,  
                            separators=(',',': '))
        else:       
            with open("data/" + file_name) as fp:
                data_list = json.load(fp)
            data_list.append(info_serialized)    
            with open("data/" + file_name, 'w') as json_file:
                json.dump(data_list, json_file,
                          indent=4,
                          separators=(',',': '))
        return    
    
    def load(file_name=""):
        with open("data/" + file_name) as fp:
            report = json.load(fp)
        print("""
                  All regestred players :
                                          """)
        print(pandas.DataFrame(report).sort_values("Family_name"))

        return
        