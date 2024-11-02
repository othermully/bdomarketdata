import json
import pandas as pd

file_path = "./output.json"

def main():
    create_dataframe()
def read_file(path):
    with open(path, 'r') as file:
        data = json.load(file)
    return data

def parse_data():
    data_dict_list = []
    data = read_file(file_path)
    for single_item_list in data["data"]:
        #Creating a new dict for each item
        record = {
            'date': single_item_list[0],
            'price': single_item_list[1],
            'stock': single_item_list[2],
            'volume': single_item_list[3]
        }
        data_dict_list.append(record)
    return data_dict_list

def create_dataframe():
    df = pd.DataFrame(parse_data())
    print(df)

main()
