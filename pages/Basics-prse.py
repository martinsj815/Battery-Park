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
    __name__, name="Primary vs Secondary", top_nav=True, path="/basics-prse"
    )

#dash.register_page(__name__, name="basics", top_nav=False)
data_election = OrderedDict(
    [
        (
            "Types",
            [
                "Alkaline",
                "Dry Cell",
                "Silver Oxide",
            ], 
        ),
        (
            "Negative electrode",
            [
             "Zn", 
             "Zn", 
             "Zn",
             ],
        ),
        (
            "Positive electrode", 
            [
            "MnO<sub>2</sub>", 
            "Carbon",
            "Ag<sub>2</sub>O",
            ]),
        (
            "Electrolyte",
        [
            "KOH",
            "NH<sub>4</sub>Cl (or ZnCl<sub>2</sub>) (Paste)",
            "NaOH (or KOH)",
        ]
        ),
        (
            "Representative reaction",
        [
            "Zn(s)+2MnO<sub>2</sub>(s) &rArr; ZnO(s)+Mn<sub>2</sub>O<sub>3</sub>(s)",
            "Zn + 2 MnO<sub>2</sub> + 2 NH<sub>4</sub>Cl + H<sub>2</sub>O &rArr; ZnCl<sub>2</sub>+ Mn<sub>2</sub>O<sub>3</sub>+ 2 NH<sub>4</sub>OH \n (Zn + 2MnO<sub>2</sub> + H<sub>2</sub>O &rArr; Mn<sub>2</sub>O<sub>3</sub> + Zn(OH)<sub>2</sub>)",
            "Zn(s) + H<sub>2</sub>O(l) + Ag<sub>2</sub>O(s) &rArr; Zn(OH)<sub>2</sub>(s) + 2Ag(s)",
        ]
        ),
        (
            "Nominal voltage (V)",
        [
            "1.5",
            "1.5",
            "1.55",
        ]
        ),
        (
            "Applications",
        [
            "Portable electronics, Flash lights, Toys",
            "Remote control, Smoke detectors, Clocks",
            "Watches, Hearing aids, Device instruments",
        ]
        ),
        (
            "Form factors",
        [
            "Cylindrical",
            "Cylindrical",
            "Button",
        ]
        ),
        ],
)

data_election2 = OrderedDict(
    [
        (
            "Types",
            [
                "Lead-Acid",
                "Nickel-Cadmium",
                "Nickel-Metal Hydride",
                "Lithium-ion",
                "Sodium-ion",
                "Zinc-ion"
            ], 
        ),
        (
            "Negative electrode",
            [
             "Pb", 
             "Cd", 
             "Intermetallic compound (M)",
             "Carbon (Graphite), Silicon, Li metal",
             "",
             "Zn"
             ],
        ),
        ("Positive electrode", 
         [
             "PbO<sub>2</sub>", 
             "NiO(OH)", 
             "NiO(OH)",
             "Layered oxides (LCO, LMO, LFP, NCM,...)",
             "",
             "mainly MnO<sub>2</sub>"
          ]),   
        (
        "Electrolyte",
        [
             "H<sub>2</sub>SO<sub>4</sub>", 
             "KOH", 
             "KOH",
             "Wide variety liquid w/ low to high concentration solute",
             "",
             "Liquid (Aqueous/Non-aqueous) w/ sulfate, TFSI, triflate solute"
         ],),
         (
        "Representative reaction",
        [
             "Pb(s)+PbO<sub>2</sub>(s)+2H<sub>2</sub>SO<sub>4</sub>(aq) &hArr; 2PbSO<sub>4</sub>(s)+2H<sub>2</sub>O(l)", 
             "2NiO(OH)(s) + Cd(s) + 2H<sub>2</sub>O(l) &hArr; 2Ni(OH)<sub>2</sub>(s) + Cd(OH)<sub>2</sub>(s)", 
             "MH + NiO(OH)(s) <--> M + Ni(OH)<sub>2</sub>(s)",
             "LiMO<sub>2</sub>(s) + C(s) <--> Li<sub>x</sub>C(s) + Li<sub>1-x</sub>MO<sub>2</sub>(s)",
             "",
             "",
        ],
        ),
        (
        "Nominal voltage (V)",
        [
             "2.1", 
             "1.2", 
             "1.2",
             "3.2-4",
             "3-3.1",
             "1.3",
        ],
        ),
        (
        "Applications",
        [
             "Solar panels, Cars, Emergency power system", 
             "Portable electronics, small power tools", 
             "HEV, PHEV, Consumer electronics",
             "EV, PHEV, Portable electronics",
             "EV, Small E-mobiles, Grid battery, Small consumer devices",
             "Stationary energy grid",
        ],
        ),
        (
        "Form factor",
        [
             "Prismatic", 
             "Cylindrical", 
             "Cylindrical",
             "Cylindrical, Prismatic, Pouch",
             "Cylindrical, Primsatic, Pouch",
             "Pouch",
        ],
        ),
        ],
)

df = pd.DataFrame(data_election)
df2 = pd.DataFrame(data_election2)

