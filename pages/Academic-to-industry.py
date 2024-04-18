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

layout = html.Div([
                html.Link(rel='stylesheet', href='/assets/table.css'),      
            dbc.Row([
                dbc.Col([
                    dbc.Row([
                        dcc.Markdown('- Academic-to-Industry', style={'font-size':'30px', 'font-weight':'bold','margin-bottom':'20px'},),
                        dbc.Col([                      
                            dcc.Markdown(('- There is a clear technological gap between academic research and industry requirements. Academic research uses the testing parameters and conditions that are way off from those that are adopted in commercial cell manufacturing. Adjusting key metrics including cathode/anode active loading, N/P ratio, and electrolyte amounts to the industrial demand is not the primary target in academia as its focus is much on materials discovery and cell performance enhancement, which can be realized quite frequently through small cell assembly and testing. For EV battery suppliers and automative OEMs who need to meet requirements/demands on safety, cell energy density and power capability, it is also inevitable to think about the cost and energy consumption for manufacturing and hence are keen on making improvement in those metrics.'), 
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
                    ]),   
                    dcc.Markdown(('- A table below shows how different are the research lab test metrics from those in the industry setting. The columns highlighted in pink/blue are those from the labs/industry.'), 
                                 style={'textAlign':'justify', 'margin-left':'20px', 'font-size':'18px'}),                     
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
                                data=dt.to_dict('records'),
                                columns=[{'id': c, 'name': c,"presentation": "markdown"} for c in dt.columns],
                        ),
                        html.Br(),
                        html.Br(),
                        dcc.Markdown(('- As shown in the table above, in the research lab, a thinner cathode is often preferred over the thicker one (especially when uncalendared) for coin cell tests to display high capacity with good reversibility by preventing possible polarization and minimizing the degree of Li stripping and deposition.  Further, putting an excessive amount of electrolyte during the coin cell assembly translates to good cycle performance without any concern of electrolyte drying that leads to rapid capacity decay. Although these measures make the data more appealing for publication, these are far from being practical in the industrial perspective owing to the loss of cell energy density.'), 
                                 style={'textAlign':'justify', 'margin-left':'20px', 'font-size':'18px'}),    
                        ],style={'textAlign':'justify', 'margin-left':'30px', 'margin-right':'30px'},
                width={"size": 16},
                xs=5, sm=10, md=10, lg=10, xl=16,
                ), 
                ]),
                html.Div(id='Options-content'),
        ])
