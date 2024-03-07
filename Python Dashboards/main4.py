import dash
from dash import html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

# Sample data with multiple groups
df = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    'Values': [10, 20, 15, 25, 30, 35, 40, 45, 50, 55],
    'Group': ['Group 1', 'Group 1', 'Group 2', 'Group 2', 'Group 3', 'Group 3', 'Group 4', 'Group 4', 'Group 5', 'Group 5']
})

# Create initial plots
fig1 = px.bar(df, x='Category', y='Values', title='Dashboard 1')
fig2 = px.scatter(df, x='Category', y='Values', title='Dashboard 2')

# Create layout with multi-select dropdown and plots
app.layout = html.Div([
    html.H1("Story Dashboard"),
    dcc.Dropdown(
        id='group-dropdown',
        options=[{'label': 'All Groups', 'value': 'all'}] + [{'label': group, 'value': group} for group in df['Group'].unique()],
        value=['all'],
        multi=True
    ),
    html.Div([
        dcc.Graph(id='bar-chart', figure=fig1),
        dcc.Graph(id='scatter-plot', figure=fig2)
    ], style={'display': 'flex'})
])

# Create callback to update plots based on dropdown value
@app.callback(
    [Output('bar-chart', 'figure'),
     Output('scatter-plot', 'figure')],
    [Input('group-dropdown', 'value')]
)
def update_plots(selected_groups):
    if 'all' in selected_groups:
        filtered_df = df
    else:
        filtered_df = df[df['Group'].isin(selected_groups)]
    updated_fig1 = px.bar(filtered_df, x='Category', y='Values', title='Dashboard 1')
    updated_fig2 = px.scatter(filtered_df, x='Category', y='Values', title='Dashboard 2')
    return updated_fig1, updated_fig2

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8050, debug=True)
