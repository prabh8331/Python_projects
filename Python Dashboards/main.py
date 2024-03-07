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
    dcc.Dropdown(
        id='dashboard-selector',
        options=[
            {'label': 'Dashboard 1', 'value': 'dashboard1'},
            {'label': 'Dashboard 2', 'value': 'dashboard2'}
        ],
        value='dashboard1'
    ),
    html.Div(id='dashboard-container')
])

@app.callback(
    Output('dashboard-container', 'children'),
    [Input('dashboard-selector', 'value')]
)
def update_dashboard(selected_dashboard):
    if selected_dashboard == 'dashboard1':
        return dcc.Graph(figure=fig1)
    elif selected_dashboard == 'dashboard2':
        return dcc.Graph(figure=fig2)

if __name__ == '__main__':
    app.run_server(debug=True)
