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
            "",
            [
                "Cathode areal capacity (mAh/cm<sup>2</sup>)",
                "Anode Areal Capacity (mAh/cm<sup>2</sup>)",
                "N/P Ratio",
                "Electrolyte weight/Cell Capacity (g/Ah)",
                "Average cathode thickness (um)",
                "Average anode thickness (um)",
                "Electrode porosity (%)",
                "Reference",
            ], 
        ),
        (
            "Coin Cell 2032 (Lab, <10mAh) (Li metal)",
            [
                "&lt;1", 
                "&gt;50", 
                "&gt;50",
                "&gt;70",
                "&lt;60",
                "&gt;250",
                "&gt;40",       
                "Jun Liu, et al., “Pathways for practical high-energy long-cycling lithium metal batteries”, Nature Energy, 4, 180 (2019)"      
            ],
        ),
        (
            "Pouch Cell (Lab, 1Ah) (NCM622/Li)", 
            [
                "3.5", 
                "10",
                "2.86",
                "3",
                "67",
                "50",
                "34",
                "Shuru Chen, et al., “Critical Parameters for Evaluating Coin Cells and Pouch Cells of Rechargeable Li-metal Batteries”, Joule, 3, 1094-1105 (2019)"
            ]
        ),
        (
            "Li-ion pouch cell (VW ID.3, 78Ah) (NCM622-811/Gr)",
            [
                "5.02",
                "5.23",
                "1.04",
                "0.95",
                "87.3",
                "115.3",
                "22",
                "F. J. Günter, et al., “State of the Art of Lithium-Ion Pouch Cells in Automotive Applications: Cell Teardown and Characterization”, J. Electrochem. Soc., 169, 030515 (2022)"
            ],
        ),
        (
            "Panasonic NCR18650B, 3.3 Ah (NCA/Gr)",
            [
                "4.93",
                "4.97",
                "1.01",
                "~1.3",
                "82.5",
                "95",
                "",
                "Markus Hagen, et al., “Lithium-Sulfur Cells: The Gap between the State-of-the-Art and the Requirements for High Energy Battery Cells”, Adv. Energy Mater., 5, 1401986 (2015)"
            ],
        ),
        (
            "Tesla 4680, 22 Ah (NCM811/Gr)",
            [
                "4.9",
                "5.5",
                "1.12",
                "",
                "~65",
                "~135",
                "",
                "Manuel Ank, et al., “Lithium-Ion Cells in Automotive Applications: Tesla 4680 Cylindrical Cell Teardown and Characterization”, J. Electrochem. Soc., 170, 120536 (2023) \n\n  https://insideevs.com/news/598656/tesla-4680-battery-cell-specs/"
            ],
        ),
        (
            "Tesla Prismatic, 161.5 Ah (LFP/Gr)",
            [
                "3.44",
                "3.66",
                "1.06",
                "",
                "94",
                "71",
                "32",
                "Sandro Stock, et al., “Cell teardown and characterization of an automotive prismatic LFP battery”, Electrochim. Acta, 471, 143341 (2023)"
            ],
        ),
    ],
)

dt = pd.DataFrame(data_election)

data_election2 = OrderedDict(
    [
        (
            "Areal capacity (mAh/cm2)",
            [
                "0.45",
                "2.5",
                "3.8",
                "1.4",
                "3.7",
                "3.8",
                "3.5",
            ], 
        ),
        (
            "Li thickness (um)",
            [
                "250", 
                "50", 
                "250",
                "50",
                "50",
                "250",
                "50",       
            ],
        ),
        (
            "N/P Ratio", 
            [
                "111", 
                "4",
                "13",
                "7.1",
                "2.7",
                "13",
                "2.9",
           ]
        ),
        (
            "Electrolyte weight/Cell Capacity (g/Ah)",
            [
                "210",
                "35",
                "25",
                "60",
                "25",
                "3",
                "3",
            ],
        ),
        (
            "Cycle life",
            [
                "&gt;300",
                "73",
                "62",
                "37",
                "15",
                "12",
                "12",
          ],
        ),
        (
            "Current Rate (mAh/cm2)",
            [
                "0.9",
                "0.5",
                "0.76",
                "0.28",
                "0.74",
                "0.76",
                "0.7",
           ],
        ),
    ],
)

dt2 = pd.DataFrame(data_election2)

