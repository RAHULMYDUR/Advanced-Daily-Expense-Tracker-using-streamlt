import plotly.express as px
import pandas as pd

def plot_expense_data(df, chart_type='Bar'):
    df['Date'] = pd.to_datetime(df['Date']).dt.date  # Remove time
    if chart_type == 'Bar':
        fig = px.bar(df, x='Date', y='Amount (INR)', color='Category', title="Expenses Over Time")
    else:
        fig = px.line(df, x='Date', y='Amount (INR)', color='Category', title="Expenses Over Time")
    return fig
