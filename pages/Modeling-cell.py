import os
import numpy as np
import dash
from dash import Dash, dcc, html, Input, Output, State, callback, dash_table
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
import plotly.express as px
import dash_mantine_components as dmc
from dash.exceptions import PreventUpdate
import math
import pandas as pd

dash.register_page(
    __name__, name="CP Modeling", top_nav=True, path="/modeling-cells"
)

tabs_styles={
     'borderBottom': '1px solid #d6d6d6',
     'padding':'14px',
     'fontWeight':'bold',
     'backgroundColor':'rgb(234, 228, 228)',
     'font-size':'20px',
 }

tab_selected_style = {
     'borderTop':'3px solid rgb(60,28,204)',
     'borderBottom':'1px solid lightgray',
     'backgroundColor':'rgb(234, 228, 228)',#'#119DFF',
     'color':'black',
     'fontWeight':'bold',
     'padding':'14px',
     'font-size':'20px'
     }



tab1 = dbc.Container([
    dbc.Row([
    dcc.Markdown('* Estimation of Cycle Life', style={'marginTop':'40px','font-size':'25px','textAlign':'left','font-weight':'bold'}),
    dcc.Markdown(" This calculation estimates the cycle life when cell cycles at a specific columbic efficiency each cycle (Option1) or estimates the required coulombic efficiency to achieve achieve a target cycle life (Option2)."),
    dcc.Markdown(" This calculation assumes that the coulombic efficiency is maintained throughout the entire cycle. This estimation therefore provides an upper bound on cycle life (Option1) and a lower bound on coulombic efficiency (Option2)."),
    dcc.Dropdown({ 'Opt1': 'Option1: Cycle Life','Opt2':'Option2: Required CE'}, value="Opt1",id='Opts', 
                 clearable=False, style={'width':'50%'}),
    html.Div(id="output-container"),
    ],
    style={'textAlign':'justify', 'margin-left':'30px', 'margin-right':'30px'},
    ),
    html.Br(),
    dmc.Divider(size="md", color="grey"),
    html.Br(),
    dbc.Row([
        dcc.Markdown('* Estimation of Li-metal thickness', style={'marginTop':'40px','font-size':'25px','textAlign':'left','font-weight':'bold'}),
        dcc.Markdown(" This calculation estimates the amount of Li deposition or exfoliation during charge/discharge reactions depending on the applied areal current density."),
        dcc.Markdown(" Note that this is theoretical estimation and calculated by assuming perfectly flat and smooth film of Li. "),
        dbc.Col([
                html.Div([html.P('Li Areal Capacity [mAh/cm\u00b2]', style={"height": "auto", "margin-bottom": "auto"}),
                dcc.Input(id="liarealcap", type="number", value='3',step='0.1',style={"margin-bottom":"1em"})]),
                html.Span(id='thickness_outcome', style={"font-size":"120%", "color":"black","font-weight":"bold"}),
            ], style={"margin-top":"50px"}, width={"size":"6"},
                xs=12, sm=12, md=10, lg=5, xl=5,
            ),
        dbc.Col([
                dcc.Graph(id='thicknessplot', style={"width":"80vh", "height":"50vh","margin-top":"0px"})
        ], width={"size":"6"},xs=12, sm=12, md=10, lg=5, xl=5,
        ),

    ],
    style={'textAlign':'justify', 'margin-left':'30px', 'margin-right':'30px'},
    ),
]),
tab2= dbc.Container([
    dbc.Row([
        dcc.Markdown('* Estimation of Pouch Cell Capacity and Energy Density', style={'marginTop':'40px','font-size':'25px','textAlign':'left','font-weight':'bold'}),
        dcc.Markdown(" This estimates the total cell capacity and eneryg density of the pouch cells."),
        dcc.Markdown(" This calculation can support in pouch cell design. For example, with a designed electrode, this modeling can determine the number of stack layers and electrolyte amount to achive target cell apacity and energy density."),
        dcc.Markdown(" Electrode Parameters:  ", style={'marginTop':'20px','font-size':'20px','textAlign':'left','font-weight':'bold'}),
        dbc.Col([
                    dbc.Row([
                        html.Br(),
                        html.Br(),
                        html.H5('Cathode Parameters', style={"margin-bottom":"0em", "color":"red"}),
                        html.Div([html.P(["Electrode density [g/cm",html.Sup("3"),"]"],style={"height": "auto", "margin-bottom": "auto"}),
                            dcc.Input(id="c_ed", type="number", value='3.0', step='0.1', style={"margin-bottom":"1em"}) ]),
                        html.Div([html.P('Electrode thickness [\u03bcm]', style={"height": "auto", "margin-bottom": "auto"}),
                            dcc.Input(id="c_et", type="number", value='70', step='0.01', style={"margin-bottom":"1em"}) ]),                      
                        html.Div([html.P(['Active material loading ratio'], style={"height": "auto", "margin-bottom": "auto"}),
                            dcc.Input(id="c_amlr", type="number", value='0.96', step='0.01', style={"margin-bottom":"1em"}) ]),
                        html.Div([html.P(['Practical capacity of active material [mAh/g]'], style={"height": "auto", "margin-bottom": "auto"}),
                            dcc.Input(id="c_pcam", type="number", value='185', step='0.1', style={"margin-bottom":"1em"}) ]),
                        html.Div([html.P(['Electrode area [cm',html.Sup("2"),']'],style={"height": "1.3em", "margin-bottom": "auto"}),
                            dcc.Input(id="c_ea", type="number", value='19.44', step='0.01', style={"margin-bottom":"1em"}) ]),
                        #html.Div([html.P('Number of layers', style={"height": "auto", "margin-bottom": "auto"}),
                        #    dcc.Input(id="input-r", type="number", value='5', step='1', style={"margin-bottom":"1em"}) ]),
                        html.Br(),
                        html.Br(),
                        ],
                    style={'textAlign':'left'},
                    ),
                ],width={"size":4},
                xs=6, sm=6, md=6, lg=4, xl=4,
        ),
        dbc.Col([
                    dbc.Row([
                        html.H5('Anode Parameters', style={"margin-bottom":"1em", "color":"blue"}),
                        html.Div([html.P(["Electrode density [g/cm",html.Sup("3"),"]"],style={"height": "auto", "margin-bottom": "auto"}),
                            dcc.Input(id="a_ed", type="number", value='0.534', step='0.001', style={"margin-bottom":"1em"}) ]),
                        html.Div([html.P('Electrode thickness [\u03bcm]', style={"height": "auto", "margin-bottom": "auto"}),
                            dcc.Input(id="a_et", type="number", value='50', step='0.01', style={"margin-bottom":"1em"}) ]),                      
                        html.Div([html.P('Active material loading ratio', style={"height": "auto", "margin-bottom": "auto"}),
                            dcc.Input(id="a_amlr", type="number", value='1.0', step='0.01', style={"margin-bottom":"1em"}) ]),
                        html.Div([html.P('Practical capacity of active material [mAh/g]', style={"height": "auto", "margin-bottom": "auto"}),
                            dcc.Input(id="a_pcam", type="number", value='3860', step='0.1', style={"margin-bottom":"1em"}) ]),
                        html.Div([html.P(['Electrode area [cm',html.Sup("2"),']'],style={"height": "1.3em", "margin-bottom": "auto"}),
                            dcc.Input(id="a_ea", type="number", value='19.44', step='0.01', style={"margin-bottom":"1em"}) ]),        
                        html.Br(),
                        html.Br(),
                        ],
                        style={'textAlign':'left'},
                        ),
                        ],
                width={"size":4}, #style={'margin-left':'5px'},
                xs=6, sm=6, md=6, lg=4, xl=4,
            ),
        dbc.Col([   
                    dbc.Row([
                        html.H5('Other parameters', style={"margin-bottom":"0.5em", "color":"Purple"}),
                        html.Div([html.P('Al foil thickness [\u03bcm]', style={"height": "auto", "margin-bottom": "auto"}),
                            dcc.Input(id="Al_t", type="number", value='12', step='1.0', style={"margin-bottom":"1em"}) ]),
                        html.Div([html.P('Cu foil thickness [\u03bcm]', style={"height": "auto", "margin-bottom": "auto"}),
                            dcc.Input(id="Cu_t", type="number", value='8', step='1.0', style={"margin-bottom":"1em"}) ]),                      
                        html.Div([html.P('Tab area [mm\u00b2]', style={"height": "auto", "margin-bottom": "auto"}),
                            dcc.Input(id="area_tap", type="number", value='25', step='1.0', style={"margin-bottom":"1em"}) ]),
                        html.Div([html.P(['Total seperator weight [g]'], style={"height": "auto", "margin-bottom": "auto"}),
                            dcc.Input(id="S_w", type="number", value='0.5', step='0.1', style={"margin-bottom":"1em"}) ]),
           
                        ],
                    style={'textAlign':'left'},
                    ),
                    ], 
                width={"size":3}, style={'margin-left':'5px'},
                xs=6, sm=6, md=6, lg=3, xl=3,
                ),
        dcc.Markdown(" Cell Parameters:  ", style={'marginTop':'10px','font-size':'20px','textAlign':'left','font-weight':'bold'}),
        dbc.Row([
        dbc.Col([
            html.H6('Type of stacked layer and its unit:'),
            dcc.Dropdown({ 't1': 'Type1','t2':'Type2','t3':'Type3'}, value="t1",id='stacktype', 
                         clearable=False, style={"height": "auto","width":"150px", "margin-bottom": "auto","margin-top":"30px"}),

            html.Div( html.Img(src='https://dl.dropboxusercontent.com/scl/fi/t0l93yiboq194etmscnvu/stack_type.png?rlkey=r4fuiabrdlqtl7rxvqnqokd6e&st=za7if4yl&raw=1', style={"width":"100%", "display": "block", "margin": "auto"}), 
                ),
            
           ], width={"size":5}, #style={'margin-left':'5px'},
                xs=6, sm=6, md=6, lg=4, xl=5,
           ),
        dbc.Col([

            html.Div([html.P(['Sum of other package weight [g]',html.Sup("*1")], style={"height": "auto", "margin-bottom": "auto"}),
                dcc.Input(id="other_packageweight", type="number", value='1.1', step='0.1', style={"margin-bottom":"1em"}) ]),
            html.Div([html.P('Nominal cell voltage [V]', style={"height": "auto", "margin-bottom": "auto"}), 
                dcc.Input(id="nom_v", type="number", value='3.7', step='0.1', style={"margin-bottom":"1em"}) ]),
            html.Div([html.P('Number of stacked layer', style={"height": "auto", "margin-bottom": "auto"}),
                dcc.Input(id="stacked_layer", type="number", value='7', step='1', style={"margin-bottom":"1em"}) ]),    
            html.H6(["Target Energy Density [Wh/Kg]",html.Sup("*2")], style={'marginTop':'10px','font-size':'20px','textAlign':'left','font-weight':'bold'}),
            dcc.Input(id="target_ed",type="number", value='300', step='5', style={"margin0bottom":"1em", 'width':"200px",'margin-left':'0px'}),   
 
            
           ], width={"size":4}, style={'margin-left':'5px'},
                xs=6, sm=6, md=6, lg=4, xl=4,
           ),
        
        dbc.Col([
                html.H5("Cell Summary", style={'textAlign':'center','font-weight':'bold'}),
                html.Div(id="summary_table", style={"margin-top":"30px"})
            ],width={"size":4}, #style={'margin-left':'5px'},
                xs=6, sm=6, md=6, lg=3, xl=3,
            ),
    ]),
        dcc.Markdown("*1 A sum of other package weights includes the total weight of tabs and the packaging case."),
        dcc.Markdown("*2 If the total cell capacity is insufficient to include the electrolyte weight in the total cell weight to reach the target energy density, this target energy density is reset according to EC ratio = 1.3 (g/Ah)(referenced Panasonic 18650B EC ratio)."),
        dbc.Row([

            dbc.Col([
                html.H5("Weight distribution of different cell components", style={'textAlign':'center','font-weight':'bold'}),
                dcc.Graph(id='pie1', style={"width":"100%", "height":"50vh","margin-top":"30px"})
                ],
            width={"size":"6"},xs=12, sm=12, md=12, lg=5, xl=5,                    
            ),
            dbc.Col([    
                html.H5(" Energy Density vs Amount of Electrolyte", style={'textAlign':'center','font-weight':'bold'}),
                dcc.Graph(id='ed_plot', style={"width":"100%","height":"50vh","margin-top":"30px", "margin-bottom":"30px"})
                ],width={"size":"6"},xs=12, sm=12, md=12, lg=6, xl=6,
            ),
        ],style=({'textAlign':'justify', 'margin-left':'30px', 'margin-right':'30px','margin-top':'30px'}),),
    ],),
]),