layout = html.Div([  
            dbc.Row([
                dbc.Row([
                    dcc.Markdown('- Academic-to-Industry', style={'font-size':'30px', 'font-weight':'bold','margin-bottom':'20px'},),
                    dbc.Col([                      
                            dcc.Markdown(('- There is a clear technological gap and lack of the bridge between academic research and industry requirements. Academic research uses the testing parameters and conditions that are way off from those that are adopted in commercial cell manufacturing. Adjusting key metrics including cathode/anode active loading, N/P ratio, and electrolyte amounts to the industrial demand is not the primary target in academia as its focus is not on reducing the cost but, instead, much on materials discovery and cell performance enhancement, which can be realized quite frequently through small cell assembly and testing. For EV battery suppliers and automative OEMs who need to meet requirements/demands on safety, cell energy density and power capability, it is also inevitable to think about the cost and energy consumption for manufacturing and hence are keen on making improvement in those metrics.'), 
                                 style={'textAlign':'justify', 'margin-left':'20px', 'font-size':'18px'}),
                        ],
                    width={"size": 7},
                    xs=9, sm=12, md=12, lg=6, xl=7
                    ),
                    dbc.Col([
                        html.Div( html.Img(src='https://www.dropbox.com/scl/fi/rpitq4tea2jdczua3un9b/industry_academia.png?rlkey=wxshe0dl8i9uhxlypfxuu4j3l&raw=1', style={"width":"100%", "display":"block", "margin-bottom":"20px"}), 
                        ),
                        ], width={"size": 5},
                        xs=7, sm=10, md=8, lg=6, xl=5
                    ),   
                    dcc.Markdown(('- A table below shows how different are the research lab test metrics from those in the industry setting. The columns highlighted in pink/blue are those from the labs/industry.'), 
                            style={'textAlign':'justify', 'margin-left':'20px', 'font-size':'18px'}),      
                ]),             
                html.Br(),
                html.Br(),
                dcc.Markdown(('- Table of comparison between cells tested in the lab scale vs manufactured in the industry'), 
                                 style={'textAlign':'justify', 'margin-left':'0px', 'font-size':'20px', 'font-weight':'bold'}),      
                dbc.Row([
                    dash_table.DataTable(
                                style_cell={'font-family': 'Arial', 'font-size': '16px', 'text-align':'center', 'minWidth': '180px', 'width': '180px', 'maxWidth': '180px', 'margin-top':'10px', 'padding':2}, 
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
                                    'if': {'column_id': 'Coin Cell 2032 (Lab, <10mAh) (Li metal)'},
                                    'backgroundColor': 'rgb(255, 197, 209)', 'padding-left':'10px'
                                },
                                {
                                    'if': {'column_id': 'Pouch Cell (Lab, 1Ah) (NCM622/Li)'},
                                    'backgroundColor': 'rgb(255, 197, 209)', 'padding-left':'10px'
                                },
                                {
                                    'if': {'column_id': ''},
                                    'fontWeight':'bold',
                                },
                                {
                                    'if': {'column_id': 'Li-ion pouch cell (VW ID.3, 78Ah) (NCM622-811/Gr)'},
                                    'backgroundColor': 'rgb(77, 188, 238)', 'padding-left':'10px'
                                },
                                {
                                    'if': {'column_id': 'Panasonic NCR18650B, 3.3 Ah (NCA/Gr)'},
                                    'backgroundColor': 'rgb(77, 188, 238)', 'padding-left':'10px'
                                },
                                {
                                    'if': {'column_id': 'Tesla 4680, 22 Ah (NCM811/Gr)'},
                                    'backgroundColor': 'rgb(77, 188, 238)', 'padding-left':'10px'
                                },
                                {
                                    'if': {'column_id': 'Tesla Prismatic, 161.5 Ah (LFP/Gr)'},
                                    'backgroundColor': 'rgb(77, 188, 238)', 'padding-left':'10px'
                                },
                                ],
                                style_header={
                                    'whiteSpace': 'normal',
                                    #'backgroundColor': 'rgb(210, 210, 210)',
                                    'backgroundColor': 'black',
                                    'color': 'white',
                                    'fontWeight': 'bold',
                                    'font-size': '18px',
                                    'text-align':'center',
                                },
                                data=dt.to_dict('records'),
                                columns=[{'id': c, 'name': c,"presentation": "markdown"} for c in dt.columns],
                    ),
                ], style={'margin-bottom':'20px'},
                ),
                html.Br(),
                html.Br(),
                dcc.Markdown(('- As shown in the table above, in the research lab, a thinner cathode is often preferred over the thicker one (especially when uncalendared) for coin cell tests to display high capacity with good reversibility by preventing possible polarization and minimizing the degree of Li stripping and deposition.  Further, putting an excessive amount of electrolyte during the coin cell assembly translates to good cycle performance without any concern of electrolyte drying that leads to rapid capacity decay. Although these measures make the data more appealing for publication, these are far from being practical in the industrial perspective owing to the loss of cell energy density.'), 
                                 style={'textAlign':'justify', 'margin-left':'20px', 'font-size':'18px'}),    
                dcc.Markdown(('* The table below reveals that increasing the cathode coating, reducing Li thickness, and reducing the electrolyte amount is detrimental to capacity retention of the cell.'), 
                                 style={'textAlign':'justify', 'margin-left':'20px', 'font-size':'18px'}), 
                html.Br(),
                dcc.Markdown(('- Influence of metrics on the coin cell (Li/NCM622) cycle performance'), 
                                 style={'textAlign':'justify', 'margin-left':'0px', 'font-size':'20px', 'font-weight':'bold'}),                                   
                dash_table.DataTable(
                                style_cell={'font-family': 'Arial', 'font-size': '16px', 'text-align':'center', 'minWidth': '180px', 'width': '180px', 'maxWidth': '180px', 'margin-top':'10px', 'padding':2}, 
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
                                    'if': {'column_id': 'Coin Cell 2032 (Lab) (Li metal)'},
                                    'backgroundColor': 'rgb(255, 197, 209)', 'padding-left':'10px'
                                },
                                {
                                    'if': {'column_id': 'Pouch Cell (Lab, 1Ah) (NCM622/Li)'},
                                    'backgroundColor': 'rgb(255, 197, 209)', 'padding-left':'10px'
                                },
                                {
                                    'if': {'column_id': ''},
                                    'fontWeight':'bold',
                                },
                                {
                                    'if': {'column_id': 'Li-ion pouch cell (VW ID.3, 78Ah) (NCM622-811/Gr)'},
                                    'backgroundColor': 'rgb(77, 188, 238)', 'padding-left':'10px'
                                },
                                {
                                    'if': {'column_id': 'Panasonic NCR18650B, 3.3 Ah (NCA/Gr)'},
                                    'backgroundColor': 'rgb(77, 188, 238)', 'padding-left':'10px'
                                },
                                {
                                    'if': {'column_id': 'Tesla 4680, 22 Ah (NCM811/Gr)'},
                                    'backgroundColor': 'rgb(77, 188, 238)', 'padding-left':'10px'
                                },
                                {
                                    'if': {'column_id': 'Tesla Prismatic, 161.5 Ah (LFP/Gr)'},
                                    'backgroundColor': 'rgb(77, 188, 238)', 'padding-left':'10px'
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
                                data=dt2.to_dict('records'),
                                columns=[{'id': d, 'name': d,"presentation": "markdown"} for d in dt2.columns],
                            ),
                dcc.Markdown(('* The data from the following paper: Shuru Chen, et al., "Critical Parameters for Evaluating Coin Cells and Pouch Cells of Rechargeale Li-Metal Batteries", 3, 1094 (2019)'), 
                                 style={'textAlign':'justify', 'margin-left':'0px', 'font-size':'12px', 'font-style':'italic'}),    
                html.Br(),                       
                html.Br(),
                dcc.Markdown(('- Will finding the new cathode material be the solution?'), 
                                 style={'textAlign':'justify', 'margin-left':'0px', 'font-size':'20px', 'font-weight':'bold'}),  
                html.Br(),
                dcc.Markdown(('- One metric to improve the cell performance is increasing the cathode areal capacity. Apparently, simply increasing the coathing thickness will not do the job due to an increase in polarization and low material utilization. Hence, finding a new cathode system with high specific capacity is desirable, but this cannot easily be realized.'), 
                                 style={'textAlign':'justify', 'margin-left':'20px', 'font-size':'18px'}),    
                dbc.Row([
                    dbc.Col([                      
                               html.Div( html.Img(src='https://www.dropbox.com/scl/fi/op512yfz60irl6hc1te6f/LFPvsNCA.png?rlkey=4hcmb8tdnwq73lyfy74jfy0em&st=x4ql2qx7&raw=1', style={"width":"100%", "display":"block", "margin-bottom":"20px"}), 
                        ),
                        ],
                            width={"size": 5},
                            xs=9, sm=12, md=12, lg=6, xl=5
                            ),
                    dbc.Col([
                                 dcc.Markdown(('- The perspective article by Frith et al., shows nicely the graphical comparison of performance between the cells consisting of NCA/Graphite-SiOx and LFP/Graphite from theoretical estimation to the pack assembly level. (see the graph on the left.) At the theory level, the differences between the cells in both gravimetric (699 Wh/kg vs. 373 Wh/kg) and volumetric energy densities (2391 Wh/L vs. 1100 Wh/L) are huge; NCA/Graphite-SiOx outperforms LFP/Graphite by almost double. However, the margin is gradually reduced during various stages of implementation- ultimately the energy densities are almost the same as each other after considering reversibility, lifetime, proportion of inactive components, and cell-to-pack technology.'), 
                                 style={'textAlign':'justify', 'margin-left':'20px', 'font-size':'18px'}),
                                 html.Br(),
                                 dcc.Markdown(('**Reference**: James T Frith, et al., "A non-academic perspective on the future of lithium-based batteries",_**Nature Commun.**_, 14, 420 (2023)'), 
                                 style={'textAlign':'justify', 'margin-left':'20px', 'font-size':'18px'}),                                 
                            ], width={"size": 7},
                            xs=7, sm=12, md=12, lg=6, xl=7
                            ),
                        ]
                ),                      
            ],
            style={'textAlign':'justify', 'margin-left':'30px', 'margin-right':'30px'},
        ),
        html.Div(id='Options-content'),
        ],
    )
    
