import pandas as pd
import os

DATA_FILE = 'expenses.csv'
COLUMNS = ['Date', 'Amount', 'Category', 'Notes']

def load_data():
    if os.path.exists(DATA_FILE):
        try:
            df = pd.read_csv(DATA_FILE)
            if df.empty and os.path.getsize(DATA_FILE) > 0:     # 有檔案，但是內容是空的
                return pd.DataFrame(columns=COLUMNS)
            return df
        except pd.errors.EmptyDataError:    # 完全沒內容
            return pd.DataFrame(columns=COLUMNS)
    else:
        return pd.DataFrame(columns=COLUMNS)

def save_data(df):
    df.to_csv(DATA_FILE, index=False)

def add_expense(date, amount, category, notes):
    df = load_data()
    new_expense = pd.DataFrame([[date, amount, category, notes]], columns=COLUMNS)
    df = pd.concat([df, new_expense], ignore_index=True)
    save_data(df)
