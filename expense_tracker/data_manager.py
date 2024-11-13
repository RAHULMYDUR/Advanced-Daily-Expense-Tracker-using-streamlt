import pandas as pd
import os
from .config import EXPENSE_FILE

def initialize_file():
    if not os.path.exists(EXPENSE_FILE):
        df = pd.DataFrame(columns=['Date', 'Amount (INR)', 'Category', 'Description'])
        df.to_csv(EXPENSE_FILE, index=False)

def load_data():
    try:
        if os.path.exists(EXPENSE_FILE):
            return pd.read_csv(EXPENSE_FILE)
        else:
            return pd.DataFrame(columns=['Date', 'Amount (INR)', 'Category', 'Description'])
    except Exception as e:
        return pd.DataFrame(columns=['Date', 'Amount (INR)', 'Category', 'Description'])

def add_expense(date, amount, category, description):
    new_expense = pd.DataFrame({
        'Date': [date], 
        'Amount (INR)': [amount], 
        'Category': [category], 
        'Description': [description]
    })
    new_expense.to_csv(EXPENSE_FILE, mode='a', header=False, index=False)

def delete_expense(date, amount, category):
    df = load_data()
    df = df[~((df['Date'] == date) & (df['Amount (INR)'] == amount) & (df['Category'] == category))]
    df.to_csv(EXPENSE_FILE, index=False)
