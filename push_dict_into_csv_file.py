import os
import pandas as pd

def add_entries_to_csv(result, csv_file_path):
    df = pd.DataFrame(result, index=[0])
    if not os.path.isfile(csv_file_path):
        df.to_csv(csv_file_path, header=True, index=False)
    else:
        # else it exists so append without writing the header
        df.to_csv(csv_file_path, mode='a', header=False, index=False)
        
def add_results_to_csv(value, filename):
    # Append results to csv file
    add_entries_to_csv({"a": value, "b": value+3}, os.path.join(os.path.dirname(os.path.realpath(_file_)), f'{filename}.csv'))

filename = "test"
# Delete the csv file if already exists
if os.path.isfile(os.path.join(os.path.dirname(os.path.realpath(_file_)), f'{filename}.csv')):
    os.remove(os.path.join(os.path.dirname(os.path.realpath(_file_)),f'{filename}.csv'))
    print("Deleted the existing csv file")

add_results_to_csv(2, filename)