tab3= dbc.Container([
        dbc.Row([
        dcc.Markdown("* Estimation of Jelly-roll capacity and required electrode dimension", style={'marginTop':'40px','font-size':'25px','textAlign':'left','font-weight':'bold'}),
        dcc.Markdown('This calculator can be used to compute the metrics for the cylindrical cell consisting of a jelly-roll of cathode, anode, and separator sheets.'),
        dcc.Markdown('This module calculates the electrode length required for customized cell components dimensions to fit the cylindrical cell case dimensions.'),
        dcc.Markdown('By knowing the outer and inner diameters, which are determined based on the cylindrical cell case, the cylindrical cell electrode length can be calculated using the Archimedean sppral using polar coordinates using the following equation:'),
        dcc.Markdown('- For the electrode length:', style={'textAlign':'left', 'font-size':'20px','font-weight':'bold','margin-left':'40px'}),
        dcc.Markdown('''$$
                        L=\\frac{a}{2\pi}(\\frac{\phi_{1}}{2}\\sqrt{\phi_{1}^2+1}+\\frac{1}{2}ln(\phi_{1}+\\sqrt{\phi_{1}^2+1})-\\frac{\phi_{0}}{2}\\sqrt{\phi_{0}^2+1}-\\frac{1}{2}ln(\phi_{0}+\\sqrt{\phi_{0}^2+1}))
                        $$
                        ''', mathjax=True, style={'textAlign':'left','font-size':"20px"}),
        dcc.Markdown(('- Number of windings:'), style={'textAlign':'left', 'font-size':'20px', 'font-weight':'bold','margin-left':'40px'}),
        dcc.Markdown('''$$
                        Nw=\\frac{\phi_{1}-\phi_{0}}{2\pi}
                        $$
                        ''', mathjax=True, style={'textAlign':'left','font-size':"20px"}),
        dcc.Markdown('where $$\phi$$ = rotation angle and $$a$$ = electrode thickness (double-sided cathode thickness + double-sided anode thickness + 2*separator thickness)', mathjax=True, style={'textAlign':'left', 'font-size':'18px', 'font-weight':'bold', 'margin-left':'50px'}),              
        dcc.Markdown('Note: cell outer diameter = $$\\frac{a}{\pi}\phi_{1}$$ & cell inner diameter = $$\\frac{a}{\pi}\phi_{0}$$', mathjax=True, style={'textAlign':'left', 'font-size':'18px', 'margin-left':'50px'}),              
        html.Br(),          
    ]),

  dbc.Row([
                dbc.Col([
                    dbc.Row([
                        html.Br(),
                        html.Br(),
                        html.Div(html.Img(src='https://www.dropbox.com/scl/fi/l4b853tep0e9r52k7oun1/cylindrical-spiral_wcaption.png?rlkey=noe3s94xw0p7rxkhx772b53l9&raw=1', style={"width":"120%", "margin-bottom":"20px"})), 
                        html.Br(),
                        html.Br(),
                        ],
                    style={'textAlign':'center'},
                    ),
                ],width={"size":4},
                xs=6, sm=8, md=6, lg=3, xl=4,
                ),
                dbc.Col([
                    dbc.Row([
                        html.Br(),
                        html.Br(),
                        html.H5('Cathode Parameters', style={"margin-bottom":"0em", "color":"red"}),
                        html.Div([html.P('Coating thickness (Single-side) (um)', style={"height": "auto", "margin-bottom": "auto"}),
                            dcc.Input(id="jinput-c1", type="number", value='60', step='0.001', style={"margin-bottom":"1em"}) ]),
                        html.Div([html.P('Al foil thickness (um)', style={"height": "auto", "margin-bottom": "auto"}),
                            dcc.Input(id="jinput-c2", type="number", value='15', step='0.1', style={"margin-bottom":"1em"}) ]),
                        html.Div([html.P('Discharge capacity of active material (mAh/g)', style={"height": "auto", "margin-bottom": "auto"}),
                            dcc.Input(id="jinput-c3", type="number", value='200', step='0.1', style={"margin-bottom":"1em"}) ]),                        
                        html.Div([dcc.Markdown('Density of electrode material (g/cm<sup>3</sup>)', dangerously_allow_html=True, style={"height": "1.3em", "margin-bottom": "auto"}),
                            dcc.Input(id="jinput-c4", type="number", value='4.87', step='0.01', style={"margin-bottom":"1em"}) ]),
                        html.Div([html.P('Active material loading ratio', style={"height": "auto", "margin-bottom": "auto"}),
                            dcc.Input(id="jinput-c5", type="number", value='0.95', step='0.01', style={"margin-bottom":"1em"}) ]),
                        html.Div([html.P('Estimated porosity', style={"height": "auto", "margin-bottom": "auto"}),
                            dcc.Input(id="jinput-c6", type="number", value='0.2', step='0.01', style={"margin-bottom":"1em"}) ]),
                        html.Div([html.P('Electrode width (cm)', style={"height": "auto", "margin-bottom": "auto"}),
                            dcc.Input(id="jinput-c7", type="number", value='5', step='0.01', style={"margin-bottom":"1em"}) ]),
                        html.Br(),
                        html.Br(),
                        ],
                    style={'textAlign':'center'},
                    ),
                ],width={"size":4},
                xs=6, sm=8, md=6, lg=5, xl=4,
                ),
                dbc.Col([   
                    dbc.Row([
                        html.H5('Other cell parameters', style={"margin-bottom":"0.5em", "color":"Purple"}),
                        html.Div([html.P('Anode coating thickness (Single-side) (um)', style={"height": "auto", "margin-bottom": "auto"}),
                            dcc.Input(id="jinput-c8", type="number", value='50', step='0.01', style={"margin-bottom":"1em"}) ]),                      
                        html.Div([html.P('Cu foil thickness (um)', style={"height": "auto", "margin-bottom": "auto"}),
                            dcc.Input(id="jinput-c9", type="number", value='10', step='0.1', style={"margin-bottom":"1em"}) ]),                      
                        html.Div([html.P('Separator thickness (um)', style={"height": "auto", "margin-bottom": "auto"}),
                            dcc.Input(id="jinput-c10", type="number", value='25', step='0.1', style={"margin-bottom":"1em"}) ]),
                        html.Div([html.P('Outer diameter of the cell (mm)', style={"height": "auto", "margin-bottom": "auto"}),
                            dcc.Input(id="jinput-c11", type="number", value='45', step='0.001', style={"margin-bottom":"1em"}) ]),              
                        html.Div([html.P('Cell Can thickness (mm)', style={"height": "auto", "margin-bottom": "auto"}),
                            dcc.Input(id="jinput-c12", type="number", value='1.5', step='0.001', style={"margin-bottom":"1em"}) ]),              
                        html.Div([html.P('Inner diameter of the cell (mm)', style={"height": "auto", "margin-bottom": "auto"}),
                            dcc.Input(id="jinput-c13", type="number", value='2', step='0.001', style={"margin-bottom":"1em"}) ]),                                
                        html.Br(),
                        html.Br(),
                        ],
                    style={'textAlign':'center'},
                    ),
                    ], 
                width={"size":4}, style={'margin-left':'0px'},
                xs=6, sm=8, md=6, lg=5, xl=4,
                ),
            ]),
            dbc.Col([
                    dbc.Row([
                        html.Br(),
                        html.Br(),
                        html.Span(id='joutcome9', style={"font-size":"150%", "color":"blue","margin-top":"2em"}),
                        html.Span(id='joutcome10', style={"font-size":"150%", "color":"blue","margin-top":"0em"}),
                        html.Span(id='joutcome11', style={"font-size":"150%", "color":"red","margin-top":"0em"}),
                        html.Span(id='joutcome12', style={"font-size":"150%", "color":"red","margin-top":"0em"}),
                        ],
                        style={"margin-left":"80px","margin-top":"40px"},
                    ),
                    ],
                    style={'textAlign':'center'}, 
                width={"size":"12"},
                xs=8, sm=10, md=10, lg=12, xl=12,
            ),   
    
#         dcc.Markdown(" Input Parameters:  ", style={'marginTop':'20px','font-size':'20px','textAlign':'left','font-weight':'bold'}),
#         dbc.Row([
#                 dbc.Col([
#                     dbc.Row([
#                         html.Br(),
#                         html.Br(),
#                         html.Div(html.Img(src='https://dl.dropboxusercontent.com/scl/fi/l4b853tep0e9r52k7oun1/cylindrical-spiral_wcaption.png?rlkey=noe3s94xw0p7rxkhx772b53l9&raw=1', style={"width":"120%", "margin-bottom":"20px"})), 
#                         html.Br(),
#                         html.Br(),
#                         ],
#                     style={'textAlign':'center'},
#                     ),
#                 ],width={"size":4},
#                 xs=6, sm=8, md=6, lg=3, xl=4,
#                 ),
#             ]
#         ),

#         dbc.Col([
#             dbc.Row([
#                 html.H5('Parameters for Capacity', style={"margin-bottom":"0em", "color":"blue"}),
#                 html.Div([html.P(["Cathode density [g/cm",html.Sup("3"),"]"],style={"height": "auto", "margin-bottom": "auto",'margin-top':'10px'}),
#                 dcc.Input(id="jc_ed", type="number", value='3.0', step='0.1', style={"margin-bottom":"1em"}) ]),
#                 html.Div([html.P(["Anode density [g/cm",html.Sup("3"),"]"],style={"height": "auto", "margin-bottom": "auto"}),
#                     dcc.Input(id="ja_ed", type="number", value='3.0', step='0.1', style={"margin-bottom":"1em"}) ]),
#                 html.Div([html.P(['Cathode practical capacity [mAh/g]'], style={"height": "auto", "margin-bottom": "auto",'margin-top':'10px'}),
#                     dcc.Input(id="jc_pcam", type="number", value='185', step='0.1', style={"margin-bottom":"1em"}) ]),
#                 html.Div([html.P(['Anode practical capacity [mAh/g]'], style={"height": "auto", "margin-bottom": "auto"}),
#                 dcc.Input(id="ja_pcam", type="number", value='185', step='0.1', style={"margin-bottom":"1em"}) ]),

#             ],style={'textAlign':'left','margin-top':'20px'},
#             ),

#         ],width={"size":4},
#         xs=6, sm=6, md=6, lg=4, xl=4,
#         ),
    
#         dbc.Col([
#             dbc.Row([
#                 html.H5('Case and Other Parameters', style={"margin-bottom":"0em", "color":"purple"}),
#                 html.Div([html.P('Outer diameter of the cell [mm]', style={"height": "auto", "margin-bottom": "auto",'margin-top':'10px'}),
#                 dcc.Input(id="input-c11", type="number", value='45', step='0.001', style={"margin-bottom":"1em"}) ]),              
#                 html.Div([html.P('Cell Can thickness [mm]', style={"height": "auto", "margin-bottom": "auto"}),
#                 dcc.Input(id="input-c12", type="number", value='1.5', step='0.001', style={"margin-bottom":"1em"}) ]),              
#                 html.Div([html.P('Inner diameter of the cell [mm]', style={"height": "auto", "margin-bottom": "auto"}),
#                 dcc.Input(id="input-c13", type="number", value='2', step='0.001', style={"margin-bottom":"1em"}) ]), 
                
#                 html.Div([html.P('Al foil thickness [\u03bcm]', style={"height": "auto", "margin-bottom": "auto"}),
#                 dcc.Input(id="jAl_t", type="number", value='12', step='1.0', style={"margin-bottom":"1em"}) ]),
#                 html.Div([html.P('Cu foil thickness [\u03bcm]', style={"height": "auto", "margin-bottom": "auto"}),
#                 dcc.Input(id="jCu_t", type="number", value='12', step='1.0', style={"margin-bottom":"1em"}) ]),
#                 html.Div([html.P('Separator thickness [um]', style={"height": "auto", "margin-bottom": "auto"}) ,
#                 dcc.Input(id="jse_w", type="number", value='25', step='0.1', style={"margin-bottom":"1em"}) ]),
#                 ],style={'textAlign':'left','margin-top':'20px'},
                
#             ),
#         ],width={"size":4},
#         xs=6, sm=6, md=6, lg=4, xl=4,),
        
#     ],style={'textAlign':'justify','margin-left':'30px','margin-right':'30px','margin-buttom':'30px'},
#     ),
# dbc.Row([
#         dbc.Col([
#             dbc.Row([
#                 html.Br(),
#                 html.Br(),
#                 html.Div(html.Img(src='https://www.dropbox.com/scl/fi/l4b853tep0e9r52k7oun1/cylindrical-spiral_wcaption.png?rlkey=noe3s94xw0p7rxkhx772b53l9&raw=1', style={"width":"120%", "margin-bottom":"20px",'margin-top':"50px"})), 
#                 html.Br(),

#                 ], style={'textAlign':'center'},
#                 ),
#         # dbc.Row([
#         #     html.H5("Jelly-roll Summary", style={'textAlign':'center','font-weight':'bold'}),
#         #     html.Div(id="jsummary_table", style={"margin-top":"30px"})
#         # ])
#             ],width={"size":6},
#             xs=12, sm=12, md=12, lg=4, xl=4,
#         ),

#         dbc.Col([
#             dbc.Row([
#                 html.Br(),
#                 html.Br(),
#                 html.Span(id='cathod_length', style={"font-size":"150%", "color":"blue","margin-top":"2em"}),
#                 html.Span(id='No_winding', style={"font-size":"150%", "color":"blue","margin-top":"0em"}),
#                 html.Span(id='areal_cap', style={"font-size":"150%", "color":"red","margin-top":"0em"}),
#                 html.Span(id='cell_cap', style={"font-size":"150%", "color":"red","margin-top":"0em"}),
#                     ],
#                     style={"margin-left":"80px","margin-top":"40px"},
#                 ),
#                 # html.H5("Electrode Length vs cylindrical cell dimension", style={'textAlign':'center','font-weight':'bold'}),
#                 # dcc.Graph(id='jellyroll_plot', style={"width":"100%","height":"50vh","margin-top":"30px", "margin-bottom":"30px"})
#             ],width={"size":6}, #style={'margin-left':'5px'},
#                 xs=12, sm=12, md=12, lg=4, xl=4,
#             ),
]),

