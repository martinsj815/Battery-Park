import os
import numpy as np
import dash
import pandas as pd
from dash import Dash, dash_table, dcc, html, Input, Output, State, callback
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
import plotly.express as px
import dash_mantine_components as dmc
from collections import OrderedDict
from dash.exceptions import PreventUpdate

dash.register_page(
    __name__, name="basics", top_nav=True, path="/basics-sd"
    )

#dash.register_page(__name__, name="basics", top_nav=False)

data_election = OrderedDict(
    [
        (
            "Cell component",
            [
                "Electrodes",
                "Current collectors",
                "Separator",
                "Electrolyte",
                "Tabs",
            ], 
        ),
        (
            "Energy Cell",
            [
                "High coating density & thickness \n High active material loading percentage \n Low porosity", 
                "Thinner - Improved adhesion", 
                "Thin",
                "High ionic conductivity",
                "Thin/Narrow/A few tabs on each electrode (weight consideration)",         
            ],
        ),
        (
            "Power Cell", 
            [
                "Low coating density & thickness \n Low active material loading percentage \n High porosity", 
                "Thicker - Lower resistance", 
                "Thin",
                "High ionic conductivity",
                "Thick/Wide/Multiple tabs on each electrode (smoother ion transport)",      
            ]
        ),
    ],
)

data_electionII = OrderedDict(
    [
        (
            "Anode Type",
            [
                "Graphite",
                "Li<sub>4</sub>Ti<sub>5</sub>O<sub>12</sub>(LTO)",
                "Si",
                "Li metal",
            ], 
        ),
        (
            "N/P ratio",
            [
                " N/P > 1 ", 
                " N/P < 1 ", 
                " 1 < N/P < 2 ",
                " N/P ~ 1 ",        
            ],
        ),
        (
            "Comments", 
            [
                "- An excess cathode can cause excess lithium ions to deposit on the anode surface during charging, forming dendrites. This reduces battery cycle performance and can lead to short circuits. Thus, an excess anode is benefical for preventing lithium deposition on the anode surface during overcharge, thereby improving cycle life and safety.\n\n -  E.g.: N/P ratio is 1.08 with NCM811 @ W. Zhao et al., Materials Today Energy, 34, 101301 (2023)", 
                "- LTO has a stable structure, high intercalation potential (1.55V vs Li/Li<sup>+</sup>), and excellent cycle performance, and does not exhibit lithium plating with excess lithium ions from the cathode. Therefore, designing cells with excess cathode capacity and limited anode capacity (N/P < 1) can mitigate electrolyte degradation due to a high cathode potential when the battery is near or at full charge. \n\n - E.g.: N/P ratio is 0.68 with NCM111 @ 'Comprehensive guide to battery cathode and anode capacity design', 2022, tycorun.com ", 
                "- If the anode is highly overbalanced, only a small amount of silicon will be lithiated, resulting in a high anode potential at the end of charge. To reach the same full cell voltage, the cathode material may be overcharged, accelerating degradation due to side reactions in the cathode or electrolyte depletion.\n\n - E.g.: NP ratio is 1.15-1.4 with NCM811 @ F. Reuter et al., Journal of The Electrochemical Society, 166, 14, A3265-A3271 (2019)  ",
                "- A thick Li metal anode (N/P > 2.5) provides a stable initial cycle. However, continued cycling leads to a thick SEI layer build-up, increasing cell polarization. When this becomes dominant, it results in electrolyte depletion and a sudden drop in capacity. Conversely, for N/P ratio close to 1, which effectively balances the lithium consumption rate, electrolyte depletion rate, and SEI accumulation rate under realistic conditions, cell polarization is minimized, extending cell cycle life. \n\n - E.g.: N/P ratio is 1 with NMC622 @ C. Niu et al., Nature Energy, 6, 723-732 (2021)",
                
            ]
        ),
    ],
)

dt = pd.DataFrame(data_election)
dtII = pd.DataFrame(data_electionII)


