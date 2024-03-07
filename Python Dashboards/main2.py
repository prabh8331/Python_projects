import dash
from dash import html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

# Sample data
df = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [10, 20, 15, 25]
})

# Create initial charts
fig1 = px.bar(df, x='Category', y='Values', title='Dashboard 1')
fig2 = px.scatter(df, x='Category', y='Values', title='Dashboard 2')

app.layout = html.Div([
    html.H1("Story Dashboard"),
    html.Div([
        dcc.Graph(figure=fig1),
        dcc.Graph(figure=fig2)
    ], style={'display': 'flex'})
])

if __name__ == '__main__':
    # Run the app on your server IP and port of your choice
    app.run_server(host='0.0.0.0', port=8050, debug=True)