layout = html.Div([
     dcc.Tabs(id="tabs", value='tab-1', parent_className='custom-tabs', className='custom-tabs-container', children=[
         dcc.Tab(label='A Single Cell',value='tab-1', style=tabs_styles, selected_style=tab_selected_style),
         dcc.Tab(label="Stacked Cell", id='tab-2', style=tabs_styles,selected_style=tab_selected_style),       
         dcc.Tab(label="Jelly-Roll Cell", id='tab-3', style=tabs_styles,selected_style=tab_selected_style),
         ]),
     html.Div(id='tabsclasses')
 ])

@callback(
       Output('tabsclasses','children'),
       Input('tabs', 'value')
 )

def render_content(tab):
    if tab == 'tab-1':
        return tab1  
    elif tab == 'tab-2':
        return tab2
    elif tab == 'tab-3':
        return tab3

cyclelife = html.Div([
    dbc.Row([
        dbc.Col([
            html.Br(),
            html.Br(),
            dcc.Markdown("Option 1: Estimiate Cycle Number ", style={'font-weight':'bold'}),
            html.Div([html.P('Coulombic Efficiency (%)', style={"height":"auto","margin-bottom":"auto"}),
            dcc.Input(id="input_zz", type="number",value="99", step="0.01", multiple=True, style={"margin-bottom":"1em"})]),
            html.Div([html.P('Capacity Retention (%)', style={"height":"auto","margin-bottom":"auto"}),
            dcc.Input(id="input_g", type="number", value="80", step="0.1", style={"margin-bottom":"1em"})]),
            html.Br(),
            html.Br(),
            html.Span(id="option1_outcome", style={"font-size":"120%", "font-weight":"bold"}),
            ],width={"size":"6"},xs=12,sm=12, md=10, lg=5, xl=5,
        ),
        dbc.Col([
            dcc.Graph(id='cyclelife',figure={}, style={"width":"80vh", "height":"50vh","margin-top":"0px"}),
        ], width={"size":"6"}, xs=12, sm=12, md=10, lg=5, xl=5),
    ]),
])
requiredCE = html.Div([
    dbc.Row([ 
        dbc.Col([
            html.Br(),
            html.Br(),
            dcc.Markdown("Option 2: Estimate required Coulombic Efficiency (%) to achieve N cycle life",style={'font-weight':'bold'}),
            html.Div([html.P('targeted capacity retention (%)', style={"height":"auto","margin-bottom":"auto"}),
            dcc.Input(id="input_cap2", type="number",value="80", step="0.01", multiple=True, style={"margin-bottom":"1em"})]),
            html.Div([html.P('targeted cycle life', style={"height":"auto","margin-bottom":"auto"}),
            dcc.Input(id="input_cycle", type="number", value="100", step="1", style={"margin-bottom":"1em"})]),
            html.Br(),
            html.Br(),
            html.Span(id="option2_outcome", style={"font-size":"120%", "font-weight":"bold"})
            ], width={"size":"6"},xs=12,sm=12, md=10, lg=5, xl=5,
        ),
        dbc.Col([
            dcc.Graph(id='CElife',figure={}, style={"width":"80vh", "height":"50vh","margin-top":"0px"}),
            ], width={"size":"6"}, xs=12, sm=12, md=10, lg=5, xl=5,
        ),  
    ])
])

    
@callback(
        Output('output-container','children'),
        Input('Opts', 'value')
)
def modeling_dropdown(op):
    if op == 'Opt1':
        return cyclelife
    elif op == 'Opt2':
        return requiredCE
    

