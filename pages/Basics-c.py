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
    __name__, name="basics", top_nav=True, path="/basics-c"
    )

#dash.register_page(__name__, name="basics", top_nav=False)
data_election = OrderedDict(
    [
        (
            "",
            [
                "Advantage",
                "Disadvantage",
                "Capacity (Ah)",
                "Manufacturer"
            ], 
        ),
        (
            "Cylindrical Cell",
            [
             "*Good thermal control / Mechanical stability \n *Automated Manufacturing Possible", 
             "*Low packaging density \n *Ancillary parts adding weights", 
             "3-25",
             "LG ES, Samsung SDI, SK On, Panasonic, Verkor"
             ],
        ),
        (
            "Prismatic Cell", 
            ["*Good battery space utilization/packing density \n *Size flexibility", 
            "*Lack of standardized design \n*Manufacturing can be expensive",
            "100-300",
            "LG ES, Samsung SDI, CATL, Northvolt, BYD"]),
        (
        "Pouch Cell",
        [
                "*Light-weight: High energy density \n*Design flexible",
                "*Prone to damages due to lack of casing protection \n*Design limitation - Customization needed \n Stack pressure needed",
                "20-100",
                "LG ES, SK On, Verkor, Northvolt, BYD"],
                )
        ],
)

data_election2 = OrderedDict(
    [
        (
            "",
            [
                "Diameter (mm)",
                "Height (mm)",
                "Nominal Voltage (V)",
                "Max Capacity (mAh)",
                "Energy Density (Wh/kg)"
            ], 
        ),
        (
            "18650",
            [
             "18", 
             "65", 
             "3.6-3.7",
             "3450 (LG INR18650-M36) \n 3550 (Panasonic NCR18650G) \n 3350 (Samsung INR18650-36G)",
             "248 (LG INR18650-M36) \n 264 (Panasonic NCR18650G)"
             ],
        ),
        ("21700", 
         ["21", 
          "70",
          "3.6-3.7",
          "5000 (LG INR21700-M50) \n 5000 (Samsung INR21700-50E) \n 5000 (Panasonic NCR21700T)",
          "263 (LG CHEM INR21700-M50L) \n 261 (Samsung INR21700-50E) \n 271 (Panasonic NCR2170-M)"
          ]),
          
        (
        "4680",
        [
         "46",
         "80",
         "3.7 (estimate)",
         "~26000 (Tesla 4680, estimate)",
         "244 (Tesla 4680)",
         ],
                )
        ],
)

df = pd.DataFrame(data_election)
df2 = pd.DataFrame(data_election2)

