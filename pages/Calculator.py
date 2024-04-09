import os
import numpy as np
import dash
from dash import Dash, dcc, html, Input, Output, State, callback
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
import plotly.graph_objs as go
import plotly.express as px
import dash_mantine_components as dmc
import math

dash.register_page(
    __name__, name="Calculator", top_nav=True, path="/calculator"
)
module = ['Single cell', 'Series-connected module', 'Parallel-connected module']

layout = html.Div([
            dbc.Row([
                dbc.Col([
                    html.H1(('Single Cell Calculator (Stacked Design)'), 
                        style={'textAlign':'left', 'font-weight':'bold','color':'purple'}),
                    html.Br(),
                    html.Br(),
                    dcc.Markdown(('- Calculating and plotting of the Li-ion battery cell properties using the measured/estimated input parameters'), 
                        style={'textAlign':'left', 'font-size':'20px'}),
                    html.Br(),
                    html.Br(),
                    ], width={"size":12},
                xs=6, sm=8, md=12, lg=10, xl=12,
                ),
                ],
            style={'justify':'center','text-align':'left'},
            ),
            dbc.Row([
                dbc.Col([
                    dbc.Row([
                        html.Br(),
                        html.Br(),
                        html.H5('Cathode Parameters', style={"margin-bottom":"0em", "color":"red"}),
                        html.Div([dcc.Markdown('Electrode density (g/cm<sup>3</sup>)', dangerously_allow_html=True, style={"height": "1.3em", "margin-bottom": "auto"}),
                            dcc.Input(id="input-m", type="number", value='0.5', step='0.001', style={"margin-bottom":"1em"}) ]),
                        html.Div([html.P('Electrode thickness (um)', style={"height": "auto", "margin-bottom": "auto"}),
                            dcc.Input(id="input-n", type="number", value='50', step='0.01', style={"margin-bottom":"1em"}) ]),                      
                        html.Div([html.P('Active material loading ratio', style={"height": "auto", "margin-bottom": "auto"}),
                            dcc.Input(id="input-o", type="number", value='0.8', step='0.01', style={"margin-bottom":"1em"}) ]),
                        html.Div([html.P('Discharge capacity of active material (mAh/g)', style={"height": "auto", "margin-bottom": "auto"}),
                            dcc.Input(id="input-p", type="number", value='150', step='0.1', style={"margin-bottom":"1em"}) ]),
                        html.Div([dcc.Markdown('Electrode area (mm<sup>2</sup>)', dangerously_allow_html=True, style={"height": "1.3em", "margin-bottom": "auto"}),
                            dcc.Input(id="input-q", type="number", value='1500', step='0.01', style={"margin-bottom":"1em"}) ]),
                        html.Div([html.P('Number of layers', style={"height": "auto", "margin-bottom": "auto"}),
                            dcc.Input(id="input-r", type="number", value='5', step='1', style={"margin-bottom":"1em"}) ]),
                        html.Br(),
                        html.Br(),
                        ],
                    style={'textAlign':'center'},
                    ),
                ],width={"size":3},
                xs=6, sm=6, md=6, lg=3, xl=3,
                ),
                dbc.Col([   
                    dbc.Row([
                        html.H5('Other parameters', style={"margin-bottom":"0.5em", "color":"Purple"}),
                        html.Div([html.P('Total Al foil weight (g)', style={"height": "auto", "margin-bottom": "auto"}),
                            dcc.Input(id="input-x", type="number", value='0.7', step='0.001', style={"margin-bottom":"1em"}) ]),
                        html.Div([html.P('Total Cu foil weight (g)', style={"height": "auto", "margin-bottom": "auto"}),
                            dcc.Input(id="input-y", type="number", value='1.2', step='0.001', style={"margin-bottom":"1em"}) ]),                      
                        html.Div([html.P('Total separator weight (g)', style={"height": "auto", "margin-bottom": "auto"}),
                            dcc.Input(id="input-z", type="number", value='0.5', step='0.001', style={"margin-bottom":"1em"}) ]),
                        html.Div([html.P('Electrolyte weight (g)', style={"height": "auto", "margin-bottom": "auto"}),
                            dcc.Input(id="input-ab", type="number", value='3', step='0.001', style={"margin-bottom":"1em"}) ]),              
                        html.Div([html.P('Other weight-Sum (g)', style={"height": "auto", "margin-bottom": "auto"}),
                            dcc.Input(id="input-bc", type="number", value='1.1', step='0.001', style={"margin-bottom":"1em"}) ]),                                
                        html.Br(),
                        html.Br(),
                        ],
                    style={'textAlign':'center'},
                    ),
                    ], 
                width={"size":3}, style={'margin-left':'5px'},
                xs=6, sm=6, md=6, lg=3, xl=3,
                ),
                dbc.Col([
                    dbc.Row([
                        html.H5('Anode Parameters', style={"margin-bottom":"1em", "color":"blue"}),
                        html.Div([dcc.Markdown('Electrode density (g/cm<sup>3</sup>)', dangerously_allow_html=True, style={"height": "1.3em", "margin-bottom": "auto"}),
                            dcc.Input(id="input-i", type="number", value='2', step='0.001', style={"margin-bottom":"1em"}) ]),
                        html.Div([html.P('Electrode thickness (um)', style={"height": "auto", "margin-bottom": "auto"}),
                            dcc.Input(id="input-j", type="number", value='50', step='0.01', style={"margin-bottom":"1em"}) ]),                      
                        html.Div([html.P('Active material loading ratio', style={"height": "auto", "margin-bottom": "auto"}),
                            dcc.Input(id="input-k", type="number", value='0.9', step='0.01', style={"margin-bottom":"1em"}) ]),
                        html.Div([html.P('Discharge capacity of active material (mAh/g)', style={"height": "auto", "margin-bottom": "auto"}),
                            dcc.Input(id="input-l", type="number", value='500', step='0.1', style={"margin-bottom":"1em"}) ]),
                        html.Div([dcc.Markdown('Electrode area (mm<sup>2</sup>)', dangerously_allow_html=True, style={"height": "1.3em", "margin-bottom": "auto"}),
                            dcc.Input(id="input-w", type="number", value='1000', step='0.01', style={"margin-bottom":"1em"}) ]),        
                        html.Br(),
                        html.Br(),
                        ],
                        style={'textAlign':'center'},
                        ),
                        ],
                width={"size":3}, style={'margin-left':'5px'},
                xs=6, sm=6, md=6, lg=3, xl=3,
                ),
                dbc.Col([
                    dbc.Row([
                        dbc.Col(html.Span(id='outcome3', style={"font-size": "150%", "color": "grey", "margin-top": "1em",
                                                "width": "100%",
                                                "justify": "center", "text-align": "left"})),
                                                ],
                                                style = {"margin-top":"1em"}
                                                ),
                    html.Br(),
                    dbc.Row([
                        dbc.Col(html.Span(id='outcome4', style={"font-size": "150%", "color": "grey", "margin-top": "1em",
                                                "width": "100%", "justify": "center",
                                                "text-align": "left"})),
                    ],
                    ),
                ],
                width={"size":3}, style={'margin-left':'5px', "border":"5px black solid", "display":"inline-block", "border-radius":"1em"},
                xs=1, sm=5, md=6, lg=2, xl=2,
                ),
            dbc.Row([
                dbc.Col([
                    dcc.Graph(id='plot3', style={"width":"100%", "height":"50vh","margin-top":"20px"})
                    ],
                width={"size":"6"},
                xs=6, sm=12, md=10, lg=6, xl=6,                    
                ),
                dbc.Col([    
                    dcc.Graph(id='plot4', style={"width":"100%", "height":"50vh","margin-top":"20px"})
                    ],
                width={"size":"6"},
                xs=6, sm=12, md=10, lg=6, xl=6,
                    ),
                ],
                ),
            ]),
            html.Br(),
            dmc.Divider(size="md", variant="dotted", color="grey"),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    html.Br(),
                    html.H1(('Pack Calculator'), 
                        style={'textAlign':'left', 'font-weight':'bold','color':'purple'}),
                    html.Br(),
                    html.Br(),
                    dcc.Markdown(('- Generating simple estimated calculation of the pack-level performance of the cell above.'), 
                        style={'textAlign':'left', 'font-size':'20px'}),
                    ], width={"size":"12"},
                xs=8, sm=12, md=12, lg=12, xl=12,
                ),
                ],
            style={'justify':'left','text-align':'left'},
            ),
            dbc.Row([
                dbc.Col([
                    dbc.Row([
                        html.Br(),
                        html.Br(),
                        html.H4('Parameters', style={"margin-bottom":"0em", "color":"red"}),
                        html.Div(children=[
                                html.Label('Module Type'),dcc.Dropdown(
                                    id='dropdown', style={'margin':'auto','maxWidth':'100%','width':'100%', "margin": "auto"}, 
                                options=(module), multi=False, clearable=False, value='Single cell'),
                        html.Div(id='display-result')],
                            style={"margin-bottom":"30px"}
                        ),  
                        html.Div([html.P('# Cells/Modules in Series', style={"height": "auto", "margin-bottom": "auto"}),
                            dcc.Input(id="input-s", type="number", value='6', step='1', style={"margin-bottom":"1em"}) ]),
                        html.Div([html.P('# Cells/Modules in Parallel', style={"height": "auto", "margin-bottom": "auto"}),
                             dcc.Input(id="input-t", type="number", value='15', step='1', style={"margin-bottom":"1em"}) ]),                    
                        html.Div([html.P('Nominal Voltage (V)', style={"height": "auto", "margin-bottom": "auto"}),
                             dcc.Input(id="input-u", type="number", value='3', step='0.01', style={"margin-bottom":"1em"}) ]),
                        html.Div([html.P('Cell-to-Pack Weight Ratio', style={"height": "auto", "margin-bottom": "auto"}),
                            dcc.Input(id="input-v", type="number", value='0.6', step='0.1', style={"margin-bottom":"1em"}) 
                        ]),
                        ],
                        style={"margin-left":"40px","margin-top":"40px","margin-right":"0px", "border": "black solid", "border-width":"3px", "border-radius":"15px"},
                    ),
                ],
                width={"size":3}, style={'margin-left':'5px'},
                xs=6, sm=10, md=6, lg=6, xl=3,
                ),
                dbc.Col([
                    dbc.Row([
                        html.Br(),
                        html.Br(),
                        html.Span(id='outcome5', style={"font-size":"150%", "color":"blue","margin-top":"2em"}),
                        html.Span(id='outcome6', style={"font-size":"150%", "color":"blue","margin-top":"2em"}),
                        html.Span(id='outcome7', style={"font-size":"150%", "color":"red","margin-top":"2em"}),
                        html.Span(id='outcome8', style={"font-size":"150%", "color":"red","margin-top":"2em"}),
                        ],
                        style={"margin-left":"80px","margin-top":"40px"},
                    ),
                    ],
                    style={'textAlign':'center'}, 
                width={"size":"6"},
                xs=10, sm=12, md=10, lg=6, xl=6,
                ),
            ],
        ),
        html.Br(),
        dmc.Divider(size="md", color="grey"),
        html.Br(),
        dbc.Row([
                dbc.Col([
                    html.H1(('Single Cell Calculator (Jelly-roll Design)'), 
                        style={'textAlign':'left', 'font-weight':'bold','color':'purple'}),
                    html.Br(),
                    html.Br(),
                    dcc.Markdown(('- Calculating and plotting of the Li-ion battery cell properties for the cylindrical cell'), 
                        style={'textAlign':'left', 'font-size':'20px'}),
                    html.Br(),
                    html.Br(),
                    ], width={"size":12},
                xs=6, sm=8, md=12, lg=10, xl=12,
                ),
                ],
            style={'justify':'center','text-align':'left'},
        ),
        dbc.Row([
                dbc.Col([
                    dbc.Row([
                        html.Br(),
                        html.Br(),
                        html.H5('Cathode Parameters', style={"margin-bottom":"0em", "color":"red"}),
                        html.Div([html.P('Coating thickness (Single-side) (um)', style={"height": "auto", "margin-bottom": "auto"}),
                            dcc.Input(id="input-c1", type="number", value='52.5', step='0.001', style={"margin-bottom":"1em"}) ]),
                        html.Div([html.P('Al foil thickness (um)', style={"height": "auto", "margin-bottom": "auto"}),
                            dcc.Input(id="input-c2", type="number", value='20', step='0.1', style={"margin-bottom":"1em"}) ]),
                        html.Div([html.P('Discharge capacity of active material (mAh/g)', style={"height": "auto", "margin-bottom": "auto"}),
                            dcc.Input(id="input-c3", type="number", value='200', step='0.1', style={"margin-bottom":"1em"}) ]),                        
                        html.Div([dcc.Markdown('Density of electrode material (g/cm<sup>3</sup>)', dangerously_allow_html=True, style={"height": "1.3em", "margin-bottom": "auto"}),
                            dcc.Input(id="input-c4", type="number", value='4.87', step='0.01', style={"margin-bottom":"1em"}) ]),
                        html.Div([html.P('Active material loading ratio', style={"height": "auto", "margin-bottom": "auto"}),
                            dcc.Input(id="input-c5", type="number", value='0.8', step='0.01', style={"margin-bottom":"1em"}) ]),
                        html.Div([html.P('Estimated porosity', style={"height": "auto", "margin-bottom": "auto"}),
                            dcc.Input(id="input-c6", type="number", value='0.35', step='0.01', style={"margin-bottom":"1em"}) ]),
                        html.Div([html.P('Electrode width (cm)', style={"height": "auto", "margin-bottom": "auto"}),
                            dcc.Input(id="input-c7", type="number", value='6.8', step='0.01', style={"margin-bottom":"1em"}) ]),
                        html.Br(),
                        html.Br(),
                        ],
                    style={'textAlign':'center'},
                    ),
                ],width={"size":4},
                xs=6, sm=6, md=6, lg=3, xl=4,
                ),
                dbc.Col([   
                    dbc.Row([
                        html.H5('Other cell parameters', style={"margin-bottom":"0.5em", "color":"Purple"}),
                        html.Div([html.P('Anode coating thickness (Single-side) (um)', style={"height": "auto", "margin-bottom": "auto"}),
                            dcc.Input(id="input-c8", type="number", value='58', step='0.01', style={"margin-bottom":"1em"}) ]),                      
                        html.Div([html.P('Cu foil thickness (um)', style={"height": "auto", "margin-bottom": "auto"}),
                            dcc.Input(id="input-c9", type="number", value='10', step='0.1', style={"margin-bottom":"1em"}) ]),                      
                        html.Div([html.P('Separator thickness (um)', style={"height": "auto", "margin-bottom": "auto"}),
                            dcc.Input(id="input-c10", type="number", value='16', step='0.1', style={"margin-bottom":"1em"}) ]),
                        html.Div([html.P('Outer diameter of the cell (mm)', style={"height": "auto", "margin-bottom": "auto"}),
                            dcc.Input(id="input-c11", type="number", value='47', step='0.001', style={"margin-bottom":"1em"}) ]),              
                        html.Div([html.P('Cell Can thickness (mm)', style={"height": "auto", "margin-bottom": "auto"}),
                            dcc.Input(id="input-c12", type="number", value='0.5', step='0.001', style={"margin-bottom":"1em"}) ]),              
                        html.Div([html.P('Inner diameter of the cell (mm)', style={"height": "auto", "margin-bottom": "auto"}),
                            dcc.Input(id="input-c13", type="number", value='2', step='0.001', style={"margin-bottom":"1em"}) ]),                                
                        html.Br(),
                        html.Br(),
                        ],
                    style={'textAlign':'center'},
                    ),
                    ], 
                width={"size":4}, style={'margin-left':'5px'},
                xs=6, sm=6, md=6, lg=3, xl=4,
                ),
                dbc.Col([
                    dbc.Row([
                        html.Br(),
                        html.Br(),
                        html.Span(id='outcome9', style={"font-size":"150%", "color":"blue","margin-top":"2em"}),
                        html.Span(id='outcome10', style={"font-size":"150%", "color":"blue","margin-top":"2em"}),
                        html.Span(id='outcome11', style={"font-size":"150%", "color":"red","margin-top":"2em"}),
                        html.Span(id='outcome12', style={"font-size":"150%", "color":"red","margin-top":"2em"}),
                        ],
                        style={"margin-left":"80px","margin-top":"40px"},
                    ),
                    ],
                    style={'textAlign':'center'}, 
                width={"size":"6"},
                xs=10, sm=12, md=10, lg=6, xl=6,
                ),
            ]),
            html.Br(),
            dmc.Divider(size="md", variant="dotted", color="grey"),
            html.Br(), 
        dbc.Row([
                dbc.Col([
                    html.H1(('Li cell performance predictor'), 
                        style={'textAlign':'left', 'font-weight':'bold','color':'purple'}),
                    ],  width={"size":"6"},
                xs=16, sm=12, md=10, lg=6, xl=6,
                ),
                ],
            style={'justify':'left','text-align':'left'},
        ),
        dbc.Row([
            dbc.Col([
                    dbc.Row([
                        html.Div([html.P('Coulombic Efficiency (%)', style={"height": "auto", "margin-bottom": "auto"}),
                        dcc.Input(id="input-zz", type="number", value='95', step='0.1', style={"margin-bottom":"1em"}) ]),
                        html.Div([html.P('Capacity Retention (%)', style={"height": "auto", "margin-bottom": "auto"}),
                        dcc.Input(id="input-g", type="number", value='80', step='0.1', style={"margin-bottom":"1em"}) ]),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Span(id='outcome', style={"font-size":"150%", "color":"red"}),
                    ],
                    style={"margin-left":"10px","margin-top":"50px"},
                    ),
                ], 
                width={"size":"6"},
                xs=12, sm=12, md=10, lg=6, xl=6,
                ),
            dbc.Col([
                dbc.Row([
                    dcc.Graph(id='plot', style={"width":"120vh", "height":"50vh","margin-top":"0px"})
                        ],),
                ], 
                width={"size":"6"},
                xs=12, sm=12, md=10, lg=6, xl=6,
            ),
        ],),
        dbc.Row([
            dbc.Col([
                    dbc.Row([
                        html.Div([html.P('Coulombic Efficiency (%)', style={"height": "auto", "margin-bottom": "auto"}),
                        dcc.Input(id="input-f", type="number", value='95', step='0.1', style={"margin-bottom":"1em"}) ]),
                        html.Div([html.P('Desired cycle number', style={"height": "auto", "margin-bottom": "auto"}),
                        dcc.Input(id="input-h", type="number", value='80', step='0.1', style={"margin-bottom":"1em"}) ]),
                        html.Br(),
                        html.Br(),
                        html.Span(id='outcome2', style={"font-size":"150%", "color":"red"}),
                    ],
                    style={"margin-left":"10px","margin-top":"50px"},
                    ),
            ], 
            width={"size":"6"},
            xs=12, sm=12, md=10, lg=6, xl=6,
            ),
            dbc.Col([
                dbc.Row([
                dcc.Graph(id='plot2', style={"width":"120vh", "height":"50vh","margin-top":"20px"})
                ],),
                ], 
                width={"size":"6"},
                xs=12, sm=12, md=10, lg=6, xl=6,
            ),
            ],
        ),
        html.Br(),
        html.Br(),
        html.Br(),
        ], 
        #style={'textAlign':'justify', 'margin-left':'30px', 'margin-right':'30px'},
        #style={'padding': '2%', 'width': '100%', 'boxSizing': 'border-box', 'display': 'flex', 'flexWrap': 'wrap', 'justifyContent': 'left'}
        style={'padding': '1%', 'width': '100%', 'justifyContent': 'left'}
   
    ),
        
        