def option1(zz,g):
    fig=go.Figure()
    opt1_cn= np.arange(1,3000,1)
    opt1_cap = np.power(float(zz)/100, opt1_cn)
    find_index = np.argmin(np.abs(np.array(opt1_cap)-(float(g)/100)))
    cycle_life = opt1_cn[find_index]
    cap = float(g)/100

    fig.add_trace(go.Scatter(x=opt1_cn, y=opt1_cap, mode='lines'))
        
    fig.add_trace(go.Scatter(x=[0,cycle_life], y=[0.8,0.8], mode='lines',line=dict(dash='dash',color="gray")))
    fig.add_trace(go.Scatter(x=[cycle_life, cycle_life], y=[0, 0.8], mode='lines',line=dict(dash='dash',color="gray")))
    fig.add_trace(go.Scatter(x=[cycle_life], y=[cap], mode='markers', marker_symbol='circle', marker_size=15))
    fig.update_layout(xaxis_range=[0,cycle_life+100])

    fig.update_layout(
        plot_bgcolor='rgb(234, 228, 228)',
        paper_bgcolor='rgb(211, 211, 211)',
        title=" Coulombic Efficiency vs Capacity Retention",
        title_x=0.5,
        xaxis_title="Cycle Number",
        yaxis_title="Capacity Retention",
        font=dict(
            family="arial, monospace",
            size=16,
            color="black"
        ),
        showlegend=False
    )
    return dcc.Markdown("The cell is expected to undergo **{}** cycles".format(cycle_life), dangerously_allow_html=True), fig


