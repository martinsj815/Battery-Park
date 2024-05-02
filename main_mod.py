import os
import numpy as np
import dash
from dash import Dash, dcc, html, Input, Output, State, callback
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
import plotly.express as px

# Initialize the app
app_name = os.getenv("APP_NAME", "Beyond-Cell")
app = Dash( __name__,
    external_stylesheets=[dbc.themes.SANDSTONE], assets_folder='masthead', assets_url_path='/masthead/', suppress_callback_exceptions=True
)

app.title="Cell Design"

server = app.server

# App layout
app.layout = html.Div([
    html.Br(),
    html.Br(),
    dbc.Row([
    html.Div( className="app-header", children=[
        html.H1('', className="app-header--title")]),
    ],style={'background-image':'url("https://dl.dropboxusercontent.com/scl/fi/7nffwz67v6d6zmqs3sz7q/Masthead_new.png?rlkey=t6ulgyybpwopmymp5dp4gykaz&raw=1")',
             'background-size': '160vh', 'background-repeat':'no-repeat',
          'background-position':'center left', 'height':'20vh'}),
    html.Br(),
    html.Br(),
    dbc.Row([
    dbc.Col(html.H5(children="Batteries, comprising one or more electrochemical cells, play an ever more crucial role in our daily lives, powering everything from smartphones to electric vehicles. As the demand for higher performance increases and the availability of battery constituent resources becomes scarcer, there is an urgent need to concentrate on developing batteries with optimized parameters through efficient resource allocation."),
            width=11),dbc.Col(width=3),
    ], style={'margin-left':'20px'}),
    html.Br(),
    html.Br(),
    dcc.Tabs(id='Options', value='tab-1', children=[
        dcc.Tab(label='Basics', value='Lim', style={'font-size':'25px', 'border-style':'solid', 'border-radius':'6px'}),
        dcc.Tab(label='Parameters/Performance', value='NP', style={'font-size':'25px', 'border-style':'solid', 'border-radius':'6px'}),
        dcc.Tab(label='What more?', value='cells', style={'font-size':'25px', 'border-style':'solid', 'border-radius':'6px'})]
    ),
    html.Div(id='Options-content')
], 
)

@app.callback(Output('Options-content', 'children'), [Input('Options','value')])

