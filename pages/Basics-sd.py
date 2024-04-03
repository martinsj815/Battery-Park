import os
import numpy as np
import dash
from dash import Dash, dcc, html, Input, Output, State, callback
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
import plotly.express as px
import dash_mantine_components as dmc
from dash.exceptions import PreventUpdate

dash.register_page(
    __name__, name="basics", top_nav=True, path="/basics-sd"
    )

#dash.register_page(__name__, name="basics", top_nav=False)

layout = html.Div([
             dbc.Row([
                dbc.Col([
                    dbc.Row([
                        dcc.Markdown('* N/P Ratio', style={'font-size':'25px', 'textAlign':'left','font-weight':'bold'}),
                        dbc.Col([
                         html.H5('- By setting the ratio between the areal capacity of the anode and cathode for the different cycle rates, cell performance can be optimized. Typically, anodes are designed in a way to both have a higher areal capacity and a larger geometry/dimension than those of the cathode to lessen lithium metal plating and avoid high current density on the edge and thus the overlap effect (i.e. lithium plating). N/P ratio of 1-1.2 is commonly used in literature.', style={'textAlign':'justify', 'margin-left':'20px'}),
                      ], width={"size": 7},
                         xs=12, sm=10, md=10, lg=7, xl=7
                         ), 
                        dbc.Col([
                        ], width={"size": 4},
                        xs=8, sm=8, md=6, lg=3, xl=3
                        ),
                    ],),
                    html.Br(),
                    dmc.Divider(size="md", color="grey"),
                    html.Br(),                   
                    dbc.Row([

                        dcc.Markdown('* Cell design specifications', style={'font-size':'25px', 'textAlign':'left','font-weight':'bold'}),
                        dbc.Col([
                         html.H5('- For high-voltage packs, cells are connected in series to form a series-connected module (SCM).', style={'textAlign':'justify', 'margin-left':'20px'}),
                         dcc.Markdown(dangerously_allow_html=True, mathjax=True, children=("$$v_{pack}=n_{series}*v_{cell}$$"), style={'text-align':'center','font-size':'120%'}),
                         html.H5('- For high-current packs, cells are connected in parallel to form a parallel-connected module (PCM). Capacity scales with the number of cells in parallel.', style={'textAlign':'justify', 'margin-left':'20px'}),
                         dcc.Markdown(dangerously_allow_html=True, mathjax=True, children=("$$i_{pack}=n_{parallel}*i_{cell}$$"), style={'text-align':'center','font-size':'120%'}),
                         html.H5('- Total internal resistance of the pack can be estimated from the cell assuming the same open-circuit voltage and internal resistance:', style={'textAlign':'justify', 'margin-left':'20px'}),
                         dcc.Markdown(dangerously_allow_html=True, mathjax=True, children=("$$R_{pack}=\\frac{n_{series}}{n_{parallel}}*R_{cell}$$"), style={'text-align':'center','font-size':'120%'}),
                         html.H5('- Total pack energy and power can also be calculated:', style={'textAlign':'justify', 'margin-left':'20px'}),
                         dcc.Markdown(dangerously_allow_html=True, mathjax=True, children=("$$E_{pack}=n_{series}*n_{parallel}*Q_{cell}*v_{cell}$$"), style={'text-align':'center','font-size':'120%'}),
                         dcc.Markdown(dangerously_allow_html=True, mathjax=True, children=("$$P_{pack}=n_{series}*n_{parallel}*i_{cell}*v_{cell}$$"), style={'text-align':'center','font-size':'120%'}),
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
                        dcc.Markdown('* Cell scaling', style={'font-size':'25px', 'textAlign':'left','font-weight':'bold'}),
                        dbc.Col([
                         html.H5('- The amount of electrochemically active material used in the cell or battery determines the magnitude of its capacity. The volume of the electrode is proportional to the capacity of its material by a following relation:', style={'textAlign':'justify', 'margin-left':'20px'}),
                         dcc.Markdown(dangerously_allow_html=True, mathjax=True, children=("$$V_{electrode}=\\frac{3600*Q*M_{w}}{F*\\rho}$$"), style={'text-align':'center','font-size':'150%'}),
                         html.H5('- Since the separator covers the areas of the cathode and anode, nominal current density can be denoted as:', style={'textAlign':'justify', 'margin-left':'20px'}),
                         dcc.Markdown(dangerously_allow_html=True, mathjax=True, children=("$$i_{cell}=\\frac{Q}{t_{d}*A_{sep}}$$"), style={'text-align':'center','font-size':'150%'}),
                         html.H5(children=[html.Span('- Increasing the cell capacity requires increasing the cell volume - increasing the cell thickness or area (or both). When increasing the electrode thickness without changing their areas, current density will be doubled'), html.Strong(' (Case 1)'), html.Span('. This however increases the cell polarization and leads to a lower effective capacity as the cell discharge reaches the cutoff voltage sooner.')], style={'textAlign':'justify', 'margin-left':'20px'}),
                         html.H5(children=[html.Span('- What about increasing the area of the cell to increase its capacity while keeping other parameters the same '), html.Strong('(Case 2)'), html.Span('? Average density is constant as the area of the separator scales with the capacity. Increasing capacity now requires a larger volume change as the separator (and other relevant) volumes also change.')], style={'textAlign':'justify', 'margin-left':'20px'}),
                         html.H5('- This is still not in a desirable way to increase cell capacity since the resistance (i.e. current collectors) goes up as the area increases. Why so? Increase in the area of the current collector means a larger distance the tab is from the entire current collector area.' , style={'textAlign':'justify', 'margin-left':'20px'}),
                       ], width={"size": 8},
                       xs=12, sm=10, md=10, lg=8, xl=8
                       ), 
                        dbc.Col([
                        html.Div( html.Img(src='https://dl.dropboxusercontent.com/scl/fi/8sk0h6a60izh3g7nfzfie/Cell-optimization.png?rlkey=mrx6n266cj1cvfyrlhcacoini&raw=1', style={"width":"100%"}), 
                                 ),
                        ], width={"size": 4},
                        xs=8, sm=8, md=8, lg=5, xl=3
                        ),
                    ],),
                    html.Br(),
                    html.Br(),
                    dbc.Row([
                        dbc.Col([
                        html.Div( html.Img(src='https://dl.dropboxusercontent.com/scl/fi/0jqhyz2iuwjgdom4qh9am/Multilayer-stack.png?rlkey=uy5rjrz0pqxt3uy7pqazarxd3&raw=1', style={"width":"100%"}), 
                                 ),
                        ], width={"size": 4},
                        xs=8, sm=8, md=8, lg=5, xl=3
                        ),
                        dbc.Col([
                        html.H5(children=[html.Span('- A better way to increase capacity is to stack multiple thinner electrodes such that the same electrode material is positioned on both sides of a current collector'), html.Strong(' (Case 3)'), html.Span('. Such addition of layers connected in parallel increases capacity while mitigating problems associated with the electrode size tuning.')], style={'textAlign':'justify', 'margin-left':'20px'}),
                       ], width={"size": 7},
                       xs=12, sm=10, md=10, lg=8, xl=8
                       ), 
                    ],),
                    html.Br(),
                    dmc.Divider(size="md", color="grey"),
                    html.Br(),
                ],style={'textAlign':'justify', 'margin-left':'30px', 'margin-right':'30px'},),
             ],),
             html.Div(id='Options-content'),
    ])