@callback([Output('result', 'children'), Output('graph','figure')],
                [Input('input-a', 'value'),
                Input('input-b', 'value'),
                Input('input-c', 'value'),
                Input('input-d', 'value'),
                Input('input-e', 'value')    
                ], 
            )
def update_content(input_a, input_b, input_c, input_d, input_e):
    if input_a and input_b and input_c and input_d and input_e:
        result = 10000*float(input_a)*float(input_b)/(float(input_c)*float(input_d)*float(input_e))
        x=np.arange(0,10)
        y=10000*x * float(input_b)/(float(input_c)*float(input_d)*float(input_e))
        z=np.polyfit(x,y,1)
        f=np.poly1d(z)
        x_new=np.linspace(0,10,500)
        y_new=f(x_new)
        #trace1 = go.Scatter(x=x, y=y, name='data', mode='lines')
        trace1 = go.Scatter(x=x_new, y=y_new, name='fit', mode='lines')
        data=[trace1]
        fig = go.Figure(data=data)
        fig.update_layout(
            plot_bgcolor='white',
            xaxis_title='Areal Capacity of Li (mAh/cm^2)',
            yaxis_title="Li Thickness (\u03BCm)",
            font=dict(
                family="arial, monospace",
                size=16,
                color="black"
            )
        )
        fig.update_xaxes(
            mirror=False,
            ticks='outside',
            showline=True,
            linecolor='black',
            gridcolor='lightgrey'
        )
        fig.update_yaxes(
            mirror=True,
            ticks='outside',
            showline=True,
            linecolor='black',
            gridcolor='lightgrey'
        )
        return "The calculated Li thickness is: {} \u03BCm".format(round(result,2)), fig
    else:
        return "", {}

