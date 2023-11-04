import pandas as pd
import sys
from subprocess import run

file_path='wc.csv'

def read_dataset(file_path):
    try:
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)

        data = pd.read_csv(file_path)  
        print("Dataset Head:")
        print(data.head())
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_path>")
    else:
        file_path = sys.argv[1]
        read_dataset(file_path)
        
run(["python", "dpre.py", file_path])        