def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
        ])
    elif tab=='Lim':
        return html.Div([
            html.Br(),
            html.Br(),
            html.Br(),
             dbc.Row([
                dbc.Col([
                    dbc.Row([
                         dcc.Markdown('* Electrochemical Cell', style={'font-size':'25px', 'textAlign':'left','font-weight':'bold'}),
                         html.H5(('- A cell is the smallest building unit of the battery. Main constituents are cathode and anode that are immersed in electrolyte and undergo reduction/oxidation. Cations migrate inside the electrolyte while electrons move through the external load to do the work.'), 
                                 style={'textAlign':'justify', 'margin-left':'20px'}),
                         html.H5(('- When a cell is discharged, cations and electrons from the negative electrode move towards the positive electrode, where the reduction takes place (while the negative electrode is oxidized). Different from the case of primary batteries, this process can be reversed through charging in secondary rechargeable batteries.'), 
                                 style={'textAlign':'justify', 'margin-left':'20px'}),
                         html.H5(('- Cells also include the separator that isolate the positive and negative electrodes to prevent the electron flow and permit only the ion flow and the current collectors - metal foils where the electrodes are attached and that conduct electrical current to the external circuit.'), 
                                 style={'textAlign':'justify', 'margin-left':'20px'}),
                    ],),
                    html.Br(),
                    html.Br(),
                    dbc.Row([
                         dcc.Markdown('* Battery Pack', style={'font-size':'25px', 'textAlign':'left','font-weight':'bold'}),
                         html.H5(('- Battery or Battery Pack is consisting of one or more cells that are connected in series or parallel or in combination of both, assembled with the electrical interconnects and packaged into a single unit.'), 
                                 style={'textAlign':'justify', 'margin-left':'20px'}),
                         html.H5(('- The pack usually requires monitoring, sensing (i.e. voltage and temperature), and control through effective battery management system for protection, stability, and safety of the battery.'), 
                                 style={'textAlign':'justify', 'margin-left':'20px'}),
                    ],),
                    html.Br(),
                    html.Br(),
                    dbc.Row([
                         dcc.Markdown('* Voltage', style={'font-size':'25px', 'textAlign':'left','font-weight':'bold'}),
                         html.H5(('- Cell voltage is dependent on the chemistry of chemical compounds assembled. Nominal voltage is more like an average (or typical) voltage for the system different from the precise operating cell voltage (under load).'), 
                                 style={'textAlign':'justify', 'margin-left':'20px'}),
                         html.H5(('- For lead-acid, the nominal voltage is 2V. For nickel-based, it is 1.2V. For lithium-ion, it is typically more than 3V.'), 
                                 style={'textAlign':'justify', 'margin-left':'20px'}),
                    ],),
                    html.Br(),
                    html.Br(),
                    dbc.Row([
                         dcc.Markdown('* Capacity', style={'font-size':'25px', 'textAlign':'left','font-weight':'bold'}),
                         html.H5(('- Cell capacity states the quantity of charge in the cell and is dependent on the amount of active materials used. It is measured in Amphere-hours.'), 
                                 style={'textAlign':'justify', 'margin-left':'20px'}),
                         html.H5(('- Specific capacity is the capacity measured per unit mass. This can be calculated theoretically using its molecular weight and Faraday constant.'), 
                                 style={'textAlign':'justify', 'margin-left':'20px'}),    
                    ],),
                ],),
                dbc.Col([
                    dbc.Row([
                        html.Div( className="app-header", style={'background-image':'url("https://cdn.pixabay.com/photo/2017/03/01/18/14/batteries-2109241_1280.png")',
             'background-size': '60vh', 'background-repeat':'no-repeat',
          'background-position':'center top', 'height':'50vh', 'margin-bottom':'60px'}),
                    ],),
                    dbc.Row([
                        html.Div( className="app-header", style={'background-image':'url("https://cdn.pixabay.com/photo/2017/03/01/18/14/batteries-2109241_1280.png")',
             'background-size': '40vh', 'background-repeat':'no-repeat',
          'background-position':'center top', 'height':'50vh', 'margin-bottom':'2px'}),
                    ],),
                    dbc.Row([
                        html.Div( className="app-header", style={'background-image':'url("https://dl.dropboxusercontent.com/scl/fi/04eebykwg2dgxfr4o2bns/voltage-curve.png?rlkey=1iwh8vmh9cuax2r41gspsvopf&raw=1")',
             'background-size': '60vh', 'background-repeat':'no-repeat',
          'background-position':'center top', 'height':'50vh'}),
                   ],),
                    dbc.Row([
                        dcc.Markdown(dangerously_allow_html=True, mathjax=True, children=('$$Q_{grav}=\\frac{nF*1000}{M_{W}*3600}$$'), style={'margin':'20px','font-size':'200%'}),
                   ],),
                ],),
             ],),
            html.Span(id='result', style={"font-size":"150%", "color":"red"}),
                    ],
                    style={"margin-left":"80px","margin-top":"40px"},
                    ),

    elif tab=='NP':
        module = ['Single cell', 'Series-connected module', 'Parallel-connected module']
        return html.Div([
            html.Br(),
            html.H1(('Single Cell Calculator'), style={'textAlign':'center', 'font-weight':'bold'}),
            html.Br(),
            html.Br(),
            html.H4(('- Calculating and plotting of the Li-ion battery cell properties using the measured/estimated input parameters'), 
                    style={'textAlign':'left', 'margin-left':'80px'}),
            html.Br(),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    dbc.Row([
                        html.Br(),
                        html.Br(),
                        html.H4('Positive Electrode Parameters', style={"margin-bottom":"0em", "color":"red"}),
                        html.Div([html.P('Electrode density (g/cm3)', style={"height": "auto", "margin-bottom": "auto"}),
                            dcc.Input(id="input-m", type="number", value='0.5', step='0.001', style={"margin-bottom":"1em"}) ]),
                        html.Div([html.P('Electrode thickness (um)', style={"height": "auto", "margin-bottom": "auto"}),
                            dcc.Input(id="input-n", type="number", value='50', step='0.01', style={"margin-bottom":"1em"}) ]),                      
                        html.Div([html.P('Active material loading ratio', style={"height": "auto", "margin-bottom": "auto"}),
                            dcc.Input(id="input-o", type="number", value='0.8', step='0.01', style={"margin-bottom":"1em"}) ]),
                        html.Div([html.P('Discharge capacity of active material (mAh/g)', style={"height": "auto", "margin-bottom": "auto"}),
                            dcc.Input(id="input-p", type="number", value='150', step='0.1', style={"margin-bottom":"1em"}) ]),
                        html.Div([html.P('Electrode area (mm2)', style={"height": "auto", "margin-bottom": "auto"}),
                            dcc.Input(id="input-q", type="number", value='1500', step='0.01', style={"margin-bottom":"1em"}) ]),
                        html.Div([html.P('Number of layers', style={"height": "auto", "margin-bottom": "auto"}),
                            dcc.Input(id="input-r", type="number", value='5', step='1', style={"margin-bottom":"1em"}) ]),
                        html.Br(),
                        html.Br(),
                    ],
                    style={"margin-left":"80px", "border": "black solid", "border-width":"3px", "border-radius":"15px"},
                    ),
                     dbc.Row([
                        html.H4('Other parameters', style={"margin-bottom":"0.5em", "color":"Purple"}),
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
                    style={"margin-left":"80px","margin-top":"25px", "border": "black solid", "border-width":"3px", "border-radius":"15px"},
                    ),
                ],
                style={'textAlign':'center'},
                ),
                dbc.Col([
                    html.Br(),
                    html.Br(),
                    dbc.Row([
                        html.H4('Negative Electrode Parameters', style={"margin-bottom":"1em", "color":"blue"}),
                        html.Div([html.P('Electrode density (g/cm3)', style={"height": "auto", "margin-bottom": "auto"}),
                            dcc.Input(id="input-i", type="number", value='2', step='0.001', style={"margin-bottom":"1em"}) ]),
                        html.Div([html.P('Electrode thickness (um)', style={"height": "auto", "margin-bottom": "auto"}),
                            dcc.Input(id="input-j", type="number", value='50', step='0.01', style={"margin-bottom":"1em"}) ]),                      
                        html.Div([html.P('Active material loading ratio', style={"height": "auto", "margin-bottom": "auto"}),
                            dcc.Input(id="input-k", type="number", value='0.9', step='0.01', style={"margin-bottom":"1em"}) ]),
                        html.Div([html.P('Discharge capacity of active material (mAh/g)', style={"height": "auto", "margin-bottom": "auto"}),
                            dcc.Input(id="input-l", type="number", value='500', step='0.1', style={"margin-bottom":"1em"}) ]),
                        html.Div([html.P('Electrode area (mm2)', style={"height": "auto", "margin-bottom": "auto"}),
                            dcc.Input(id="input-w", type="number", value='1000', step='0.01', style={"margin-bottom":"1em"}) ]),
                            
                        html.Br(),
                        html.Br(),
                        ],
                        style={"margin-left":"20px","margin-right":"20px", "border": "black solid", "border-width":"3px", "border-radius":"15px"},
                        ),
                    html.Br(),
                    dbc.Row([
                        dbc.Col(html.Span(id='outcome3', style={"font-size": "150%", "color": "red", "margin-top": "2em",
                                                "border": "3px magenta solid", "width": "100%",
                                                "justify": "center", "text-align": "center"})),
                                                ],
                                                style = {"margin-top":"6em"}
                                                ),
                    html.Br(),
                    dbc.Row([
                        dbc.Col(html.Span(id='outcome4', style={"font-size": "150%", "color": "purple", "margin-top": "1em",
                                                "border": "3px orange solid", "width": "100%", "justify": "center",
                                                "text-align": "center"})),
                    ],
                ),
                ],
                style={'textAlign':'center'},
                ),
                dbc.Col([
                    dbc.Row([
                    dcc.Graph(id='plot3', style={"width":"100vh", "height":"50vh","margin-top":"0px"})
                    ],),
                    dbc.Row([
                    dcc.Graph(id='plot4', style={"width":"100vh", "height":"50vh","margin-top":"0px"})
                    ],),
            ],),
            html.Br(),
            html.Br(),
            html.H1(('Pack Calculator'), style={'textAlign':'center', "font-weight":"bold", "margin-top":"2em", "margin-bottom":"1em"}),
            html.Br(),
            html.Br(),
            html.H4(('- Generating simple estimated calculation of the pack-level performance of the cell above'), 
                    style={'textAlign':'left', 'margin-left':'80px'}),
            dbc.Row([
                dbc.Col([
                    dbc.Row([
                        html.Br(),
                        html.Br(),
                        html.H4('Parameters', style={"margin-bottom":"0em", "color":"red"}),
                        html.Div(children=[
                                html.Label('Module Type'),dcc.Dropdown(
                                    id='dropdown', style={'margin':'auto','maxWidth':'80%','width':'50%'}, 
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
            style={"margin-left":"120px","margin-top":"40px","margin-right":"20px", "border": "black solid", "border-width":"3px", "border-radius":"15px"},
                ),
            ],
            style={'textAlign':'center'}, align='center'
            ),
            dbc.Col([
                dbc.Row([
            html.Br(),
            html.Br(),
            html.Span(id='outcome5', style={"font-size":"150%", "color":"blue","margin-top":"2em"}),
            html.Span(id='outcome6', style={"font-size":"150%", "color":"blue","margin-top":"2em"}),
            html.Span(id='outcome7', style={"font-size":"150%", "color":"red","margin-top":"2em"}),
            html.Span(id='outcome8', style={"font-size":"150%", "color":"red","margin-top":"2em"}),
            #html.Span(id='outcome8', style={"font-size":"150%", "color":"red","margin-top":"2em", "border":"3px orange solid"}),
               ],
            style={"margin-left":"80px","margin-top":"40px"},
                ),
            ],
            style={'textAlign':'center'},
            ),
            ],
        ),
        ],
        ),
        ],
        )
    elif tab=='cells':
        return html.Div([
            html.Br(),
            html.Br(),
            html.H1(('Li cell performance predictor'), style={'textAlign':'center'}),
            dbc.Row([
            dbc.Col([
                    dbc.Row([
            html.Div([html.P('Coulombic Efficiency (%)', style={"height": "auto", "margin-bottom": "auto"}),
                      dcc.Input(id="input-f", type="number", value='95', step='0.1', style={"margin-bottom":"1em"}) ]),
            html.Div([html.P('Capacity Retention (%)', style={"height": "auto", "margin-bottom": "auto"}),
                   dcc.Input(id="input-g", type="number", value='80', step='0.1', style={"margin-bottom":"1em"}) ]),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Span(id='outcome', style={"font-size":"150%", "color":"red"}),
                    ],
                    style={"margin-left":"80px","margin-top":"100px"},
                    ),
            ],),
            dbc.Col([
                dbc.Row([
            dcc.Graph(id='plot', style={"width":"120vh", "height":"70vh","margin-top":"0px"})
                ],),
            ],),
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
            html.Br(),
            html.Br(),
            html.Span(id='outcome2', style={"font-size":"150%", "color":"red"}),
                    ],
                    style={"margin-left":"80px","margin-top":"100px"},
                    ),
            ],),
            dbc.Col([
                dbc.Row([
            dcc.Graph(id='plot2', style={"width":"120vh", "height":"70vh","margin-top":"0px"})
                ],),
            ],),
            ],),
            ],
        )