@callback([Output('outcome', 'children'), Output('outcome2', 'children'), Output('plot','figure'), Output('plot2','figure')],
                [Input('input-f', 'value'),
                Input('input-g', 'value'),
                Input('input-h', 'value'),
                Input('input-zz','value'),  
                ], 
            )
def update_content(input_f, input_g, input_h, input_zz):
    if input_f is not None and input_g is not None and input_h is not None and input_zz is not None:
        outcome = np.log10(float(input_g)/100)/np.log10(float(input_zz)/100)
        outcome2 = np.exp(float(input_h)*np.log10(float(input_f)/100))*100
        x2=np.arange(98,100,0.05)
        y2=np.log10(float(input_g)/100)/np.log10(x2/100)
        y3=np.exp(float(input_h)*np.log10(x2/100))*100
        #z=np.polyfit(x,y,1)
        #f=np.poly1d(z)
        #x_new=np.linspace(0,10,500)
        #y_new=f(x_new)
        trace2 = go.Scatter(x=x2, y=y2, name='data2', mode='lines')
        trace3 = go.Scatter(x=x2, y=y3, name='data3', mode='lines')
        data2=[trace2]
        data3=[trace3]
        fig2 = go.Figure(data=data2)
        fig3 = go.Figure(data=data3)
        fig2.update_layout(
            plot_bgcolor='rgb(234, 228, 228)',
            paper_bgcolor='rgb(211, 211, 211)',
            title="Coulombic Efficiency vs Cycle Number",
            title_x=0.5,
            xaxis_title="Coulombic Efficiency (%)",
            yaxis_title="Cycle Numbers",
            font=dict(
                family="arial, monospace",
                size=16,
                color="black"
            )
        )
        fig2.update_xaxes(
            mirror=False,
            ticks='outside',
            showline=True,
            linecolor='black',
            gridcolor='lightgrey'
        )
        fig2.update_yaxes(
            mirror=True,
            ticks='outside',
            showline=True,
            linecolor='black',
            gridcolor='lightgrey'
        )
        fig3.update_layout(
            plot_bgcolor='rgb(234, 228, 228)',
            paper_bgcolor='rgb(211, 211, 211)',
            title="Coulombic Efficiency vs Capacity Retention",
            title_x=0.5,
            xaxis_title="Coulombic Efficiency (%)",
            yaxis_title="Capacity Retention (%)",
            font=dict(
                family="arial, monospace",
                size=16,
                color="black"
            )
        )
        fig3.update_xaxes(
            mirror=False,
            ticks='outside',
            showline=True,
            linecolor='black',
            gridcolor='lightgrey'
        )
        fig3.update_yaxes(
            mirror=True,
            ticks='outside',
            showline=True,
            linecolor='black',
            gridcolor='lightgrey'
        )
        return dcc.Markdown("The cell is expected to undergo **{}** cycles".format(round(outcome,2)), dangerously_allow_html=True),  \
                dcc.Markdown("The cell is expected to have **{} %** capacity retention".format(round(outcome2,2)), dangerously_allow_html=True), \
                fig2, fig3
    else:
        return "", "", {}, {}

