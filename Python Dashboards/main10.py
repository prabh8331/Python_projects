import dash
from dash import html, dcc, Input, Output
import plotly.express as px
import pandas as pd

# Sample data
df = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D', 'E'],
    'Values': [10, 20, 15, 25, 30]
})

app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div([
    html.H1("Drag and Drop Columns Dashboard"),
    html.Div([
        dcc.Dropdown(
            id='plot-type',
            options=[
                {'label': 'Bar Chart', 'value': 'bar'},
                {'label': 'Line Chart', 'value': 'line'},
                {'label': 'Scatter Plot', 'value': 'scatter'}
            ],
            value='bar'
        )
    ]),
    html.Div([
        dcc.Dropdown(
            id='x-axis',
            options=[{'label': col, 'value': col} for col in df.columns],
            value='Category'
        ),
        dcc.Dropdown(
            id='y-axis',
            options=[{'label': col, 'value': col} for col in df.columns],
            value='Values'
        )
    ]),
    html.Div([
        dcc.Graph(id='plot')
    ])
])

# Create callback to update the plot based on the selected columns and plot type
@app.callback(
    Output('plot', 'figure'),
    [Input('x-axis', 'value'),
     Input('y-axis', 'value'),
     Input('plot-type', 'value')]
)
def update_plot(x_axis, y_axis, plot_type):
    if plot_type == 'bar':
        fig = px.bar(df, x=x_axis, y=y_axis)
    elif plot_type == 'line':
        fig = px.line(df, x=x_axis, y=y_axis)
    elif plot_type == 'scatter':
        fig = px.scatter(df, x=x_axis, y=y_axis)
    else:
        fig = px.bar(df, x=x_axis, y=y_axis)
    return fig

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8050, debug=True)