@app.callback([Output('result', 'children'), Output('graph','figure')],
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
                size=18,
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

@app.callback([Output('outcome', 'children'), Output('outcome2', 'children'), Output('plot','figure'), Output('plot2','figure')],
                [Input('input-f', 'value'),
                Input('input-g', 'value'),
                Input('input-h', 'value')  
                ], 
            )
def update_content(input_f, input_g, input_h):
    if input_f is not None and input_g is not None and input_h is not None:
        outcome = np.log10(float(input_g)/100)/np.log10(float(input_f)/100)
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
            plot_bgcolor='white',
            title="Coulombic Efficiency vs Cycle Number",
            title_x=0.5,
            xaxis_title="Coulombic Efficiency (%)",
            yaxis_title="Cycle Numbers",
            font=dict(
                family="arial, monospace",
                size=18,
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
            plot_bgcolor='white',
            title="Coulombic Efficiency vs Capacity Retention",
            title_x=0.5,
            xaxis_title="Coulombic Efficiency (%)",
            yaxis_title="Capacity Retention (%)",
            font=dict(
                family="arial, monospace",
                size=18,
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
        return "The cell is expected to undergo {} cycles".format(round(outcome,2)), \
                "The cell is expected to have {} % capacity retention".format(round(outcome2,2)), \
                fig2, fig3
    else:
        return "", "", {}, {}

@app.callback([Output('outcome3', 'children'), Output('outcome4', 'children'), Output('outcome5', 'children'), 
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
        np_ratio="NP ratio calculated is {}".format(round(outcome3,2))
        cell_capacity="Cell capacity calculated is {} Ah".format(round(outcome4,2))
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
            plot_bgcolor='white',
            title="Cell Dimension vs Energy Density",
            title_x=0.5,
            xaxis_title="Cathode loading (g/cm2)",
            yaxis_title="Cell energy density (Wh/kg)",
            font=dict(
                family="arial, monospace",
                size=18,
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
            plot_bgcolor='white',
            title="Cell Dimension vs Energy Density",
            title_x=0.5,
            xaxis_title="Cathode area capacity (mAh/cm2)",
            yaxis_title="Cell energy density (Wh/kg)",
            font=dict(
                family="arial, monospace",
                size=18,
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
        

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'check, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run_server(debug=True, host='127.0.0.1',port=8050)