layout = html.Div([
             dbc.Row([
                dbc.Col([
                    dbc.Row([
                        dcc.Markdown('* Primary Cell', style={'font-size':'20px', 'textAlign':'left','font-weight':'bold'}),
                        dbc.Col([
                        html.Div(('- It is a galvanic cell that can only be used once before disposal as the electrochemical reaction is irreversible and the cell is unable to be recharged with electricity.'), 
                                 style={'textAlign':'justify', 'margin-left':'20px', 'font-size':'16px'}),
                        html.Br(),
                        html.Div( html.Img(src='https://dl.dropboxusercontent.com/scl/fi/we5r1v5ibif9pdcj1ez0t/Primary-battery.png?rlkey=w61wlssuevd3iq0i1zjf91ugb&st=zzirqevg&raw=1', style={"width":"60%", "display": "block", "margin": "auto", "justify-content":"center"}), 
                                 ),
                        ], width={"size": 6}, style={"margin-bottom":"20px"},
                        xs=12, sm=10, md=10, lg=6, xl=6
                        ),
                        dbc.Col([
                            dash_table.DataTable(
                                markdown_options={"html": True},
                                style_table={'overflowX': 'auto', 'minWidth':400},
                                style_cell={'font-family': 'Arial', 'font-size': '14px', 'text-align':'left', 'margin-top':'10px'}, 
                                style_data={
                                        'whiteSpace': 'break-spaces',
                                        'color': 'black',
                                        'backgroundColor': 'white',
                                        'height':'auto',
                                        'lineheight':'15px'
                                },
                                style_data_conditional=[
                                {
                                    'if': {'row_index': 'odd'},
                                    'backgroundColor': 'rgb(220, 220, 220)',
                                },
                                {
                                    'if': {'column_id': ''},
                                    'fontWeight': 'bold' 
                                },
                                ],
                                style_header={
                                    'backgroundColor': 'rgb(210, 210, 210)',
                                    'color': 'black',
                                    'fontWeight': 'bold',
                                    'font-size': '14px'
                                },
                                data=df.to_dict('records'),
                                columns=[{'id': c, 'name': c, "presentation": "markdown"} for c in df.columns]
                            ),
                        ], width={"size": 6},
                        xs=10, sm=8, md=6, lg=6, xl=6
                        ),
                    ],),
                    html.Br(),
                    html.Br(),
                    dbc.Row([
                        html.Br(),
                        dmc.Divider(size="md", variant="dotted", color="grey"),
                        html.Br(),
                        dcc.Markdown('* Secondary Cell', style={'font-size':'20px', 'textAlign':'left','font-weight':'bold'}),
                        dbc.Row([
                            dbc.Col([
                                html.Div(('- It is a rechargeable cell with electrochemical reaction reversible by applying the reverse current. Discharge involves converting chemical energy to electricity while the reverse happens upon charge.'), 
                                 style={'textAlign':'justify', 'margin-left':'20px', 'font-size':'16px'}),
                                html.Br(),
                                html.Div(html.Img(src='https://dl.dropboxusercontent.com/scl/fi/a9szr5hl3pr3b9asxfnvj/Secondary-battery.png?rlkey=4ml8tm823ezvmqphn8z5co9qf&st=4f61y4f3&raw=1', style={"width":"80%", "display": "block", "margin": "auto", "justify-content":"center"})), 
                            ], width={"size": 5},
                            xs=12, sm=10, md=6, lg=5, xl=5
                            ),
                            dbc.Col([
                                dash_table.DataTable(
                                markdown_options={"html": True},
                                style_table={'overflowX': 'scroll'},
                                style_cell={'font-family': 'Arial', 'font-size': '14px','text-align':'left', 'margin-top':'10px'}, 
                                style_data={
                                        'whiteSpace': 'pre-wrap',
                                        'color': 'black',
                                        'backgroundColor': 'white',
                                        'height':'auto',
                                        'lineheight':'15px',
                                },
                                style_data_conditional=[
                                {
                                    'if': {'row_index': 'odd'},
                                    'backgroundColor': 'rgb(220, 220, 220)',
                                },
                                {
                                    'if': {'column_id': ''},
                                    'fontWeight': 'bold', 
                                },
                                ],
                                style_header={
                                    'backgroundColor': 'rgb(210, 210, 210)',
                                    'color': 'black',
                                    'fontWeight': 'bold',
                                    'font-size': '14px',
                                    'whiteSpace': 'pre-wrap',
                                },
                                data=df2.to_dict('records'),
                                columns=[{'id': c, 'name': c, "presentation": "markdown"} for c in df2.columns]
                            ),                                    
                            ], width={"size": 7},
                            xs=10, sm=8, md=8, lg=8, xl=7
                            ),
                            ]
                            ),
                        ],
                        style={"margin-bottom":"20px"}
                        ),
                        html.Br(),
                        ],style={'textAlign':'justify', 'margin-top':'0px'},
                        ), 
                    html.Br(),
             ],
             style={'textAlign':'justify', 'margin-left':'10px', 'margin-right':'10px'},
             ),
             html.Div(id='Options-content'),
    ])

#@callback(
#    Output('Options-content', 'children'),
#    [Input('Options', 'value')]
#)
#def update_output(value):
#    if value is None:
#        raise PreventUpdate
#    return f'You have selected {value}'