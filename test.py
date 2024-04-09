import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Create the Dash application
app = dash.Dash(__name__)

# Define the layout of the application
app.layout = html.Div([
    html.H1("Simple Dash Application"),
    dcc.Input(id='input', value='', type='text'),
    html.Div(id='output')
])

# Define callback to update the output based on the input value
@app.callback(
    Output(component_id='output', component_property='children'),
    [Input(component_id='input', component_property='value')]
)
def update_output_div(input_value):
    return f'Output: {input_value}'


# Run the Dash application
if __name__ == '__main__':
    app.run_server(debug=True)
