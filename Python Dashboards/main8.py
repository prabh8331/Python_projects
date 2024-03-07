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
fig1_1 = px.bar(df, x='Category', y='Values', title='Dashboard 1 - Plot 1')
fig1_2 = px.scatter(df, x='Category', y='Values', title='Dashboard 1 - Plot 2')
fig2 = px.scatter(df, x='Category', y='Values', title='Dashboard 2')
fig3 = px.line(df, x='Category', y='Values', title='Dashboard 3')

# Define the layout with tabs
app.layout = html.Div([
    html.H1("Story Dashboard"),
    dcc.Tabs([
        dcc.Tab(label='Dashboard 1', children=[
            html.Div([
                html.Div([
                    dcc.Checklist(
                        id='group-checkboxes',
                        options=[{'label': group, 'value': group} for group in df['Group'].unique()],
                        value=df['Group'].unique()
                    ),
                ], style={'float': 'right'}),
                html.Div([
                    dcc.Graph(id='bar-chart', figure=fig1_1),
                    dcc.Graph(id='scatter-plot', figure=fig1_2)
                ], style={'display': 'flex'}),
            ]),
        ]),
        dcc.Tab(label='Dashboard 2', children=[
            dcc.Graph(figure=fig2)
        ]),
        dcc.Tab(label='Dashboard 3', children=[
            dcc.Graph(figure=fig3)
        ]),
    ])
])

# Create callback to update plots based on checkbox value
@app.callback(
    [Output('bar-chart', 'figure'),
     Output('scatter-plot', 'figure')],
    [Input('group-checkboxes', 'value')]
)
def update_plots(selected_groups):
    if 'all' in selected_groups:
        filtered_df = df
    else:
        filtered_df = df[df['Group'].isin(selected_groups)]
    updated_fig1_1 = px.bar(filtered_df, x='Category', y='Values', title='Dashboard 1 - Plot 1')
    updated_fig1_2 = px.scatter(filtered_df, x='Category', y='Values', title='Dashboard 1 - Plot 2')
    return updated_fig1_1, updated_fig1_2


if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8050, debug=True)
