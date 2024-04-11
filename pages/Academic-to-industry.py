import os
import numpy as np
import pandas as pd
import dash
from dash import Dash, dash_table, dcc, html, Input, Output, State, callback
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
import plotly.express as px
import dash_mantine_components as dmc
from collections import OrderedDict
from dash.exceptions import PreventUpdate

dash.register_page(
    __name__, name="Academic-to-Industry", top_nav=True, path="/academic-to-industry"
    )

data_election = OrderedDict(
    [
        (
            "Cathode Name",
            [
                "Lithium Cobalt Oxide (LCO)",
                "Lithium Manganese Oxide",
                "Lithium Iron Phosphate (LFP)",
                "Lithium Nickel Cobalt Manganese Oxide (NCM)",
                "",
                "",
                "Lithium Nickel Cobalt Aluminum Oxide (NCA)",
            ], 
        ),
        (
            "Crystal Structure",
            [
                "Layered", 
                "Spinel", 
                "Olivine",
                "Layered",
                "",
                "",
                "Layered",             
            ],
        ),
        (
            "Stoichiometry", 
            [
                "LiCoO<sub>2</sub>", 
                "LiMn<sub>2</sub>O<sub>4</sub>",
                "LiFePO<sub>4</sub>",
                "NCM111",
                "NCM622",
                "NCM811",
                "LiNi<sub>0.8</sub>Co<sub>0.15</sub>Al<sub>0.05</sub>O<sub>2</sub>",
            ]
        ),
        (
            "Specific Capacity (mAh/g) \n (The/Exp)",
            [
                "274/148",
                "148/120",
                "170/165",
                "280/160",
                "275/170",
                "275/200",
                "279/200",
            ],
        ),
        (
            "Average Voltage \n (V)",
            [
                "3.8",
                "4.1",
                "3.4",
                "3.7",
                "",
                "",
                "3.7",
            ],
        ),
        (
            "Pros",
            [
                "* Good structural stability",
                "* Cost efficient",
                "* Cost affordable \n * Thermal stability",
                "",
                "",
                "* High specific capacity \n * High energy density",
                "* High specific capacity \n * High energy density",
            ],
        ),
        (
            "Cons",
            [
                "* Co expensive \n * Unstable upon charging >50%",
                "* Mn dissolution in electrolyte",
                "* Low ionic conductivity \n * Low energy density",
                "",
                "",
                "* Cycle instability for high Ni content \n * Co expensive",
                "* Cycle/Thermal instability \n * Co expensive",
            ],
        ),
    ],
)

dt = pd.DataFrame(data_election)

layout = html.Div([
                html.Link(rel='stylesheet', href='/assets/table.css'),      
            dbc.Row([
                dbc.Col([
                        dcc.Markdown('- Academic-to-Industry', style={'font-size':'35px', 'font-weight':'bold'},),
                        html.Br(),                        
                        dcc.Markdown(('- There is a clear technological gap between academic research and industry requirements. Academic research uses the testing parameters and conditions that are way off from those that are adopted in commercial cell manufacturing. Adjusting key metrics including N/P ratio based upon electrode areal capacities and electrolyte amounts to the industrial setting is not the primary target in academia as its focus is much on materials discovery and cell performance enhancement through it, which can quite frequently be realized through small cell assembly and testing. For EV battery suppliers and automative OEMs who need to meet requirements/demands on safety, cell energy density and power capability, it is also inevitable for them to think about the cost and energy consumption for manufacturing and hence are much sensitive and even eyeing for improvement in those metrics.'), 
                                 style={'textAlign':'justify', 'margin-left':'20px', 'font-size':'18px'}),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        dash_table.DataTable(
                                style_cell={'font-family': 'Arial', 'font-size': '16px', 'text-align':'center', 'margin-top':'10px', 'padding':5}, 
                                markdown_options={"html": True},
                                style_data={
                                        'whiteSpace': 'normal',
                                        'color': 'black',
                                        'backgroundColor': 'white',
                                        'height':'auto',
                                        'lineheight':'10px',
                                },
                                style_data_conditional=[
                                {
                                    'if': {'column_id': 'Cathode Name'},
                                    'fontWeight': 'bold', 
                                },
                                ],
                                style_header={
                                    'whiteSpace': 'normal',
                                    #'backgroundColor': 'rgb(210, 210, 210)',
                                    'backgroundColor': 'black',
                                    'color': 'white',
                                    'fontWeight': 'bold',
                                    'font-size': '18px',
                                    'text-align':'center'
                                },
                                data=dt.to_dict('records'),
                                columns=[{'id': c, 'name': c,"presentation": "markdown"} for c in dt.columns],
                        ),
                        ],style={'textAlign':'justify', 'margin-left':'30px', 'margin-right':'30px'},
                ),
                ]),
                html.Div(id='Options-content'),
        ])