def option2(cap2, raw_cycle):
    cycle=float(raw_cycle)
    fig=go.Figure()
    req_CE = np.exp((np.log(float(cap2)/100))/cycle)
    cy_x = np.arange(cycle*0.2, cycle*1.5)
    ce_y = [np.exp((np.log(float(cap2)/100))/xval) for xval in cy_x ]
    y_0 = np.exp((np.log(float(cap2)/100))/cy_x[0])
    res_CE = req_CE*100
    fig.add_trace(go.Scatter(x=cy_x, y=ce_y, mode='lines'))
    fig.add_trace(go.Scatter(x=[cy_x[0],cycle], y=[req_CE,req_CE], mode='lines',line=dict(dash='dash',color="gray")))
    fig.add_trace(go.Scatter(x=[cycle, cycle], y=[y_0, req_CE], mode='lines',line=dict(dash='dash',color="gray")))
    fig.add_trace(go.Scatter(x=[cycle], y=[req_CE], mode='markers', marker_symbol='circle', marker_size=15))

    fig.update_layout(
        plot_bgcolor='rgb(234, 228, 228)',
        paper_bgcolor='rgb(211, 211, 211)',
        #title=" Coulombic Efficiency with {}% capacity retention".format(cap2),
        title=" Coulombic Efficiency vs Cycle Number",
        title_x=0.5,
        xaxis_title="Cycle Number",
        yaxis_title="Coulmbic Efficiency",
        font=dict(
            family="arial, monospace",
            size=16,
            color="black"
        ),
        showlegend=False
    )
    return dcc.Markdown("The cell is requried **{}** % CE to achieve {} cycle life.".format(round(res_CE,4), int(cycle)), dangerously_allow_html=True), fig

