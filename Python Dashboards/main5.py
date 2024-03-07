import dash
from dash import html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

# Sample data
df = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    'Values': [10, 20, 15, 25, 30, 35, 40, 45, 50, 55],
    'Group': ['Group 1', 'Group 1', 'Group 2', 'Group 2', 'Group 3', 'Group 3', 'Group 4', 'Group 4', 'Group 5', 'Group 5']
})

# Create initial plots for each dashboard
fig1 = px.bar(df, x='Category', y='Values', title='Dashboard 1')
fig2 = px.scatter(df, x='Category', y='Values', title='Dashboard 2')
fig3 = px.line(df, x='Category', y='Values', title='Dashboard 3')

# Define the layout with tabs
app.layout = html.Div([
    html.H1("Story Dashboard"),
    dcc.Tabs([
        dcc.Tab(label='Dashboard 1', children=[
            dcc.Dropdown(
                id='group-dropdown',
                options=[{'label': 'All Groups', 'value': 'all'}] + [{'label': group, 'value': group} for group in df['Group'].unique()],
                value=['all'],
                multi=True
            ),
            dcc.Graph(id='bar-chart', figure=fig1)
        ]),
        dcc.Tab(label='Dashboard 2', children=[
            dcc.Graph(figure=fig2)
        ]),
        dcc.Tab(label='Dashboard 3', children=[
            dcc.Graph(figure=fig3)
        ]),
    ])
])

# Create callback to update plots based on dropdown value
@app.callback(
    Output('bar-chart', 'figure'),
    [Input('group-dropdown', 'value')]
)
def update_plot(selected_groups):
    if 'all' in selected_groups:
        filtered_df = df
    else:
        filtered_df = df[df['Group'].isin(selected_groups)]
    updated_fig = px.bar(filtered_df, x='Category', y='Values', title='Dashboard 1')
    return updated_fig

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8050, debug=True)
