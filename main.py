import json
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

file_path = "./output.json"

def main():
    eval_and_predict()

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
    return df

def data_preparation():
    df = create_dataframe()

    feature_columns = ['date', 'stock', 'volume']
    X = df[feature_columns]
    y = df['price']

    X_train, X_test, y_train, y_test = train_test_split(X,y)

    return X_train, X_test, y_train, y_test

def eval_and_predict():
    X_train, X_test, y_train, y_test = data_preparation()

    lrmodel = LinearRegression()
    lrmodel.fit(X_train, y_train)

    prediction = lrmodel.predict(X_train)
    print('Predicted Price:', prediction[0])
    print('Actual value:', y_train[:1])



main()