@callback([Output('outcome3', 'children'), Output('outcome4', 'children'), Output('outcome5', 'children'), 
               Output('outcome6','children'), Output('outcome7','children'), Output('outcome8','children'), Output('plot3','figure'), Output('plot4','figure')],
                [Input('input-i', 'value'),
                Input('input-j', 'value'),
                Input('input-k', 'value'),
                Input('input-l', 'value'),
                Input('input-m', 'value'),
                Input('input-n', 'value'),
                Input('input-o', 'value'),
                Input('input-p', 'value'),
                Input('input-q', 'value'),
                Input('input-r', 'value'),
                Input('input-s', 'value'),
                Input('input-t', 'value'),
                Input('input-u', 'value'),  
                Input('input-v', 'value'),
                Input('input-w', 'value'),
                Input('input-x', 'value'),
                Input('input-y', 'value'),
                Input('input-z', 'value'),
                Input('input-ab', 'value'),
                Input('input-bc', 'value'),
                Input('dropdown', 'value')
                ], 
            )
def update_content(input_i, input_j, input_k, input_l, input_m, input_n, input_o, input_p, input_q, input_r, input_s, input_t, input_u, input_v, input_w, input_x, input_y, input_z, input_ab, input_bc, dropdown_value):
    if all([input_i and input_j and input_k and input_l and input_m and input_n and input_o and input_p and input_q and input_r and input_s and input_t and input_u and input_v and input_w and input_x and input_y and input_z and input_ab and input_bc and dropdown_value]):
        ano_n = float(input_i)*float(input_j)*0.0001*float(input_k)*float(input_l)
        cat_p = float(input_m)*float(input_n)*0.0001*float(input_o)*float(input_p)
        outcome3 = ano_n/cat_p
        outcome4 = cat_p*float(input_q)*0.01*float(input_r)/1000
        outcome5 = outcome4
        outcome6 = outcome4*float(input_t)
        outcome7 = float(input_s)*float(input_u)*float(input_t)*outcome4
        #total weight(all parts including anode weight but not cathode weight)
        tot_w=float(input_x)+float(input_y)+float(input_z)+float(input_ab)+float(input_bc)+(float(input_i)*float(input_j)*0.0001*float(input_w)*0.01)*float(input_r)
        #total weight(all parts including both anode and cathode weights)
        tot_w2=float(input_x)+float(input_y)+float(input_z)+float(input_ab)+float(input_bc)+((float(input_i)*float(input_j)*0.0001*float(input_w)*0.01)+(float(input_m)*float(input_n)*0.0001*float(input_q)*0.01))*float(input_r)
        outcome8 = outcome7 /((1/float(input_v))*tot_w2)*1000/1000
        np_ratio=dcc.Markdown("NP ratio calculated is **{}**.".format(round(outcome3,2)), dangerously_allow_html=True),
        cell_capacity=dcc.Markdown("Cell capacity calculated is **{}** Ah.".format(round(outcome4,2)), dangerously_allow_html=True),
        x3=np.arange(0,0.04,0.001) #cathode loading (g/cm2)
        y4=(float(input_u)*(x3*float(input_o)*float(input_p)*float(input_q)*0.01*float(input_r))/1000)/((tot_w+(x3*float(input_q)*0.01*float(input_r)))*0.001)
        x4=np.arange(0,5.5,0.01) #like cat_p
        y5=(float(input_u)*(x4*float(input_q)*0.01*float(input_r))/1000)/((tot_w+(x4/float(input_p)*float(input_q)*0.01*float(input_r)))*0.001)
        trace4 = go.Scatter(x=x3, y=y4, name='data4', mode='lines')
        trace5 = go.Scatter(x=x4, y=y5, name='data5', mode='lines')
        data4=[trace4]
        data5=[trace5]
        fig4 = go.Figure(data=data4)
        fig5 = go.Figure(data=data5)
        fig4.update_layout(
            plot_bgcolor='rgb(234, 228, 228)',
            paper_bgcolor='rgb(211, 211, 211)',
            title="Cell Dimension vs Energy Density",
            title_x=0.5,
            xaxis_title="Cathode loading (g/cm2)",
            yaxis_title="Cell energy density (Wh/kg)",
            font=dict(
                family="arial, monospace",
                size=16,
                color="black"
            )
        )
        fig4.update_xaxes(
            mirror=False,
            ticks='outside',
            showline=True,
            linecolor='black',
            gridcolor='lightgrey' 
        )
        fig4.update_yaxes(
            mirror=True,
            ticks='outside',
            showline=True,
            linecolor='black',
            gridcolor='lightgrey'
        )
        fig4.add_hline(y=200, line_dash="dash", line_color="orange")
        fig4.add_hline(y=300, line_dash="dash", line_color="red")
        fig5.update_layout(
            plot_bgcolor='rgb(234, 228, 228)',
            paper_bgcolor='rgb(211, 211, 211)',
            title="Cell Dimension vs Energy Density",
            title_x=0.5,
            xaxis_title="Cathode area capacity (mAh/cm2)",
            yaxis_title="Cell energy density (Wh/kg)",
            font=dict(
                family="arial, monospace",
                size=16,
                color="black"
            )
        )
        fig5.update_xaxes(
            mirror=False,
            ticks='outside',
            showline=True,
            linecolor='black',
            gridcolor='lightgrey'
        )
        fig5.update_yaxes(
            mirror=True,
            ticks='outside',
            showline=True,
            linecolor='black',
            gridcolor='lightgrey'
        )
        fig5.add_hline(y=200, line_dash="dash", line_color="orange")
        fig5.add_hline(y=300, line_dash="dash", line_color="red")
        
        if dropdown_value == 'Series-connected module':
            return (
                np_ratio,
                cell_capacity,
                "SCM capacity is {} Ah".format(round(outcome5,2)),
                "Pack energy calculated is {} Wh".format(round(outcome7,2)), 
                "Pack energy density calculated is {} kWh/kg".format(round(outcome8,2)),
                "",fig4, fig5
                )
        elif dropdown_value == 'Parallel-connected module':
            return (
                np_ratio,
                cell_capacity,
                "PCM capacity is {} Ah".format(round(outcome6,2)),
                "Pack energy calculated is {} Wh".format(round(outcome7,2)), 
                "Pack energy density calculated is {} kWh/kg".format(round(outcome8,2)),
                "",fig4, fig5
                )
        else:
            return (
                np_ratio, 
                cell_capacity, 
                "",
                "",
                "",
                "", fig4, fig5
                )
    else:   
        return (
            "",
            "",
            "",
            "",
            "",
            "",
            {}, {}
            )

