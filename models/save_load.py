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
    
    def save_tournament_players(data_serialized, file_name=""):
        with open("database/" + file_name, 'w') as json_file:
            json.dump(data_serialized, json_file, 
                        indent=4,  
                        separators=(',',': '))
        return   
    
    def load(file_name="", title=""):
        with open("database/" + file_name) as fp:
            report = json.load(fp)
        print("""
                         All {} :
                                          """.format(title))
        if "Family_name" in pandas.DataFrame(report):
            print(pandas.DataFrame(report).sort_values("Family_name"))
        else:
            print(pandas.DataFrame(report))
        return
    
    def load_only(file_name=""):
        with open("database/" + file_name) as fp:
            report = json.load(fp)
        return report        
    
    def selected_archive(archive_name, key="", file_name=""):
        all_archives = SaveLoad.load_only(file_name)
        selection = next((sub for sub in all_archives if sub[key] == archive_name), None)
        return selection 
    
    def update(element_name, changes, file_name=""):
        selected_element = SaveLoad.selected_element(element_name, file_name)
        with open("database/" + file_name) as fp:
            data_list = json.load(fp)
        selection_index = data_list.index(selected_element)
        data_list[selection_index].update(changes)    
        with open("database/" + file_name, 'w') as json_file:
            json.dump(data_list, json_file,
                          indent=4,
                          separators=(',',': '))
      