@callback(Output('option1_outcome', 'children'),Output('cyclelife','figure'),Input('input_zz','value'),Input('input_g','value'))
def update_figure(zz, g):
    if zz and g is not None:
        return option1(zz,g)


@callback([Output('option2_outcome', 'children'),Output('CElife','figure')],[Input('input_cap2','value'),Input('input_cycle','value')])
def update_figure(cap2, cyclno):
    if cap2 and cyclno is not None:
        return option2(cap2,cyclno)
    else:
        return dcc.Markdown("It is not working, sorry ")
    

def li_thickness(arealcap=3.00):
    fig=go.Figure()
    cap_x = np.arange(float(arealcap)*0.2, float(arealcap)*1.5,0.01)
    thick_Li =[10000*x*6.941/(26801.4814*0.534) for x in cap_x]
    T_Li = 10000*float(arealcap)*6.941/(26801.4814*0.534)
    S_Li = 10000*float(cap_x[0])*6.941/(26801.4814*0.534)
    fig.add_trace(go.Scatter(x=cap_x, y=thick_Li, mode='lines'))
    fig.add_trace(go.Scatter(x=[cap_x[0],float(arealcap)], y=[T_Li,T_Li], mode='lines',line=dict(dash='dash',color="gray")))
    fig.add_trace(go.Scatter(x=[float(arealcap), float(arealcap)], y=[S_Li, T_Li], mode='lines',line=dict(dash='dash',color="gray")))
    fig.add_trace(go.Scatter(x=[float(arealcap)], y=[T_Li], mode='markers', marker_symbol='circle', marker_size=15))

    fig.update_layout(
        plot_bgcolor='rgb(234, 228, 228)',
        paper_bgcolor='rgb(211, 211, 211)',
        title="Li thickness response to Li Areal Capacity",
        title_x=0.5,
        xaxis_title="Li Areal Capacity [mAh/cm\u00b2]",
        yaxis_title="Li Thickness [\u03bcm]",
        font=dict(
            family="arial, monospace",
            size=16,
            color="black"
        ),
        showlegend=False
    )    
    return dcc.Markdown("With Areal capacity of Li, {} \u03bcm Li is stripped or deposited".format(round(T_Li,2)), dangerously_allow_html=True), fig

@callback([Output('thickness_outcome', 'children'),Output('thicknessplot','figure')],Input('liarealcap','value'))
def update_arealcap(liareal_cap):
    if liareal_cap is not None:
        areal_cap = float(liareal_cap)
        return li_thickness(areal_cap)
    else:
        return li_thickness()
    

@callback(
    [Output('summary_table','children'), Output('pie1','figure'),Output('ed_plot','figure')],
    [Input('c_ed','value'), Input('c_et','value'), Input('c_amlr','value'), Input('c_pcam','value'),Input('c_ea','value')],
    [Input('a_ed','value'), Input('a_et','value'), Input('a_amlr','value'), Input('a_pcam','value'),Input('a_ea','value')],
    [Input('Al_t','value'), Input('Cu_t','value'), Input('area_tap','value'),Input('S_w','value')],
    [Input('stacktype','value'),Input('other_packageweight','value'),Input('nom_v','value'),Input('stacked_layer','value')],
    Input('target_ed','value'),
    )

