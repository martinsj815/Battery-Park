import os
import numpy as np
import dash
from dash import Dash, dcc, html, Input, Output, State, callback
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
import plotly.express as px
# Initialize the app
app_name = os.getenv("APP_NAME", "Beyond-Cell")
app = Dash( __name__,
    external_stylesheets=[dbc.themes.SANDSTONE]
)

app.title="Cell Design"

server = app.server

# App layout
app.layout = html.Div([
    html.Br(),
    html.Br(),
    dbc.Row([
    html.Div( className="app-header", children=[
        html.H1('Welcome to Beyond-Cell Design Platform', className="app-header--title")]),
    ],justify="center"),
    html.Br(),
    html.Br(),
    dbc.Row([
    dbc.Col(html.H6(children=" Batteries are complex devices. To optimize cell performance and develop new types of battery chemistry for practical applications, it is critical to allocate our precious resources effectively. The modeling tools here can play a significant role in providing valuable information for developing plans and strategies"),
            width=7),dbc.Col(width=3),
    ], justify="center"),
    dcc.Tabs(id='Options', value='tab-1', children=[
        dcc.Tab(label=' N/P ratio', value='NP'),
        dcc.Tab(label='Cathode', value='cat'),
        dcc.Tab(label='Cells', value='cells'),
    ]),
    html.Div(id='Options-content')
],
)

@app.callback(Output('Options-content', 'children'), [Input('Options','value')])

def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.H3('Design Pouch Cell'),
            html.P('Desing Li-metal, cathode, and stacking numbers')
        ])
    elif tab=='NP':
        return html.Div([
            html.H3('N/P ratio'),
            html.P('Design minium Li metal thickness')
        ])
    elif tab=='cat':
        return html.Div([
            html.H3('Types of Cathode'),
            html.P('Chooose Cathode and target energy density')
        ])
    elif tab=='cells':
        return html.Div([
            html.H3('Choose the dimension'),
            html.P('Choose cell dimension WxHXT mm')
        ])

# app.layout = html.Div(
#     [
#         html.Br(),
#         html.Br(),
#         dbc.Row(
#             [
#                 dbc.Col(html.H1(children=" Welcome to Cell Design "), width=7),
#                 dbc.Col(width=12),
#             ],
#             justify="center"),
#         html.Br(),
#         html.Br(),
#         dbc.Row(
#             [
#                 dbc.Col(
#                     html.Div(
#                         [
#                             html.H6(
#                                 children=" Batteries are complex devices. To optimize cell performance and develop new types of battery chemistry for practical applications, it is critical to allocate our precious resources effectively. The modeling tools here can play a significant role in providing valuable information for developing plans and strategies"
#
#                             ),
#         #                     html.Div(
#         #                         [
#         #                             dcc.Link(
#         #                                 html.Button(
#         #                                     "Home", id="home-button", className="p1"
#         #                                 ),
#         #                                 href=f"/{app_name}/",
#         #                             ),
#         #                             dcc.Link(
#         #                                 html.Button(
#         #                                     "Poutch", id="poutch-cell", className="p1"
#         #                                 ),
#         #                                 href=f"/{app_name}/Poutch",
#         #                             ),
#         #                         ],
#         #                     ),
#                          ]
#                      ),
#                      width=7,
#                  ),
#                  dbc.Col(width=3),
#              ],
#              justify="center",
#          ),
#          html.Br(),
#          html.Br(),
#     ]
# )


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'check, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run_server(debug=True, host='127.0.0.1',port=8050)

