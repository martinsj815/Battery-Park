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
    __name__, name="basics", top_nav=True, path="/basics-pm"
    )

#dash.register_page(__name__, name="basics", top_nav=False)


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


layout = html.Div([
             dcc.Tabs(id="P or M", value='tab-1', children=[
                dcc.Tab(label='Parameters', value='tab-1', style=tabs_styles, selected_style=tab_selected_style,
                        children=[
                    dbc.Row([
                        dcc.Markdown('* Current Density', style={'marginTop':'40px','font-size':'25px','textAlign':'left','font-weight':'bold'}),
                        dbc.Col([
                         html.H5(('- Current density represents the quantity of current flowing through a unit cross-sectional area [mA/cm\u00b2]. Often in the literature, it is expressed in terms of current per unit active material loading [mA/g]. However, it is enssential to also provide the areal active material loading [mg/cm\u00b2] concurrently. Without this information, misleading performrance evaluations can occur, especially when the active loading of cells is low, which may not accuratley represent the true performance.'), style={'textAlign':'justify','margin-left':'20px'}),
                         html.H5(('- Additionally, current density depends on the C-rate. When specifying a current density, it should be indicated under which C-rate it applies. Without this specification, a rate 1C is typically assumed. Furthermore, when rate performance is claimed, the highest rate should correspond to 80% capacity retention. For example, if the capacity can maintain 80% at 3C, it can be claim that this cell can discharge/charge at 3C.'), style={'textAlign':'justify','margin-left':'20px'}),
                         html.H5(('- With this parameter, areal capacity can also be obtained by multiplying it with time.'), style={'textAlign':'justify','margin-left':'20px'}),
                        ], width={"size":8},
                        xs=12, sm=12, md=12, lg=8, xl=8
                        ),
                        dbc.Col([
                        html.Div( html.Img(src='https://www.dropbox.com/scl/fi/y8vsd5rcg0tu026bzxe60/CurrentDensity.png?rlkey=sfghzpokmu30bcr6603lhz8e6&raw=1', style={"width":"150%"}), 
                                ),
                        ], width={"size": 3},
                        xs=8, sm=8, md=6, lg=6, xl=3
                        ),
                    ]),
                    html.Br(),
                    dmc.Divider(size="md", color="grey"),
                    html.Br(),

                    dbc.Row([
                        dcc.Markdown('* Internal Resistance from impulse current', style={'font-size':'25px', 'textAlign':'left','font-weight':'bold'}),
                        dbc.Col([
                         html.H5(('- Resistance is an important parameter to evaluate battery quality, with its variation during cycling significantly impacting performance.'), 
                                 style={'textAlign':'justify', 'margin-left':'20px'}),
                         html.H5(("- Resistance can be measured according to Ohm's law by observing the voltage drop (\u0394V) when applying a pulse current (I, [A]) to the battery."), 
                                 style={'textAlign':'justify', 'margin-left':'20px'}),
 
                        dcc.Markdown(dangerously_allow_html=True, mathjax=True, children=('$$R_{total}=\\frac{\u0394V}{I}=R_{0}+R_{CT}+R_{p}$$'), style={'text-align':'center','font-size':'120%'}),
                         html.H5(("- Cause of resistance can be categorized into three parts based on their timescale (resistance is typically measured over 10 seconds):"), 
                                 style={'textAlign':'justify', 'margin-left':'20px'}),
                         html.H5((["1. The instantaneous voltage drop (R",html.Sub("0"), ") arises from the purely ohmic resistance and the bulk ionic resistance of the battery. Timescale of the dominant contribution is < 10",html.Sup("-3")," seconds."]), 
                                 style={'textAlign':'justify', 'margin-left':'40px'}),
                         html.H5((["2. Charge transfer resistance (R",html.Sub("CT"), ") is caused by the battery's double-layer capacitance at the electrde/electrolyte interface. Timescale of dominant contribution is < 2~3 seconds."]), 
                                 style={'textAlign':'justify', 'margin-left':'40px'}),
                         html.H5((["3. The linear voltage drop due to polarization (R",html.Sub("p"), ") results from ion diffusion in the solid phase and is generally considered the rate-determining step in Li-ion batteries."]), 
                                 style={'textAlign':'justify', 'margin-left':'40px'}),
                        html.H5((" Resistance value is affected by temperature, state of charge, state of health, and applied current."), 
                                 style={'textAlign':'justify', 'margin-left':'20px'}),
                         ], width={"size": 8},
                         xs=12, sm=12, md=12, lg=8, xl=8
                         ),
                         dbc.Col([
                         html.Div( html.Img(src='https://www.dropbox.com/scl/fi/l9zmll5xggmb8wkerdug8/Resistance.png?rlkey=uy8dus0jmvbpoghs6r26tz4q7&raw=1', style={"width":"150%"}), 
                                  ),
                         ], width={"size": 3},
                         xs=12, sm=8, md=6, lg=6, xl=3
                         ),
                    ],style={'marginTop': '20px'},
                    ),]
                ),
                dcc.Tab(label='Metrics',value='tab-2',style=tabs_styles,selected_style=tab_selected_style,
                        children=[
                            dbc.Row([
                          dcc.Markdown('* Voltage & Capacity', style={'font-size':'25px', 'textAlign':'left','font-weight':'bold'}),
                          dbc.Col([
                           html.H5(('- Cell voltage is dependent on the chemistry of chemical compounds assembled. Nominal voltage is more like an average (or typical) voltage for the system different from the precise operating cell voltage (under load). For lead-acid, the nominal voltage is 2V. For nickel-based, it is 1.2V. For lithium-ion, it is typically more than 3V.'), 
                                   style={'textAlign':'justify', 'margin-left':'20px'}),
                           html.H5(('- Cell capacity states the quantity of charge in the cell and is dependent on the amount of active materials used. It is measured in Amphere-hours.'), 
                                   style={'textAlign':'justify', 'margin-left':'20px'}),
                           html.H5(('- Specific capacity is the capacity measured per unit mass. This can be calculated theoretically using its molecular weight and Faraday constant:'), 
                                   style={'textAlign':'justify', 'margin-left':'20px'}),   
                          dcc.Markdown(dangerously_allow_html=True, mathjax=True, children=('$$Q_{gravimetric}=\\frac{n*F}{M_{W}*3600}$$'), style={'text-align':'center','font-size':'150%'}),
                          ], width={"size": 8},
                          xs=12, sm=12, md=12, lg=8, xl=8
                          ),
                          dbc.Col([
                          html.Div( html.Img(src='https://dl.dropboxusercontent.com/scl/fi/04eebykwg2dgxfr4o2bns/voltage-curve.png?rlkey=1iwh8vmh9cuax2r41gspsvopf&raw=1', style={"width":"100%"}), 
                                   ),
                          ], width={"size": 3},
                          xs=12, sm=12, md=6, lg=6, xl=3
                          ),
                      ],style={'marginTop': '40px'},),
                      html.Br(),
                      dmc.Divider(size="md", color="grey"),
                      html.Br(),
                      dbc.Row([
                          dcc.Markdown('* Energy & Power', style={'marginTop':'20px','font-size':'25px', 'textAlign':'left','font-weight':'bold'}),
                          dbc.Col([
                           html.H5('- Energy stored in the cell is defined as the Capacity multiplied by Voltage and its unit is Wh and can be described as:', style={'textAlign':'justify', 'margin-left':'20px'}),
                           dcc.Markdown(dangerously_allow_html=True, mathjax=True, children=("$$E=\\int_0^{t_{d}} IV(t)\\, dt$$"), style={'text-align':'center','font-size':'120%'}),
                           html.H5('- Power is the rate at which how fast the energy can be delivered. Its unit is in Watts. Instantaneous power is simply Current times Voltage at the certain time during battery operation. Average power is defined as:', style={'textAlign':'justify', 'margin-left':'20px'}),
                           dcc.Markdown(dangerously_allow_html=True, mathjax=True, children=("$$P_{avg}=\\frac{1}{t_{d}}\\cdot\\int_0^{t_{d}} IV(t)\\, dt$$"), style={'text-align':'center','font-size':'120%'}),
                           ], width={"size": 8}, 
                           xs=12, sm=12, md=12, lg=8, xl=8
                           ),
                          dbc.Col([
                          html.Div( html.Img(src='https://dl.dropboxusercontent.com/scl/fi/u3hpg4778cobd1gkwt7ip/voltage-curve_energy.png?rlkey=yk40i5t5nkfqel0k6v7lrii2x&raw=1', style={"width":"100%"}), 
                                   ),
                          ], 
                          width={"size": 3},
                          xs=12, sm=12, md=6, lg=6, xl=3
                          ),
                      ],),
                      html.Br(),
                      dbc.Row([
                          dbc.Col([
                           html.H5('- Energy density and power density is energy and power normalized by the cell mass. Hence, the unit is Wh/kg and W/kg, respectively. Energy density can be approximated by multiplying specific capacity with nominal voltage.', style={'textAlign':'justify', 'margin-left':'20px'}),
                           html.H5('- Typically, it is difficult for batteries to have both metrics met at the high end. High energy density demands the cell to be discharged at a slow rate for it to reach its maximum capacity and avoid polarization losses. However, since a lower current rate means longer discharge time, power density will be low. For high power density, energy density is likely sacrificed. This trend is illustrated in a Ragone Plot.', style={'textAlign':'justify', 'margin-left':'20px'}),
                           ], width={"size": 8},
                           xs=12, sm=10, md=10, lg=8, xl=8
                           ), 
                          dbc.Col([
                          html.Div( html.Img(src='https://dl.dropboxusercontent.com/scl/fi/95o1wg7pysd41mx7qd1jy/Ragone-plot.bmp?rlkey=3d7offwomdyp0qn7b0tw6fwk6&raw=1', style={"width":"140%"}), 
                                   ),
                          html.Div(('Courtesy: Venkat Srinivasan'), 
                                   style={'textAlign':'justify', 'font-size':'15px', 'font-style':'italic', 'margin-left':'0px'}),  
                          ], width={"size": 3},
                          xs=12, sm=12, md=6, lg=6, xl=3),
                      ],),
                    ])
                ],),
                html.Div(id='tabs-content'),
])