def cell_energy_densit(c_ed, c_et, c_amlr, c_pcam, c_ea, a_ed, a_et, a_amlr, a_pcam, a_ea, Al_t, Cu_t, area_tap, S_w, stacktype,other_packageweight,nom_v, stacked_layer,target_ed):

    # Internal parameters:
    Al_density = 2.7 # [g/cm3]
    Cu_density = 8.93 # [g/cm3]
    # Calculate capacity per sheet
        
        # areal capacity 
    areal_cap_cath = float(c_ed)*float(c_et)*0.0001*float(c_amlr)*float(c_pcam)   # [g/cm3][um][cm/10000um][][mAh/g] = [mAh/cm2];
    areal_cap_anode =float(a_ed)*float(a_et)*0.0001*float(a_amlr)*float(a_pcam) # [mAh/cm2]

        # capacity and weight per sheet
    cap_cath = areal_cap_cath * float(c_ea) # [mAh/cm2]*[cm2] = [mAh]
    cap_anode = areal_cap_anode * float(a_ea) # [mAh/cm2]*[cm2] = [mAh]

    w_cath = float(c_ed)*float(c_et)*0.0001*float(c_ea) # [g/cm3][um][cm/10000um][cm2]=[g]
    w_anode =float(a_ed)*float(a_et)*0.0001*float(a_ea) # [g/cm3][um][cm/10000um][cm2]=[g]

    # total capacity : take min capacity between anode and cathode, x stacking layer
    rep_cap = min([cap_cath, cap_anode]);
    

    Al_area = float(c_ea) + (float(area_tap) * 0.01) # [cm2]
    Cu_area = float(a_ea) + (float(area_tap) * 0.01) # [cm2]

    # Calculate weight for energy density
    if stacktype == 't1':
        N_cu=int(stacked_layer);
        N_al=int(stacked_layer);
        N_ed=int(stacked_layer)*2;
        cell_cap = rep_cap * int(stacked_layer) * 2 * 0.001 # [mAh]*Numeroflayer*2(why??)*0.001[Ah/mAh] = [Ah]
        
        # weight for electrode:
        cell_w_cath = w_cath * int(stacked_layer) * 2 #[g]
        cell_w_anode = w_anode * int(stacked_layer) * 2

        # weight for other componets: otherpackageweight(tabsand packaing), Al_foil, Cu_foil, Separator, anode, cathode, electrolyte
        w_Al = int(stacked_layer) * Al_density * Al_area * float(Al_t) * 0.0001 # [g/cm3][cm2][um][cm/10000um] = [g]
        w_Cu = int(stacked_layer) * Cu_density * Cu_area * float(Cu_t) * 0.0001 # [g/cm3][cm2][um][cm/10000um] = [g]

 
    elif stacktype =='t2':
        cell_cap = rep_cap * int(stacked_layer) * 0.001 # [mAh]*Numeroflayer*2(why??)*0.001[Ah/mAh] = [Ah]
        if int(stacked_layer)==1:
            N_al=1;
            N_cu=1;
        else:
            N_al=math.ceil(int(stacked_layer)/2);
            N_cu=math.floor(int(stacked_layer)/2)+1;
        
        N_ed=int(stacked_layer)
        cell_w_cath = w_cath * int(stacked_layer)  #[g]
        cell_w_anode = w_anode * int(stacked_layer)
        w_Al = N_al * Al_density * Al_area * float(Al_t) * 0.0001 # [g/cm3][cm2][um][cm/10000um] = [g]
        w_Cu = N_cu * Cu_density * Cu_area * float(Cu_t) * 0.0001 # [g/cm3][cm2][um][cm/10000um] = [g] 
    
    elif stacktype == "t3":
        cell_cap = rep_cap * int(stacked_layer) * 0.001 # [mAh]*Numeroflayer*2(why??)*0.001[Ah/mAh] = [Ah]
        if int(stacked_layer)==1:
            N_al=1;
            N_cu=1;
        else:
            N_cu=math.ceil(int(stacked_layer)/2);
            N_al=math.floor(int(stacked_layer)/2)+1;
        N_ed=int(stacked_layer);
        cell_w_cath = w_cath * int(stacked_layer)  #[g]
        cell_w_anode = w_anode * int(stacked_layer)
        w_Al = N_al * Al_density * Al_area * float(Al_t) * 0.0001 # [g/cm3][cm2][um][cm/10000um] = [g]
        w_Cu = N_cu * Cu_density * Cu_area * float(Cu_t) * 0.0001 # [g/cm3][cm2][um][cm/10000um] = [g] 

    global cell_energy
       # Calculate amount of electrode to reach target eneryg density
    cell_energy = cell_cap * float(nom_v) # [Ah][V] = [Wh]
    total_target_weight = (cell_energy / float(target_ed))*1000 # [kg]*1000[g/kg]=[g]
    weight_beside_electrolyte = float(other_packageweight)+ w_Al+ w_Cu + float(S_w)+ cell_w_cath + cell_w_anode;
    w_electrolyte = total_target_weight - weight_beside_electrolyte #[g]
    
    
    fig1=go.Figure()
    
    if w_electrolyte < 0:
        w_electrolyte = 1.3*cell_cap # [g/Ah][Ah]=[g]
        EC_ratio = 1.3;
        EC = EC_ratio;
        
    else:

        EC_ratio = w_electrolyte/cell_cap
        EC = round(EC_ratio,2)



    x2 = np.arange(w_electrolyte*0.2, w_electrolyte*1.4, 0.1);
    y2 = [(cell_energy/((weight_beside_electrolyte+xx)*0.001)) for xx in x2];
    idx = np.argmin(np.abs(np.abs(x2-w_electrolyte)));
    fig1.add_trace(go.Scatter(x=x2, y=y2, mode='lines'))
    fig1.add_trace(go.Scatter(x=[x2[idx]], y=[y2[idx]], mode='markers', marker_symbol='circle',marker_size=15))

    total_weight = [cell_w_cath,cell_w_anode,w_Al,w_Cu,S_w,w_electrolyte,other_packageweight];
    w_idx=['Cathode','Anode','Al-foil','Cu-foil','Separator','Electrolyte','Others'];   

    weight_data = pd.DataFrame({'component':w_idx, 'weight [g]':total_weight})

     # make outputs
    pfig=px.pie(weight_data, values=weight_data['weight [g]'],hole=.3, names=weight_data['component'])

    
    pfig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(
            family="arial, monospace",
            size=14,
            color="black"
        ),
        margin=dict(t=0,b=0,l=0,r=0)

    )


    fig1.update_layout(
        plot_bgcolor='rgb(234, 228, 228)',
        paper_bgcolor='rgb(211, 211, 211)',
        xaxis_title="Amount of Electrolyte [g]",
        yaxis_title="Energy Density [Wh/kg]",
        font=dict(
            family="arial, monospace",
            size=16,
            color="black"
        ),
        showlegend=False
    )

    ed_plot=fig1;
        # N/P ratio;
    NP_ratio = areal_cap_anode/areal_cap_cath

        # For summary table
    s_index = ['Cell Capacity[Ah]','Energy [Wh]', 'NP ratio','EC ratio [g/Ah]','No. Al-foil','No. Cu-foil', 'No. single side electrode']
    summary_data=[round(cell_cap,2),round(cell_energy,2),round(NP_ratio,2), EC, N_al, N_cu, N_ed]
    st = pd.DataFrame({"Parameters":s_index,"Results":summary_data})



    Summary_table=dash_table.DataTable(
                                style_cell={'font-family': 'Arial', 'font-size': '16px', 'text-align':'auto', 'margin-top':'auto', 'minWidth': '140px', 'width': '140px', 'maxWidth': '160px', 'padding':2}, 
                                markdown_options={"html": True},
                                #virtualization=True,
                                style_table={'overflowX': 'auto'},
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
                                    'backgroundColor': 'black',
                                    'color': 'white',
                                    'fontWeight': 'bold',
                                    'font-size': '18px',
                                    'text-align':'center'
                                },
                                data=st.to_dict('records'),
                                columns=[{'id': c, 'name': c,"presentation": "markdown"} for c in st.columns],
                    ),
    
    return Summary_table, pfig, ed_plot


