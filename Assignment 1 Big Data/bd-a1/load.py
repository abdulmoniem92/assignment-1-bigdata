import pandas as pd
import sys

def load_data(filepath):
    df = pd.read_csv(filepath)
    return df

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the file path as an argument.")
    else:
        filepath = sys.argv[1]
        df = load_data(filepath)
        print(df)
        df.to_csv('res.csv', index=False)