layout = html.Div([
             dbc.Row([
                dbc.Col([
                    dbc.Row([
                        dcc.Markdown('* N/P Ratio', style={'font-size':'25px', 'textAlign':'left','font-weight':'bold'}),
                        html.Div("The N/P ratio is a crucial cell design parameter that can influences the utilization level of the electrodes, thereby affecting overall performance and cell-level energy density. The N/P ratio represents the capacity ratio between the anode and cathode. The optimal N/P ratio depends on the electrode's electrochemical reaction mechanism, reaction efficiency, and the decay rate of the cathode and anode during cycling. This parameter must be optimized based on the operating environment.", 
                                  style={'textAlign':'justify', 'margin-left':'20px', 'font-size':'18px', 'margin-bottom':'20px'}),
                
                        dash_table.DataTable(
                                style_cell={'font-family': 'Arial', 'font-size': '14px', 'text-align':'auto', 'margin-top':'auto', 'padding':2}, 
                                markdown_options={"html": True},
                                #virtualization=True,
                                style_table={'overflowX': 'auto','margin-left':'20px'},
                                style_data={
                                        'whiteSpace': 'normal',
                                        'color': 'black',
                                        'backgroundColor': 'white',
                                        'height':'auto',
                                        'lineheight':'10px',
                                },
                                style_data_conditional=[
                                {
                                    'if': {'column_id': 'Anode Type'},
                                    'fontWeight': 'bold', 

                                },
                                {
                                    'if': {'column_id': 'N/P ratio'},
                                    'width': '90px', 
                                },
                                ],
                                style_header={
                                    'whiteSpace': 'normal',
                                    'backgroundColor': 'black',
                                    'color': 'white',
                                    'fontWeight': 'bold',
                                    'font-size': '14px',
                                    'text-align':'center'
                                },
                                data=dtII.to_dict('records'),
                                columns=[{'id': c, 'name': c,"presentation": "markdown"} for c in dtII.columns],
                                ),
                    ],),
                    html.Br(),
                    dmc.Divider(size="md", color="grey"),
                    html.Br(),                   
                    dbc.Row([

                        dcc.Markdown('* Cell connection layout (mS-nP)', style={'font-size':'25px', 'textAlign':'left','font-weight':'bold'}),
                        dbc.Col([
                         html.Div('- For high-voltage packs, cells are connected in series to form a series-connected module (SCM).', style={'textAlign':'justify', 'margin-left':'20px', 'font-size':'18px'}),
                         dcc.Markdown(dangerously_allow_html=True, mathjax=True, children=("$$v_{pack}=m_{series}*v_{cell}$$"), style={'text-align':'center','font-size':'120%'}),
                         html.Div('- For high-current packs, cells are connected in parallel to form a parallel-connected module (PCM). Capacity scales with the number of cells in parallel.', style={'textAlign':'justify', 'margin-left':'20px', 'font-size':'18px'}),
                         dcc.Markdown(dangerously_allow_html=True, mathjax=True, children=("$$i_{pack}=n_{parallel}*i_{cell}$$"), style={'text-align':'center','font-size':'120%'}),
                         html.Div('- Total internal resistance of the pack can be estimated from the cell assuming the same open-circuit voltage and internal resistance:', style={'textAlign':'justify', 'margin-left':'20px', 'font-size':'18px'}),
                         dcc.Markdown(dangerously_allow_html=True, mathjax=True, children=("$$R_{pack}=\\frac{m_{series}}{n_{parallel}}*R_{cell}$$"), style={'text-align':'center','font-size':'120%'}),
                         html.Div('- Total pack energy and power can also be calculated:', style={'textAlign':'justify', 'margin-left':'20px', 'font-size':'18px'}),
                         dcc.Markdown(dangerously_allow_html=True, mathjax=True, children=("$$E_{pack}=m_{series}*n_{parallel}*Q_{cell}*v_{cell}$$"), style={'text-align':'center','font-size':'120%'}),
                         dcc.Markdown(dangerously_allow_html=True, mathjax=True, children=("$$P_{pack}=m_{series}*n_{parallel}*i_{cell}*v_{cell}$$"), style={'text-align':'center','font-size':'120%'}),
                         ], width={"size": 7},
                         xs=12, sm=10, md=10, lg=7, xl=7
                         ), 
                        dbc.Col([
                        html.Div( html.Img(src='https://dl.dropboxusercontent.com/scl/fi/jg6c9nt6e178rvwqgzmn1/Cell-in-Series-and-Parallel.png?rlkey=jx3kgx1r043llbnv0ewrfiykh&raw=1', style={"width":"140%"}), 
                                 ),
                        ], width={"size": 4},
                        xs=8, sm=8, md=6, lg=3, xl=3
                        ),
                    ],),
                    html.Br(),
                    dmc.Divider(size="md", color="grey"),
                    html.Br(),
                    dbc.Row([
                        dcc.Markdown('* Designing cell: Energy density vs Power capability?', style={'font-size':'25px', 'textAlign':'left','font-weight':'bold'}),
                        dbc.Col([
                        html.Div('- When designing the cell, the trade-off between energy density and power capability needs to be considered as both cannot go hand in hand. To increase the cell energy density, thicker and denser coating (i.e. higher material loading density) is needed for each electrode layer to store more energy. However, increasing the loading can engender many issues that raise the cell’s internal resistance including concentration polarization and uneven thermal distribution with possible ohmic heating. That is because low porosity, high tortuosity, and high thickness all translate to longer diffusion length of Li ions and possible bottleneck for Li flow in and out the cell. Hence power, which is the measure of how fast the energy can be driven in and out the electrode, is inevitably low for these cells.', style={'textAlign':'justify', 'margin-left':'20px','font-size':'18px'}),
                        html.Br(),
                        dash_table.DataTable(
                                style_cell={'font-family': 'Arial', 'font-size': '15px', 'text-align':'center', 'minWidth': '160px', 'width': '160px', 'maxWidth': '160px', 'margin-top':'10px', 'padding':2}, 
                                markdown_options={"html": True},
                                style_table={'overflowX': 'auto'},
                                style_data={
                                        'whiteSpace': 'normal',
                                        'color': 'black',
                                        'backgroundColor': 'white',
                                        'height':'auto',
                                        'lineheight':'5px',
                                },
                                style_data_conditional=[
                                {
                                    'if': {'column_id': 'Cell component'},
                                    'fontWeight': 'bold',
                                },
                                ],
                                style_header={
                                    'whiteSpace': 'normal',
                                    #'backgroundColor': 'rgb(210, 210, 210)',
                                    'backgroundColor': 'black',
                                    'color': 'white',
                                    'fontWeight': 'bold',
                                    'font-size': '16px',
                                    'text-align':'center',
                                },
                                data=dt.to_dict('records'),
                                columns=[{'id': c, 'name': c,"presentation": "markdown"} for c in dt.columns],
                        ),
                        ], width={"size": 7}, style={"margin-right":"10px"},
                       xs=12, sm=10, md=10, lg=8, xl=7
                       ), 
                        dbc.Col([
                        html.Div( html.Img(src='https://dl.dropboxusercontent.com/scl/fi/17gyxolvyjlaws7ksxw1m/power-vs-energy.png?rlkey=bikeko9bn4y6vehbhjv7aox8e&st=92q02hgo&raw=1', style={"width":"100%"}), 
                                 ),
                        ], width={"size": 4},
                        xs=8, sm=8, md=8, lg=5, xl=4
                        ),
                    ],),
                    html.Br(),
                    html.Br(),
                    dmc.Divider(size="md", color="grey"),
                    html.Br(),
                    dcc.Markdown(('* Reference'), style={'textAlign':'justify', 'margin-left':'0px', 'font-size':'20px', 'font-weight':'bold'}),
                   dcc.Markdown(('Michael J. Lain, et al., "Design Strategies for High Power vs. High Energy Lithium Ion Cells", _**batteries**_, 5, 64 (2019)'), style={'textAlign':'justify', 'margin-left':'0px', 'font-size':'18px'}),
                ],),
             ],
             style={'textAlign':'justify', 'margin-left':'30px', 'margin-right':'30px'},
             ),
             html.Div(id='Options-content'),
    ])