layout = html.Div([
             dbc.Row([
                dbc.Col([
                    dbc.Row([
                        dcc.Markdown('* Electrochemical Cell', style={'font-size':'25px', 'textAlign':'left','font-weight':'bold'}),
                        dbc.Col([
                         html.Div(('- A cell is the smallest building unit of the battery. Main constituents are cathode and anode that are immersed in electrolyte and undergo reduction/oxidation. Cations migrate inside the electrolyte while electrons move through the external load to do the work.'), 
                                 style={'textAlign':'justify', 'margin-left':'20px', 'font-size':'20px'}),
                         html.Div(('- When a cell is discharged, cations and electrons from the negative electrode move towards the positive electrode, where the reduction takes place (while the negative electrode is oxidized). Different from the case of primary batteries, this process can be reversed through charging in secondary rechargeable batteries.'), 
                                 style={'textAlign':'justify', 'margin-left':'20px', 'font-size':'20px'}),
                         html.Div(('- Cells also include the separator that isolate the positive and negative electrodes to prevent the electron flow and permit only the ion flow and the current collectors - metal foils where the electrodes are attached and that conduct electrical current to the external circuit.'), 
                                 style={'textAlign':'justify', 'margin-left':'20px', 'font-size':'20px'}),
                        ], width={"size": 7},
                        xs=7, sm=10, md=10, lg=7, xl=7
                        ),
                        dbc.Col([
                            html.Div( html.Img(src='https://www.dropbox.com/scl/fi/hc0318st6fcb8hsk7kw11/cell-image.png?rlkey=uutzhyefy4uhb1sie5qdr6wpl&raw=1', style={"width":"100%", "display": "block", "margin": "auto", "align-items":"center", "justify-content":"center"}), 
                                 ),
                        ], width={"size": 5},
                        xs=8, sm=8, md=6, lg=5, xl=5
                        ),
                    ],),
                    html.Br(),
                    dmc.Divider(size="md", color="grey"),
                    html.Br(),
                    dbc.Row([
                        dbc.Col([                         
                            dcc.Markdown('* Cell Formats', style={'font-size':'25px', 'textAlign':'left','font-weight':'bold'}),
                            html.H5(('- Cells can be constructed in many different forms. These include button/coin-type, cylindrical, prismatic, and pouch-type.'), 
                                 style={'textAlign':'justify', 'margin-left':'20px'}),
                            html.Br(),
                            dmc.Divider(size="md", variant="dotted", color="black"),
                            html.Br(),
                            dbc.Row([
                                dbc.Col([
                                    html.H5(('1. Coin Cell'), 
                                    style={'textAlign':'justify', 'font-weight':'bold', 'margin-left':'30px'}),       
                                    html.Div(('- Coin cells are most commonly used in academic research and for the small consumer electronics parts such as watches and calculators. The electrodes divided by the separator are sealed inside the can with its top and bottom electrically isolated by the gasket. Coin cells have the dimension designation - 20xx, which means 20mm diameter x.x mm height. For example, CR2016 is 20mm in diameter and 1.6 mm in height.'), 
                                    style={'textAlign':'justify', 'margin-left':'50px', 'font-size':'18px'}),
                                    html.Div(('- Electrode thickness, spacer thickness, parts alignment are important for controlling both internal and external assembling pressure and acquiring good data with minimum cell-to-cell difference.'), 
                                    style={'textAlign':'justify', 'margin-left':'50px', 'font-size':'18px'}),
                                ], width={"size": 8},
                                xs=12, sm=10, md=10, lg=8, xl=8
                                ),
                                dbc.Col([
                                    html.Div( html.Img(src='https://dl.dropboxusercontent.com/scl/fi/03zylofuvvr3mtov6et4v/coin-cell2.png?rlkey=17pw4r0pqlqq00kpujh63yg0o&raw=1', style={"width":"100%"}), 
                                        ),
                                ], width={"size": 3},
                                xs=12, sm=12, md=6, lg=6, xl=3
                                ),
                            ],),
                            html.Br(),
                            dmc.Divider(size="md", variant="dotted", color="grey"),
                            html.Br(),
                            dbc.Row([
                                dbc.Col([
                                    html.H5(('2. Cylindrical Cell'), 
                                        style={'textAlign':'justify', 'font-weight':'bold', 'margin-left':'30px'}),       
                                    html.Div(('- In a cylindrical cell, anode, cathode, and separator sheets are rolled in spiral and packed in a cylindrical can. Typically, this cell has a lower casing designed for a negative terminal and a top protruded cap used for a positive terminal. Also included are +/- tabs, CID and PTC elements, to protect against current surge/shorting, and gasket. These types of cells are well produced to be also actively utilized in electric vehicles.'), 
                                        style={'textAlign':'justify', 'margin-left':'50px', 'font-size':'18px'}),
                                    html.Div(('- The three widely used dimensions for Li-ion battery cylindrical cells are 18650, 21700, and 4680, with which the first two digits correspond to the cell diameter and the next two digits correspond to its height (i.e. 18650 cell is 18 mm in diameter and 65 mm long.). A 4680 cell has the highest max capacity ~25,000 mAh and is currently used by Tesla in various car models including Model Y and Cybertrucks.'), 
                                        style={'textAlign':'justify', 'margin-left':'50px', 'font-size':'18px'}),
                                ], width={"size": 8},
                                xs=12, sm=10, md=10, lg=8, xl=8
                                ),
                                dbc.Col([
                                    html.Div( html.Img(src='https://www.dropbox.com/scl/fi/w0iv2jor01ppfoz2k92z9/Cylindrical-battery.png?rlkey=hxen2pb54yesl070le3r0wjw0&raw=1', style={"width":"100%"}), 
                                    ),
                                ], width={"size": 3},
                                xs=12, sm=12, md=6, lg=6, xl=3
                                ),
                            ],),
                            html.Br(),
                            dcc.Markdown(('* Cylindrical Cell Comparison'), 
                                    style={'textAlign':'justify', 'margin-left':'0px', 'font-size':'20px', 'font-weight':'bold'}),
                            dash_table.DataTable(
                                markdown_options={"html": True},
                                style_table={'overflowX': 'auto'},
                                style_cell={'font-family': 'Arial', 'font-size': '18px', 'text-align':'left', 'margin-top':'10px'}, 
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
                                    'color': 'blue',
                                    'fontWeight': 'bold',
                                    'font-size': '20px'
                                },
                                data=df2.to_dict('records'),
                                columns=[{'id': c, 'name': c, "presentation": "markdown"} for c in df2.columns]
                            ),
                            html.Br(),
                            html.Br(),
                            dmc.Divider(size="md", variant="dotted", color="grey"),
                            html.Br(),
                            dbc.Row([
                                dbc.Col([
                                    html.H5(('3. Prismatic Cell'), 
                                            style={'textAlign':'justify', 'font-weight':'bold', 'margin-left':'30px'}),       
                                    html.Div(('- Prismatic cells consist of the anode, cathode, and separator sheets that are rolled/pressed (“jelly-rolled”) or stacked to be placed inside the metal cuboid casing. These cells are used in many small (i.e. cell phone & laptop) to larger device and electric vehicle applications.'), 
                                            style={'textAlign':'justify', 'margin-left':'50px', 'font-size':'18px'}),
                                ], width={"size": 8},
                                xs=12, sm=10, md=10, lg=8, xl=8
                                ),
                                dbc.Col([
                                    html.Div( html.Img(src='https://www.dropbox.com/scl/fi/fngsptshttxmi7znxdie9/Prismatic-Cell2.png?rlkey=laa7f0j1y1i4mecx3dh1n1qwd&raw=1', style={"width":"100%"}), 
                                            ),
                                  ], width={"size": 3},
                                    xs=12, sm=12, md=6, lg=6, xl=3
                                    ),
                            ],),
                        html.Br(),
                        dmc.Divider(size="md", variant="dotted", color="grey"),
                        html.Br(),
                        dbc.Row([
                                dbc.Col([
                                    html.H5(('4. Pouch Cell'), 
                                        style={'textAlign':'justify', 'font-weight':'bold', 'margin-left':'30px'}),       
                                    html.Div(('- A pouch cell uses a flexible aluminum-coated foil for sealed enclosing of cathode, anode and separator layers that are stacked. Tabs are welded outside the cell for the electron transport. Since there is no rigid outside body casing, enough space should be given inside the cell in preparation for swelling during electrochemical cycling. Pouch cells are used in a wide variety of applications including consumer electronics and electric vehicles owing to their good adaptability, energy density, and lightweight.'), 
                                        style={'textAlign':'justify', 'margin-left':'50px', 'font-size':'18px'}),
                                ], width={"size": 8},
                                xs=12, sm=10, md=10, lg=8, xl=8
                                ),
                                 dbc.Col([
                                    html.Div( html.Img(src='https://www.dropbox.com/scl/fi/09mxpib7azoh9mfc95dds/Pouch-cell2.png?rlkey=p4km2g4bxqkxylan6cy1whdj5&raw=1', style={"width":"100%"}), 
                                    ),
                                ], width={"size": 3},
                                xs=12, sm=12, md=6, lg=6, xl=3
                                ),
                        ],),
                        html.Br(),
                        dmc.Divider(size="md", color="grey"),
                        html.Br(),
                        html.Br(),
                        dcc.Markdown('* Comparing Cell Formats (for EV Batteries)', style={'font-size':'25px', 'textAlign':'left','font-weight':'bold', 'margin-bottom':'40px'}),
                        dash_table.DataTable(
                                markdown_options={"html": True},
                                style_table={'overflowX': 'auto'},
                                style_cell={'font-family': 'Arial', 'font-size': '18px', 'text-align':'left', 'margin-top':'10px'}, 
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
                                    'fontWeight': 'bold', 
                                },
                                ],
                                style_header={
                                    'backgroundColor': 'rgb(210, 210, 210)',
                                    'color': 'blue',
                                    'fontWeight': 'bold',
                                    'font-size': '20px'
                                },
                                data=df.to_dict('records'),
                                columns=[{'id': c, 'name': c, "presentation": "markdown"} for c in df.columns]
                        ),
                        html.Br(),
                        ],style={'textAlign':'justify', 'margin-top':'0px'},
                        ), 
                    ]),
                    html.Br(),
                ],),
             ],
             style={'textAlign':'justify', 'margin-left':'30px', 'margin-right':'30px'},
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