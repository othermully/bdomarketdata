import json
import pandas as pd

file_path = "./output.json"

def main():
    parse_data()

def read_file(path):
    with open(path, 'r') as file:
        data = json.load(file)
    return data

def parse_data():
    data_dict = {}
    data_dict_list = []
    data = read_file(file_path)
    for single_item_list in data["data"]:
        data_dict["date"] = single_item_list[0]
        data_dict["price"] = single_item_list[1]
        data_dict["stock"] = single_item_list[2]
        data_dict["volume"] = single_item_list[3]
        data_dict_list.append(data_dict) 
    return data_dict_list

def create_dataframe():
    pass

main()
