import os
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import dash
import plotly.graph_objs as go
import plotly.express as px

# Initialize the app
app_name = os.getenv("APP_NAME", "Beyond-Cell")
app = dash.Dash(
    external_stylesheets=[dbc.themes.LUX], suppress_callback_exceptions=True
)

app.title="Cell Design"

server = app.server
"""Homepage"""
app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content"),]
)

index_page = html.Div(
    [
        html.Br(),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(html.H1(children=" Welcome to Cell Design "), width=5),
                dbc.Col(width=5),
            ],
            justify="center",
        ),
        html.Br(),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [
                            html.H4(
                                children=" Batteries are complex devices. To optimize cell performance and develop new types of battery chemistry for practical applications, it is critical to allocate our precious resources effectively. The modeling tools here can play a significant role in providing valuable information for developing plans and strategies"

                            ),
                            html.Div(
                                [
                                    dcc.Link(
                                        html.Button(
                                            "Home", id="home-button", className="p1"
                                        ),
                                        href=f"/{app_name}/",
                                    ),
                                    dcc.Link(
                                        html.Button(
                                            "Poutch", id="poutch-cell", className="p1"
                                        ),
                                        href=f"/{app_name}/Poutch",
                                    ),
                                ]
                            ),
                        ]
                    ),
                    width=7,
                ),
                dbc.Col(width=3),
            ],
            justify="center",
        ),
        html.Br(),
        html.Br(),
    ]
)
def print_hi(name):
    print(f'check,{name}')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run_server(debug=False)

