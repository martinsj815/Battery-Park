import time

import dash
import dash_bootstrap_components as dbc
import numpy as np
import plotly.graph_objs as go
from dash import Input, Output, dcc, html



app = dash.Dash(external_stylesheets=[dbc.themes.SPACELAB], suppress_callback_exceptions=True, use_pages=True)
app.scripts.config.serve_locally=True



navbar_children=[
    dbc.NavItem(dbc.NavLink("LiS", href="/Li-S", className="text-dark")),
    dbc.NavItem(dbc.NavLink("Formation", href="/formation", className="text-dark")),
    dbc.NavItem(dbc.NavLink("Cyclic_performance", href="/cycle", className="text-dark")),
    dbc.NavItem(dbc.NavLink("Voltage_profile", href="/voltage", className="text-dark")),
    dbc.NavItem(dbc.NavLink("LIB-Formation", href="/LIB_formation", className="text-dark")),
    dbc.NavItem(dbc.NavLink("LIB-Cycle", href="/LIB_cycle", className="text-dark")),
    dbc.NavItem(dbc.NavLink("LIB-Voltage_profile", href="/LIB_voltage", className="text-dark")),
    
]
navbar = dbc.Navbar(
    [
        html.A(
            dbc.Row(
                [   
                    dbc.Col(dbc.NavbarSimple(navbar_children))
                ]
            )
        )
    ]
)


app.layout = dbc.Container(
     [
         dcc.Store(id="store"),
         html.H1("Plot Cell Data"),
         html.Hr(),
         html.Div([
             navbar
         ]),
         html.Div(id="tab-content", className="p-4"),
         dash.page_container

         
     ]
 )

# app.layout = serve_layout
if __name__ == '__main__':
    #app.run(debug=True)
    app.run_server(debug=True, host='0.0.0.0', port=8050)