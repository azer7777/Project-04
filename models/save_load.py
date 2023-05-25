import json
from os import path
import pandas
class SaveLoad():
    def save(data_serialized, file_name=""):
        if not path.exists("database/" + file_name):
            with open("database/" + file_name, 'w') as json_file:
                json.dump([data_serialized], json_file, 
                            indent=4,  
                            separators=(',',': '))
        else:       
            with open("database/" + file_name) as fp:
                data_list = json.load(fp)
            data_list.append(data_serialized)    
            with open("database/" + file_name, 'w') as json_file:
                json.dump(data_list, json_file,
                          indent=4,
                          separators=(',',': '))
        return    
    
    def load(file_name=""):
        with open("database/" + file_name) as fp:
            report = json.load(fp)
        subject = (file_name).replace("_", " ").replace("info", "")
        print("""
                         All {} :
                                          """.format(subject))
        if "Family_name" in pandas.DataFrame(report):
            print(pandas.DataFrame(report).sort_values("Family_name"))
        else:
            print(pandas.DataFrame(report))
        return
    


    def load_only(file_name=""):
        with open("database/" + file_name) as fp:
            report = json.load(fp)
        return report        
            