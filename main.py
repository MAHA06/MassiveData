# Graph:	G_C Graph of the pages using FORMULA
# Structure:	Maximal Clique
import pandas as pd
import os

def get_formula(filename,dict):
    return dict[filename]["results"][0][0]['formula'][0]

def load_data(base_dir):
    # base_dir = '/Users/thijseekelaar/Downloads/airlines_complete'

    # Get all files in the directory

    data_list = {}
    for file in os.listdir(base_dir):

        # If file is a json, construct it's full path and open it, append all json data to list
        if 'json' in file:
            filenameWithoutExtension=os.path.splitext(file)[0]
            json_path = os.path.join(base_dir, file)
            json_data = pd.read_json(json_path, lines=True)
            data_list[filenameWithoutExtension]=json_data

    print(data_list)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    base_dir = "./sequences/sequences/"
    load_data(base_dir)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
