import os
import dash
from dash import dcc
from dash import html, Input, Output
import dash_bootstrap_components as dbc


app_name = os.getenv("APP_NAME", "Beyond-Cell")
app = dash.Dash(
    external_stylesheets=[dbc.themes.SANDSTONE]
)

app.title="Cell Design"
server = app.server
"""Homepage"""
app.layout = html.Div(
    [
        dbc.Row([
            html.Div(className="app-header", children=[
                html.H1("welcome to beyond-cell design")
            ])
        ]), html.Div(id='Options-content')
    ]
)
@app.callback(Output('options-content','children'),[Input('Options','value')])

def print_hi(name):
    print(f'check,{name}')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run_server(debug=False, host="127.0.0.1")