@callback([Output('joutcome9', 'children'), Output('joutcome10', 'children'), Output('joutcome11', 'children'), 
               Output('joutcome12','children')],
                [Input('jinput-c1', 'value'),
                Input('jinput-c2', 'value'),
                Input('jinput-c3', 'value'),
                Input('jinput-c4', 'value'),
                Input('jinput-c5', 'value'),
                Input('jinput-c6', 'value'),
                Input('jinput-c7', 'value'),
                Input('jinput-c8', 'value'),
                Input('jinput-c9', 'value'),
                Input('jinput-c10', 'value'),
                Input('jinput-c11', 'value'),
                Input('jinput-c12', 'value'),
                Input('jinput-c13', 'value'),  
                ], 
            )        
def update_content(input_c1, input_c2, input_c3, input_c4, input_c5, input_c6, input_c7, input_c8, input_c9, input_c10, input_c11, input_c12, input_c13):
    if all([input_c1 and input_c2 and input_c3 and input_c4 and input_c5 and input_c6 and input_c7 and input_c8 and input_c9 and input_c10 and input_c11 and input_c12 and input_c13]):
        d_asc = float(input_c1)*2+float(input_c2)+float(input_c8)*2+float(input_c9)+float(input_c10)*2
        a=d_asc/(2*np.pi)*(0.000001)
        d_o=float(input_c11)-2*float(input_c12) # outer diammeter, cell can thickness [mm]
        r_o=d_o*(0.001)/2
        d_i=float(input_c13)
        r_i=d_i*(0.001)/2
        sigma_1=r_o/a
        sigma_0=r_i/a
        L1=(sigma_1/2)*(pow(((sigma_1)*(sigma_1)+1),0.5))+0.5*np.log(sigma_1+pow(((sigma_1)*(sigma_1)+1),0.5))
        L0=(sigma_0/2)*(pow(((sigma_0)*(sigma_0)+1),0.5))+0.5*np.log(sigma_0+pow(((sigma_1)*(sigma_1)+1),0.5))
        L_t=(L1-L0)*d_asc/(2*np.pi)*0.000001
        outcome9 = L_t #Length of the cathode
        cathode_length=dcc.Markdown("The length of the cathode inside the cell is **{}** m.".format(round(outcome9,2)), dangerously_allow_html=True),
        outcome10 = (sigma_1-sigma_0)/(2*np.pi) #Number of turns of the cathode in the cell
        winding_number=dcc.Markdown("The number of winding(turn) inside the cell is **{}**.".format(round(outcome10,1)), dangerously_allow_html=True),
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

# @callback(
#     #[Output('jsummary_table','children'), Output('jellyroll_plot','figure')],
#     [Output('cathod_length', 'children'), Output('No_winding', 'children'), Output('areal_cap', 'children'), Output('cell_cap','children')],
#     [Input('jc_et','value'), Input('ja_et','value'), Input('jc_amlr','value'), Input('ja_amlr','value'),Input('jc_w','value')],
#     [Input('jc_ed','value'), Input('ja_ed','value'), Input('jc_pcam','value'), Input('ja_pcam','value')],
#     [Input('input-c11','value'), Input('input-c12','value'), Input('input-c13','value'),Input('jAl_t','value'),Input('jCu_t','value'),Input('jse_w','value')],
#     )

# def jelly_roll(jc_et, ja_et, jc_amlr, ja_amlr, jc_w, jc_ed, ja_ed, jc_pcam, ja_pcam, input_c11, input_c12, input_c13, jAl_t, jCu_t, jse_w):
    
#     # Areal capacity 
#     areal_cap_cath = float(jc_ed)*float(jc_et)*0.0001*float(jc_amlr)*float(jc_pcam)   # [g/cm3][um][cm/10000um][][mAh/g] = [mAh/cm2];
#     areal_cap_anode= float(ja_ed)*float(ja_et)*0.0001*float(ja_amlr)*float(ja_pcam) # [mAh/cm2]

#     d_asc = (float(jc_et)+float(ja_et)+float(jse_w))*2+float(jAl_t)+float(jCu_t) # [um] total thickness
#     a=d_asc/(2*np.pi)*(0.000001) # [um]--> [mm]
#     d_o=float(input_c11)-2*float(input_c12)
#     r_o=d_o*(0.001)/2
#     d_i=float(input_c13)
#     r_i=d_i*(0.001)/2
#     sigma_1=r_o/a
#     sigma_0=r_i/a
#     L1=(sigma_1/2)*(pow(((sigma_1)*(sigma_1)+1),0.5))+0.5*np.log(sigma_1+pow(((sigma_1)*(sigma_1)+1),0.5))
#     L0=(sigma_0/2)*(pow(((sigma_0)*(sigma_0)+1),0.5))+0.5*np.log(sigma_0+pow(((sigma_1)*(sigma_1)+1),0.5))
#     L_t=(L1-L0)*d_asc/(2*np.pi)*0.000001
#     outcome9 = L_t #Length of the cathode
#     cathode_length=dcc.Markdown("The length of the cathode inside the cell is **{}** m.".format(round(outcome9,2)), dangerously_allow_html=True),
#     outcome10 = (sigma_1-sigma_0)/(2*np.pi) #Number of turns of the cathode in the cell
#     winding_number=dcc.Markdown("The number of winding(turn) inside the cell is **{}**.".format(round(outcome10,1)), dangerously_allow_html=True),
#     outcome11 =areal_cap_cath #Areal cathode capacity
#     areal_capacity=dcc.Markdown("The areal cathode capacity is **{}** mAh/cm<sup>2</sup>.".format(round(outcome11,2)), dangerously_allow_html=True),
#     outcome12 = outcome11*outcome9*100*float(jc_w)/1000 #Areal cathode capacity
#     cell_capacity=dcc.Markdown("The predicted cell capacity is **{}** Ah.".format(round(outcome12,2)), dangerously_allow_html=True),

#     return  (cathode_length,
#             winding_number,
#             areal_capacity,
#             cell_capacity,)