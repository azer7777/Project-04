import json
from os import path
import pandas
class SaveLoad():
    def save(info_serialized, file_name=""):
        if not path.exists(file_name):
            with open(file_name, 'w') as json_file:
                json.dump([info_serialized], json_file, 
                            indent=4,  
                            separators=(',',': '))
        else:       
            with open(file_name) as fp:
                data_list = json.load(fp)
            data_list.append(info_serialized)    
            with open(file_name, 'w') as json_file:
                json.dump(data_list, json_file,
                          indent=4,
                          separators=(',',': '))
        return    
    
    def load(file_name=""):
        with open(file_name) as fp:
            report = json.load(fp)
        print("""
                  All regestred players :
                                          """)
        print(pandas.DataFrame(report))

        return
        