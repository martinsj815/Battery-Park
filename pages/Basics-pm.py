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
                    dbc.Col([
                     dbc.Row([
                        dcc.Markdown('* Current Density', style={'marginTop':'40px','font-size':'25px','textAlign':'left','font-weight':'bold'}),
                        dbc.Col([
                         html.Div(('- Current density represents the quantity of current flowing through a unit cross-sectional area [mA/cm\u00b2]. Often in the literature, it is expressed in terms of current per unit active material loading [mA/g]. However, it is enssential to also provide the areal active material loading [mg/cm\u00b2] concurrently. Without this information, misleading performrance evaluations can occur, especially when the active loading of cells is low, which may not accuratley represent the true performance.'), style={'textAlign':'justify','margin-left':'20px', 'font-size':'18px'}),
                         html.Br(),
                         html.Div(('- Additionally, current density depends on the C-rate. When specifying a current density, it should be indicated under which C-rate it applies. Without this specification, a rate 1C is typically assumed. Furthermore, when rate performance is claimed, the highest rate should correspond to 80% capacity retention. For example, if the capacity can maintain 80% at 3C, it can be claim that this cell can discharge/charge at 3C.'), style={'textAlign':'justify','margin-left':'20px', 'font-size':'18px'}),
                         html.Br(),
                         html.Div(('- With this parameter, areal capacity can also be obtained by multiplying it with time.'), style={'textAlign':'justify','margin-left':'20px', 'font-size':'18px'}),
                        ], width={"size":8},
                        xs=12, sm=12, md=12, lg=8, xl=8
                        ),
                        dbc.Col([
                        html.Div( html.Img(src='https://dl.dropboxusercontent.com/scl/fi/y8vsd5rcg0tu026bzxe60/CurrentDensity.png?rlkey=sfghzpokmu30bcr6603lhz8e6&raw=1', style={"width":"150%"}), 
                                ),
                        ], width={"size": 3},
                        xs=8, sm=8, md=6, lg=6, xl=3
                        ),
                    ]),
                    html.Br(),
                    dmc.Divider(size="md", color="grey"),
                    html.Br(),
                    html.Br(),
                    dbc.Row([
                        dcc.Markdown('* Open Circuit Voltage (OCV) and State of Charge (SoC)', style={'marginTop':'20px', 'font-size':'25px','textAlign':'left','font-weight':'bold'}),
                        dbc.Col([
                            html.Div(('- OCV and SOC are important parameters in battery characterization.'), style={'textAlign':'justify','margin-left':'20px', 'font-size':'18px'}),
                            html.Div(('- OCV represents the potential difference between the cathode and anode when no current or voltage is applied. Theoretically, assuming that all active electrode particles are fully connected by conductive additives and maintain electrical neutrality, the OCV can be calculated from the difference in Gibbs free energy between cathode and anode materials.'), style={'textAlign':'justify','margin-left':'20px', 'font-size':'18px'}),
                            dcc.Markdown(dangerously_allow_html=True, mathjax=True, children=('$$V_{OC}=-\\frac{\u0394G}{nF}$$'), style={'text-align':'center', 'margin-top':'20px', 'font-size':'120%'}),
                            html.Div("where n is the number of electrons involved, and F is the Faraday's constant.", style={'textAlign':'center', 'font-size':'14px'}),
                            html.Div(('- OCV is used as an important metric to analyze electrode health and identify potential issues such as internal resistance, and capacity fade by measuring deviations from the OCV.'), style={'textAlign':'justify','margin-left':'20px','margin-top':'10px', 'font-size':'18px'}),
                            html.Div(('- SOC represents the remaining capacity available in the battery at any given point in time. It is expressed as a percentage, where 100% indicates the battery is fully charged, and 0% indicates that it is complete discharge.'), style={'textAlign':'justify','margin-left':'20px', 'font-size':'18px'}),
                            html.Div(('- Since the (electro-)chemical potential of the cathode and anode varies with state of charge, OCV depends on SOC.'), style={'textAlign':'justify','margin-left':'20px', 'font-size':'18px'}),
                            html.Div(('- OCV and SOC are used for battery health assessment, quality control, and aging monitoring.'), style={'textAlign':'justify','margin-left':'20px', 'font-size':'18px'}),
                            ], width={"size":8}, xs=12, sm=12, md=12, lg=8, xl=8
                            ),
                        dbc.Col([
                        html.Div( html.Img(src='https://dl.dropboxusercontent.com/scl/fi/mld2fwcmjqdx53n1gfqad/OCV_SOC.png?rlkey=lu6096jedwoljqufh8ndw1vhi&st=ggldxlfy&raw=1', style={"width":"150%"}), 
                                ),
                        ], width={"size": 3},
                        xs=8, sm=8, md=6, lg=6, xl=3
                        ),
                            
                        ],
                            
                        ),
                    
                    html.Br(),
                    dmc.Divider(size="md", color="grey"),
                    html.Br(),
                    html.Br(),
                    dbc.Row([
                        dcc.Markdown('* Voltage and Polarization ', style={'font-size':'25px', 'textAlign':'left','font-weight':'bold'}),
                        dbc.Col([
                         html.Div(("- Voltage represents the difference in potential between the cathode and anode and the driving force of current flowing. The unit is volt [V]."),style={'textAlign':'justify', 'margin-left':'20px', 'font-size':'18px'}), 
                         html.Div(("- When a circuit is connected or current begins to flow, the voltage drops, which is caused by electrode polarization due to the kinetic limits of the reaction and other electrochemical kinetical reactions to allow current to flow during the charge/discharge reaction. The degree of this polarization can be estimated from the voltage deviation (overpotential, \u03B7) from the open circuit voltage. The overpotential is given by"), 
                                 style={'textAlign':'justify', 'margin-left':'20px', 'margin-bottom':'20px', 'font-size':'18px'}),
                        dcc.Markdown(dangerously_allow_html=True, mathjax=True, children=('$$\u03B7 = V_{T}-V_{OC}$$'), style={'text-align':'center', 'margin-bottom':'20px', 'font-size':'120%'}),
                        html.Div(["where V",html.Sub("OC")," is the voltage of the cell at open circuit and V",html.Sub("T")," is the terminal cell voltage with current flowing."], style={'textAlign':'center','margin-top':'10px', 'font-size':'14px'}),
                        html.Div(("During the reaction, the cell involves a series of physical, chemical, and electrochemical steps, including charge-transfer and charge transport reactions."),style={'textAlign':'justify', 'margin-left':'40px', 'margin-bottom':'10px', 'font-size':'18px'}),
                        html.Div(["- The main sources of polarization can be categroized into three parts: 1) ohmic polarization (R",html.Sub("O"),"), 2) activation polarization (R",html.Sub("CT"),"), and 3) concentration polarization (R",html.Sub("P"),")."],style={'textAlign':'left', 'margin-left':'20px', 'margin-bottom':'10px', 'font-size':'18px'}), 
                        dcc.Markdown(dangerously_allow_html=True, mathjax=True, children=('$$R_{total}=R_{o}+R_{ct}+R_{p}$$'), style={'text-align':'center', 'margin-bottom':'20px', 'font-size':'120%'}),
                         ], width={"size": 8},
                         xs=12, sm=12, md=12, lg=8, xl=8
                         ),
                         dbc.Col([
                         html.Div( html.Img(src='https://dl.dropboxusercontent.com/scl/fi/sm2fix5hl4hqmg7pwgib8/Polarization.png?rlkey=t42tp9mq6w0p2669yt0js90lg&st=7tw1qwd1&raw=1', style={"width":"150%"}), 
                                  ),
                         ], width={"size": 3},
                         xs=12, sm=8, md=6, lg=6, xl=3
                         ),
                        
                         html.Div((["1) Ohmic Polarization (R",html.Sub("o"), ") arises from the resistance of connectivity's of individual cell components and contact between the cell components. Ohmic polarization appears instantaneously (\u2264 10",html.Sup("-6"),"s) when current flows."]), 
                                 style={'textAlign':'justify', 'margin-left':'40px', 'margin-bottom':'10px', 'font-size':'18px'}),
                         html.Div((["2) Activation polarization (R",html.Sub("ct"), ") is related to the kinetics hinderances of the charge-transfer reactions at the electrode/electrolyte interfaces of anode and cathode. The buildup of the activation polarization are fast and can be identified by the voltage change on current interruption in a time frame of 10",html.Sup("-2"),"s - 10",html.Sup("-4"),"s."]), 
                                 style={'textAlign':'justify', 'margin-left':'40px', 'margin-bottom':'10px', 'font-size':'18px'}),
                        html.Div((["3) Concentration polarization (R",html.Sub("p"), ") arises from limited diffusion of active species to and from the electrode surface to replace the reacted material to sustain the reaction. Diffusion limitations are relatively slow, and the buildup takes \u2265 10",html.Sup("-2"),"s to appear."]), 
                                 style={'textAlign':'justify', 'margin-left':'40px', 'margin-bottom':'10px', 'font-size':'18px'}),    
                        html.Div(([" Although R",html.Sub("o"), ", R",html.Sub("ct")," and R",html.Sub("p"),"are not completely distint, they are expected to be the dominat contrituion to total resistance at their respective timescales." ]), 
                                 style={'textAlign':'justify', 'margin-left':'40px', 'margin-bottom':'10px', 'font-size':'18px'}),  
                        html.Div((" These resistances are affected by temperature, state of charge, state of health, and applied current."), 
                                 style={'textAlign':'justify', 'margin-left':'20px', 'font-size':'18px'}),
                    ],style={'marginTop': '20px',"margin-bottom":'20px'},
                    ),],

                ),
                 html.Br(),
                 dmc.Divider(size="md", color="grey"),
                 html.Br(),
                 dbc.Col([
                        dcc.Markdown(('* References'), 
                        style={'textAlign':'justify', 'margin-left':'20px', 'font-size':'30px', 'font-weight':'bold'}),
                        dcc.Markdown(('Martine Winter, et al, "What Are Batteries, Fuel Cells, and Supercapacitors?", _**Chemical Reviews**_, 104, 4245-4269 (2004)'), 
                                style={'textAlign':'justify', 'font-size':'15px', 'margin-left':'0px'}),
                        ]),
                ],
                style={'textAlign':'justify', 'margin-left':'30px', 'margin-right':'30px'},
                ),
                ],),
                dcc.Tab(label='Metrics',value='tab-2',style=tabs_styles,selected_style=tab_selected_style,
                        children=[
                dbc.Row([
                    dbc.Col([
                        dbc.Row([
                          dcc.Markdown('* Voltage & Capacity', style={'font-size':'25px', 'textAlign':'left','font-weight':'bold'}),
                          dbc.Col([
                           html.Div(('- Cell voltage is dependent on the chemistry of chemical compounds assembled. Nominal voltage is more like an average (or typical) voltage for the system different from the precise operating cell voltage (under load). For lead-acid, the nominal voltage is 2V. For nickel-based, it is 1.2V. For lithium-ion, it is typically more than 3V.'), 
                                   style={'textAlign':'justify', 'margin-left':'20px', 'font-size':'18px'}),
                           html.Br(),
                           html.Div(('- Cell capacity states the quantity of charge in the cell and is dependent on the amount of active materials used. It is measured in Amphere-hours.'), 
                                   style={'textAlign':'justify', 'margin-left':'20px', 'font-size':'18px'}),
                           html.Br(),
                           html.Div(('- Specific capacity is the capacity measured per unit mass. This can be calculated theoretically using its molecular weight and Faraday constant:'), 
                                   style={'textAlign':'justify', 'margin-left':'20px', 'font-size':'18px'}),   
                           html.Br(),
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
                          dcc.Markdown('* Energy & Power', style={'marginTop':'20px', 'font-size':'25px', 'textAlign':'left','font-weight':'bold'}),
                          dbc.Col([
                           html.Div('- Energy stored in the cell is defined as the Capacity multiplied by Voltage and its unit is Wh and can be described as:', style={'textAlign':'justify','font-size':'18px'}),
                           dcc.Markdown(dangerously_allow_html=True, mathjax=True, children=("$$E=\\int_0^{t_{d}} IV(t)\\, dt$$"), style={'text-align':'center','font-size':'120%'}),
                           html.Div('- Power is the rate at which how fast the energy can be delivered. Its unit is in Watts. Instantaneous power is simply Current times Voltage at the certain time during battery operation. Average power is defined as:', style={'textAlign':'justify','font-size':'18px'}),
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
                           html.Div('- Energy density and power density is energy and power normalized by the cell mass. Hence, the unit is Wh/kg and W/kg, respectively. Energy density can be approximated by multiplying specific capacity with nominal voltage.', style={'textAlign':'justify', 'font-size':'18px'}),
                           html.Br(),
                           html.Div('- Typically, it is difficult for batteries to have both metrics met at the high end. High energy density demands the cell to be discharged at a slow rate for it to reach its maximum capacity and avoid polarization losses. However, since a lower current rate means longer discharge time, power density will be low. For high power density, energy density is likely sacrificed. This trend is illustrated in a Ragone Plot.', style={'textAlign':'justify', 'font-size':'18px'}),
                           ], width={"size": 8}, style={'margin-bottom':'20px'},
                           xs=12, sm=10, md=10, lg=8, xl=8
                           ), 
                          dbc.Col([
                          html.Div( html.Img(src='https://dl.dropboxusercontent.com/scl/fi/95o1wg7pysd41mx7qd1jy/Ragone-plot.bmp?rlkey=3d7offwomdyp0qn7b0tw6fwk6&raw=1', style={"width":"140%"}), 
                                   ),
                          html.Div(('Courtesy: Venkat Srinivasan'), 
                                   style={'textAlign':'justify', 'font-size':'15px', 'font-style':'italic', 'margin-left':'0px'}),  
                          ], width={"size": 3},
                          xs=8, sm=8, md=6, lg=6, xl=3),
                      ],),
                    ])
                ],
                style={'textAlign':'justify', 'margin-left':'30px', 'margin-right':'30px'},
                ),
                ],
                ),
                ],),
                html.Div(id='tabs-content'),
])
