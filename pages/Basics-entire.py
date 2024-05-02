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
    __name__, name="basics", top_nav=True, path="/basics-cp"
    )

#dash.register_page(__name__, name="basics", top_nav=False)

layout = html.Div([
             dbc.Row([
                dbc.Col([
                    html.Br(),
                    html.Br(),
                    dbc.Row([
                        dbc.Col([
                         dcc.Markdown('* Voltage & Capacity', style={'font-size':'25px', 'textAlign':'left','font-weight':'bold'}),
                         html.H5(('- Cell voltage is dependent on the chemistry of chemical compounds assembled. Nominal voltage is more like an average (or typical) voltage for the system different from the precise operating cell voltage (under load). For lead-acid, the nominal voltage is 2V. For nickel-based, it is 1.2V. For lithium-ion, it is typically more than 3V.'), 
                                 style={'textAlign':'justify', 'margin-left':'20px'}),
                         html.H5(('- Cell capacity states the quantity of charge in the cell and is dependent on the amount of active materials used. It is measured in Amphere-hours.'), 
                                 style={'textAlign':'justify', 'margin-left':'20px'}),
                         html.H5(('- Specific capacity is the capacity measured per unit mass. This can be calculated theoretically using its molecular weight and Faraday constant:'), 
                                 style={'textAlign':'justify', 'margin-left':'20px'}),   
                        dcc.Markdown(dangerously_allow_html=True, mathjax=True, children=('$$Q_{gravimetric}=\\frac{n*F}{M_{W}*3600}$$'), style={'text-align':'center','font-size':'150%'}),
                        ], width={"size": 8}),
                        dbc.Col([
                        html.Div( className="app-header", style={'background-image':'url("https://dl.dropboxusercontent.com/scl/fi/04eebykwg2dgxfr4o2bns/voltage-curve.png?rlkey=1iwh8vmh9cuax2r41gspsvopf&raw=1")',
                        'background-size': '40vh', 'background-repeat':'no-repeat',
                        'background-position':'center', 'height':'50vh'}),
                        ], width={"size": 3}),
                    ],),
                    html.Br(),
                    dmc.Divider(size="md", color="grey"),
                    html.Br(),
                    dbc.Row([
                        dbc.Col([
                         dcc.Markdown('* Energy & Power', style={'font-size':'25px', 'textAlign':'left','font-weight':'bold'}),
                         html.H5('- Energy stored in the cell is defined as the Capacity multiplied by Voltage and its unit is Wh and can be described as:', style={'textAlign':'justify', 'margin-left':'20px'}),
                         dcc.Markdown(dangerously_allow_html=True, mathjax=True, children=("$$E=\\int_0^{t_{d}} IV(t)\\, dt$$"), style={'text-align':'center','font-size':'120%'}),
                         html.H5('- Power is the rate at which how fast the energy can be delivered. Its unit is in Watts. Instantaneous power is simply Current times Voltage at the certain time during battery operation. Average power is defined as:', style={'textAlign':'justify', 'margin-left':'20px'}),
                         dcc.Markdown(dangerously_allow_html=True, mathjax=True, children=("$$P_{avg}=\\frac{1}{t_{d}}\\cdot\\int_0^{t_{d}} IV(t)\\, dt$$"), style={'text-align':'center','font-size':'120%'}),
                         ], width={"size": 8}), 
                        dbc.Col([
                        html.Div( className="app-header", style={'background-image':'url("https://dl.dropboxusercontent.com/scl/fi/u3hpg4778cobd1gkwt7ip/voltage-curve_energy.png?rlkey=yk40i5t5nkfqel0k6v7lrii2x&raw=1")',
                        'background-size': '40vh', 'background-repeat':'no-repeat',
                        'background-position':'center top', 'height':'50vh'}),
                        ], width={"size": 3}),
                    ],),
                    html.Br(),
                    dbc.Row([
                        dbc.Col([
                         html.H5('- Energy density and power density is energy and power normalized by the cell mass. Hence, the unit is Wh/kg and W/kg, respectively. Energy density can be approximated by multiplying specific capacity with nominal voltage.', style={'textAlign':'justify', 'margin-left':'20px'}),
                         html.H5('- Typically, it is difficult for batteries to have both metrics met at the high end. High energy density demands the cell to be discharged at a slow rate for it to reach its maximum capacity and avoid polarization losses. However, since a lower current rate means longer discharge time, power density will be low. For high power density, energy density is likely sacrificed. This trend is illustrated in a Ragone Plot.', style={'textAlign':'justify', 'margin-left':'20px'}),
                         ], width={"size": 8}), 
                        dbc.Col([
                        html.Div( className="app-header", style={'background-image':'url("https://dl.dropboxusercontent.com/scl/fi/95o1wg7pysd41mx7qd1jy/Ragone-plot.bmp?rlkey=3d7offwomdyp0qn7b0tw6fwk6&raw=1")',
                        'background-size': '60vh', 'background-repeat':'no-repeat',
                        'background-position':'center top', 'height':'50vh'}),
                        ], width={"size": 3}),
                    ],),
                    dmc.Divider(size="md", color="grey"),
                    html.Br(),
                    dbc.Row([
                        dbc.Col([
                         dcc.Markdown('* Cell design specifications', style={'font-size':'25px', 'textAlign':'left','font-weight':'bold'}),
                         html.H5('- For high-voltage packs, cells are connected in series to form a series-connected module (SCM).', style={'textAlign':'justify', 'margin-left':'20px'}),
                         dcc.Markdown(dangerously_allow_html=True, mathjax=True, children=("$$v_{pack}=n_{series}*v_{cell}$$"), style={'text-align':'center','font-size':'120%'}),
                         html.H5('- For high-current packs, cells are connected in parallel to form a parallel-connected module (PCM). Capacity scales with the number of cells in parallel.', style={'textAlign':'justify', 'margin-left':'20px'}),
                         dcc.Markdown(dangerously_allow_html=True, mathjax=True, children=("$$i_{pack}=n_{parallel}*i_{cell}$$"), style={'text-align':'center','font-size':'120%'}),
                         html.H5('- Total internal resistance of the pack can be estimated from the cell assuming the same open-circuit voltage and internal resistance:', style={'textAlign':'justify', 'margin-left':'20px'}),
                         dcc.Markdown(dangerously_allow_html=True, mathjax=True, children=("$$R_{pack}=\\frac{n_{series}}{n_{parallel}}*R_{cell}$$"), style={'text-align':'center','font-size':'120%'}),
                         html.H5('- Total pack energy and power can also be calculated:', style={'textAlign':'justify', 'margin-left':'20px'}),
                         dcc.Markdown(dangerously_allow_html=True, mathjax=True, children=("$$E_{pack}=n_{series}*n_{parallel}*Q_{cell}*v_{cell}$$"), style={'text-align':'center','font-size':'120%'}),
                         dcc.Markdown(dangerously_allow_html=True, mathjax=True, children=("$$P_{pack}=n_{series}*n_{parallel}*i_{cell}*v_{cell}$$"), style={'text-align':'center','font-size':'120%'}),
                         ], width={"size": 7}), 
                        dbc.Col([
                        html.Div( className="app-header", style={'background-image':'url("https://dl.dropboxusercontent.com/scl/fi/jg6c9nt6e178rvwqgzmn1/Cell-in-Series-and-Parallel.png?rlkey=jx3kgx1r043llbnv0ewrfiykh&raw=1")',
                        'background-size': '60vh', 'background-repeat':'no-repeat',
                        'background-position':'center', 'height':'50vh'}),
                        ], width={"size": 4}),
                    ],),
                    html.Br(),
                    dmc.Divider(size="md", color="grey"),
                    html.Br(),
                    dbc.Row([
                        dbc.Col([
                         dcc.Markdown('* Cell scaling', style={'font-size':'25px', 'textAlign':'left','font-weight':'bold'}),
                         html.H5('- The amount of electrochemically active material used in the cell or battery determines the magnitude of its capacity. The volume of the electrode is proportional to the capacity of its material by a following relation:', style={'textAlign':'justify', 'margin-left':'20px'}),
                         dcc.Markdown(dangerously_allow_html=True, mathjax=True, children=("$$V_{electrode}=\\frac{3600*Q*M_{w}}{F*\\rho}$$"), style={'text-align':'center','font-size':'150%'}),
                         html.H5('- Since the separator covers the areas of the cathode and anode, nominal current density can be denoted as:', style={'textAlign':'justify', 'margin-left':'20px'}),
                         dcc.Markdown(dangerously_allow_html=True, mathjax=True, children=("$$i_{cell}=\\frac{Q}{t_{d}*A_{sep}}$$"), style={'text-align':'center','font-size':'150%'}),
                         html.H5(children=[html.Span('- Increasing the cell capacity requires increasing the cell volume - increasing the cell thickness or area (or both). When increasing the electrode thickness without changing their areas, current density will be doubled'), html.Strong(' (Case 1)'), html.Span('. This however increases the cell polarization and leads to a lower effective capacity as the cell discharge reaches the cutoff voltage sooner.')], style={'textAlign':'justify', 'margin-left':'20px'}),
                         html.H5(children=[html.Span('- What about increasing the area of the cell to increase its capacity while keeping other parameters the same '), html.Strong('(Case 2)'), html.Span('? Average density is constant as the area of the separator scales with the capacity. Increasing capacity now requires a larger volume change as the separator (and other relevant) volumes also change.')], style={'textAlign':'justify', 'margin-left':'20px'}),
                         html.H5('- This is still not in a desirable way to increase cell capacity since the resistance (i.e. current collectors) goes up as the area increases. Why so? Increase in the area of the current collector means a larger distance the tab is from the entire current collector area.' , style={'textAlign':'justify', 'margin-left':'20px'}),
                       ], width={"size": 7}), 
                        dbc.Col([
                        html.Div( className="app-header", style={'background-image':'url("https://dl.dropboxusercontent.com/scl/fi/8sk0h6a60izh3g7nfzfie/Cell-optimization.png?rlkey=mrx6n266cj1cvfyrlhcacoini&raw=1")',
                        'background-size': '8cm', 'background-repeat':'no-repeat',
                        'background-position':'center', 'height':'60vh'}),
                        ], width={"size": 4}),
                    ],),
                    dbc.Row([
                        dbc.Col([
                        html.Div( className="app-header", style={'background-image':'url("https://dl.dropboxusercontent.com/scl/fi/0jqhyz2iuwjgdom4qh9am/Multilayer-stack.png?rlkey=uy5rjrz0pqxt3uy7pqazarxd3&raw=1")',
                        'background-size': '8cm', 'background-repeat':'no-repeat',
                        'background-position':'center top', 'height':'60vh'}),
                        ], width={"size": 4}),
                        dbc.Col([
                        html.H5(children=[html.Span('- A better way to increase capacity is to stack multiple thinner electrodes such that the same electrode material is positioned on both sides of a current collector'), html.Strong(' (Case 3)'), html.Span('. Such addition of layers connected in parallel increases capacity while mitigating problems associated with the electrode size tuning.')], style={'textAlign':'justify', 'margin-left':'20px'}),
                       ], width={"size": 7}), 
                    ],),
                    html.Br(),
                    dmc.Divider(size="md", color="grey"),
                    html.Br(),
                ],style={'textAlign':'justify', 'margin-left':'30px', 'margin-right':'30px'},),
             ],),
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