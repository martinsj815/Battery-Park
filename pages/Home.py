import os
import dash
from dash import Dash, dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate

dash.register_page(
    __name__, name="home", top_nav=True, path="" or "/"
)

layout = html.Div(
    [
        html.Br(),
        html.Br(),
        html.Br(),
        dbc.Row([
            dbc.Col(html.Div(children="Welcome to Battery Park"),
                    width=11), 
        ], style={'justify':'center','font-size':'60px','font-weight':'bold','text-align':'center','margin-left': '20px'}),
        html.Br(),
        html.Br(),
        dbc.Row([
            dbc.Col(html.H5(children="Batteries play a crucial role in our daily lives, powering everything from smartphones to electric vehicles. As the demand for higher performance increases and the availability of battery constituent resources becomes scarcer, there is an urgent need to concentrate on developing batteries with optimized parameters through efficient resource allocation."),
                    width=11),
        ], style={'justify':'center','text-align':'center','margin-left': '20px'}),
        html.Br(),
        html.Br(),
        html.Div( className="app-header", style={'background-image':'url("https://dl.dropboxusercontent.com/scl/fi/djio7asr23jaq6emicq0o/image_home.jpg?rlkey=02hyor71gv7cjuzjru144hox0&raw=1")',
                      'background-size': '100vh', 'background-repeat':'no-repeat',
                      'background-position':'center', 'height':'50vh', 'margin-bottom':'0px'}),
        html.Br(),  
        html.Br(),      
    ]
)