@callback([Output('outcome9', 'children'), Output('outcome10', 'children'), Output('outcome11', 'children'), 
               Output('outcome12','children')],
                [Input('input-c1', 'value'),
                Input('input-c2', 'value'),
                Input('input-c3', 'value'),
                Input('input-c4', 'value'),
                Input('input-c5', 'value'),
                Input('input-c6', 'value'),
                Input('input-c7', 'value'),
                Input('input-c8', 'value'),
                Input('input-c9', 'value'),
                Input('input-c10', 'value'),
                Input('input-c11', 'value'),
                Input('input-c12', 'value'),
                Input('input-c13', 'value'),  
                ], 
            )        
def update_content(input_c1, input_c2, input_c3, input_c4, input_c5, input_c6, input_c7, input_c8, input_c9, input_c10, input_c11, input_c12, input_c13):
    if all([input_c1 and input_c2 and input_c3 and input_c4 and input_c5 and input_c6 and input_c7 and input_c8 and input_c9 and input_c10 and input_c11 and input_c12 and input_c13]):
        d_asc = float(input_c1)*2+float(input_c2)+float(input_c8)*2+float(input_c9)+float(input_c10)*2
        a=d_asc/(2*np.pi)*(0.000001)
        d_o=float(input_c11)-2*float(input_c12)
        r_o=d_o*(0.001)/2
        d_i=float(input_c13)
        r_i=d_i*(0.001)/2
        sigma_1=r_o/a
        sigma_0=r_i/a
        L1=(sigma_1/2)*(pow(((sigma_1)*(sigma_1)+1),0.5))+0.5*np.log(sigma_1+pow(((sigma_1)*(sigma_1)+1),0.5))
        L0=(sigma_0/2)*(pow(((sigma_0)*(sigma_0)+1),0.5))+0.5*np.log(sigma_0+pow(((sigma_1)*(sigma_1)+1),0.5))
        L_t=(L1-L0)*d_asc/(2*np.pi)*0.000001
        outcome9 = L_t #Length of the cathode
        cathode_length=dcc.Markdown("The length of the cathode is **{}** m.".format(round(outcome9,2)), dangerously_allow_html=True),
        outcome10 = (sigma_1-sigma_0)/(2*np.pi) #Number of turns of the cathode in the cell
        winding_number=dcc.Markdown("The number of winding(turn) is **{}**.".format(round(outcome10,1)), dangerously_allow_html=True),
        outcome11 = float(input_c4)*float(input_c5)*(1-float(input_c6))*(float(input_c1)*(0.0001))*float(input_c3) #Areal cathode capacity
        areal_capacity=dcc.Markdown("The areal cathode capacity is **{}** mAh/cm<sup>2</sup>.".format(round(outcome11,2)), dangerously_allow_html=True),
        outcome12 = outcome11*outcome9*100*float(input_c7)/1000 #Areal cathode capacity
        cell_capacity=dcc.Markdown("The predicted cell capacity is **{}** Ah.".format(round(outcome12,2)), dangerously_allow_html=True),
        return (
            cathode_length,
            winding_number,
            areal_capacity,
            cell_capacity,
        )
    else:
        return "", "", "", ""