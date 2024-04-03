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
    __name__, name="Cell Manufacturing", top_nav=True, path="/cell-manufacturing"
    )


layout = html.Div([
            dbc.Row([
                    dcc.Markdown(('- Cell manufacturing process'), 
                                    style={'textAlign':'justify', 'font-size':'30px', 'font-weight':'bold','margin-left':'0px'}),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Div( html.Img(src='https://dl.dropboxusercontent.com/scl/fi/4fkps6h0wzqhneo2wt10o/Cell-manuf2.png?rlkey=0cufo84m1sz7zi0aofp9ogq6r&raw=1', 
                                   style={"width":"100%", "margin":"0 auto", "display":"block"}),
                                   style={"textAlign":"center"} 
                            ),
                    html.Br(),
                    dmc.Divider(size="md", color="grey"),
                    html.Br(),
                    dbc.Col([
                        dbc.Row([
                                dcc.Markdown(('- Slurry Mixing'), style={'textAlign':'justify', 'font-size':'25px', 'font-weight':'bold'}),
                                dbc.Col([
                                        html.H5('- A typical slurry consists of the cathode (or anode) active material, conductive additive, and binder. A commonly used conductive additive is carbon black. An organic binder is usually a dielectric polymer like polyvinylidene fluoride (PVDF) with a wide good electrochemical stability window. As a binder solvent, N-methyl-2-pyrrolidone (NMP) is used to dissolve PVDF. Water-based binders such as carboxymethylcellulose (CMC) and styrene butadiene rubber (SBR) are considered as alternatives for cost-efficient and non-toxic processing.'),
                                        html.H5('- There are hydrodynamic shear mixing, ball-milling, and ultrasonic homogenization. Shear mixers (e.g. planetary mixers) are the most common for the industrial use. For mixing, sequence and additive properties (e.g. adhesion) are important.'),
                                        html.H5('- Since organic solvent drying is time-consuming and costly and commonly used NMP is toxic, water-based binders such as cellulose are proposed despite water not being compatible with many cathodes. Hence, increasing slurry concentration and even dry mixing are considered for improved cost, time, and energy efficiency later for coating/drying.'),
                                        html.H5('- Rheology of the slurry (e.g. viscosity, flow yield stress, wettability) is to be considered for slurry optimization, especially for later coating different thickness. Slurry viscosity can be determined by factors such as total solid loading, active material size and relative amount, binder molecular weight, etc.')
                                        ], width={"size": 8}, style={"textAlign":"justify"},
                                        xs=16, sm=16, md=10, lg=8, xl=8
                                        ),
                                dbc.Col([
                                        html.Div( html.Img(src='https://dl.dropboxusercontent.com/scl/fi/stqejbfqanx5m4x7z73il/mixing.png?rlkey=5906lmqao0oz2gimy3s1yf73b&raw=1', 
                                                                   style={"width":"40%", "display": "block", "margin": "auto"}), 
                                                ),
                                        ], width={"size": 4},
                                        xs=12, sm=12, md=6, lg=4, xl=4
                                    ),
                        ]),
                        html.Br(),
                        dmc.Divider(size="md", variant="dotted", color="grey"),
                        html.Br(),
                        dbc.Row([
                                dcc.Markdown(('- Coating'), style={'textAlign':'justify', 'font-size':'25px', 'font-weight':'bold'}),    
                                dbc.Col([
                                        html.H5('- Cathode materials are coated onto an aluminum current collector while the anode materials are coated onto a copper electrode.'),
                                         html.H5('- It is desirable that the surface tension of the mixed slurry matches with the surface energy of the current collector for proper wetting and coating.'),
                                        html.H5('- Solvent-based coating techqniues are the following:'),
                                        dcc.Markdown('* <b>Doctor blade coating</b>: Moving the doctor blade along the surface to even out the thickness and ensure that the active material is evenly distributed. It is most commonly used at the lab-scale for research.', dangerously_allow_html=True,
                                                     style={'textAlign':'justify', 'font-size':'20px', 'margin-left':'20px', 'line-height':'1.2'}),
                                        dcc.Markdown('* <b>Slot die coating</b>: Dispersing the slurry pushed through a narrow and adjustable slot-die onto the current collector. It is most widely used at the industrial level. Changing flow rate requires a change in pumping with good pressure drop control, which can be done by adjusting the slot gap using a thicker shim. Features are:', dangerously_allow_html=True,
                                                     style={'textAlign':'justify', 'font-size':'20px', 'margin-left':'20px', 'line-height':'1.2'}),                                                     
                                        dcc.Markdown('<b>a.</b> Advanced approach for enhanced thickness control, reproducibility, and flexibility \n\n<b>b.</b>Capable of coating multiple layers of different materials simultaneously and deposition of gradient or patterned coatings \n\n<b>c.</b> Key parameters: Slurry flow rate, pressure, temperature, shear, substrate speed, and distance from slot', dangerously_allow_html=True,
                                                     style={'textAlign':'justify', 'font-size':'20px', 'margin-left':'60px', 'line-height':'1.2'}),                                                    
                                        html.H5('- Solvent-free coating is under active investigation:'),
                                        dcc.Markdown('* <b>Maxwell-type</b> (developed by Maxwell Technologies): Include fibrillating that involves hot rolling and calendaring. (Narrow binder choice)', dangerously_allow_html=True, 
                                                     style={'textAlign':'justify', 'font-size':'20px', 'margin-left':'20px', 'line-height':'1.2'}),
                                        dcc.Markdown(('* <b>Electrostatic spraying</b>: Spraying dry mixture on a electrically grounded foil using an electrostatically charged gun. Followed by hot rolling for rigid adhesion with a current collector. (Wider binder choice)'), dangerously_allow_html=True, 
                                                     style={'textAlign':'justify', 'font-size':'20px', 'margin-left':'20px', 'line-height':'1.2'}),
                                        dcc.Markdown(('* <b>Hot pressing & melting</b>: Applicable to solid-state polymer electrolytes.'), dangerously_allow_html=True, 
                                                     style={'textAlign':'justify', 'font-size':'20px', 'margin-left':'20px', 'line-height':'1.2'}), 
                                        ], width={"size": 8},
                                        xs=16, sm=16, md=10, lg=8, xl=8
                                        ), 
                                dbc.Col([
                                        html.Br(),
                                        html.Br(),
                                        html.Br(),
                                        html.Div( html.Img(src='https://dl.dropboxusercontent.com/scl/fi/m09t2f1j35f3zy28xiyci/Coating.png?rlkey=dqyhew1487m6eac0oygbvdgzw&raw=1', 
                                                                   style={"width":"80%", "display": "block", "margin": "auto", "align-items":"center", "justify-content":"center"},
                                                                   ), 
                                                ),
                                        ], width={"size": 4},
                                        xs=12, sm=12, md=6, lg=4, xl=4
                                    ),                               
                        ]),
                        html.Br(),
                        dmc.Divider(size="md", variant="dotted", color="grey"),
                        html.Br(),
                        dbc.Row([
                                dcc.Markdown(('- Drying'), style={'textAlign':'justify', 'font-size':'25px', 'font-weight':'bold'}),    
                                dbc.Col([
                                        html.H5('- A wet electrode then dried for solvent evaporation. NMP solvent is recovered by a condenser and distillation. '),
                                        html.H5('- The wet slurry drying goes through the following - Slurry (Aggregation), Semi-slurry (Firm consolidation), Solid with solvent residue (Film shrinkage and formation of a condensed layer), and Solid (Pore empyting, segregation and bonding, formation of a compacted solid film coating) before full drying.'),
                                        html.H5('- A slurry mixed with water-based binder may take a longer time to dry than that with traditional NMP-based slurry despite being cost and time efficient for not having to go through the solvent recovery step.')
                                        ], width={"size": 8},
                                        xs=16, sm=16, md=10, lg=8, xl=8
                                        ), 
                                dbc.Col([
                                        html.Div( html.Img(src='https://dl.dropboxusercontent.com/scl/fi/7wx8erk8gtmyi24v3hm9c/drying.png?rlkey=ynetzmby0f66ngbp7hi3vhtjm&raw=1', 
                                                                   style={"width":"80%", "display": "block", "margin": "auto", "align-items":"center", "justify-content":"center"},
                                                                   ), 
                                                ),
                                        ], width={"size": 4},
                                        xs=12, sm=12, md=6, lg=4, xl=4
                                    ),                               
                        ]),
                        html.Br(),
                        dmc.Divider(size="md", variant="dotted", color="grey"),
                        html.Br(),
                        dbc.Row([
                                dcc.Markdown(('- Calendaring'), style={'textAlign':'justify', 'font-size':'25px', 'font-weight':'bold'}),    
                                dbc.Col([
                                        html.H5('- Process of smoothing and compressing a material during production by passing a single continuous sheet in between a pair of rolls.'),                                                 
                                        html.H5('- Reduces electrode porosity and alters pore microstructure with increased tortuosity. Increases the bonding strength between the electrode and the current collector. Improved particle contacts lead to energy and power density enhancement.'),
                                        ], width={"size": 8},
                                        xs=16, sm=16, md=10, lg=8, xl=8
                                        ), 
                                dbc.Col([
                                        html.Div( html.Img(src='https://www.dropbox.com/scl/fi/jau28k6txp44l9jpj4zi6/calendaring.png?rlkey=uw5pdwvr2v7enxrjal6zggset&raw=1', 
                                                                   style={"width":"80%", "display": "block", "margin": "auto", "align-items":"center", "justify-content":"center"},
                                                                   ), 
                                                ),
                                        ], width={"size": 4},
                                        xs=12, sm=12, md=6, lg=4, xl=4
                                    ),                               
                        ]),
                        html.Br(),
                        dmc.Divider(size="md", variant="dotted", color="grey"),
                        html.Br(),
                        dbc.Row([
                                dcc.Markdown(('- Slitting'), style={'textAlign':'justify', 'font-size':'25px', 'font-weight':'bold'}),    
                                dbc.Col([
                                        html.H5('-	Conventional process of cutting the large, coated film is by using a blade or chisel.'),                                                 
                                        html.H5('-	Laser cutting with good power and speed control is widely applied for improved shape and edge quality of the electrode.'),
                                        ], width={"size": 8},
                                        xs=16, sm=16, md=10, lg=8, xl=8
                                        ), 
                                dbc.Col([
                                        html.Div( html.Img(src='https://www.dropbox.com/scl/fi/r5dqebbqf3ta55nbu4wl2/Slitting.png?rlkey=xx2dkjjy1577srmuno34mw569&raw=1', 
                                                                   style={"width":"80%", "display": "block", "margin": "auto", "align-items":"center", "justify-content":"center"},
                                                                   ), 
                                                ),
                                        ], width={"size": 4},
                                        xs=12, sm=12, md=6, lg=4, xl=4
                                    ),                               
                        ]),
                        html.Br(),
                        dmc.Divider(size="md", variant="dotted", color="grey"),
                        html.Br(),
                        dbc.Row([
                                dcc.Markdown(('- Stacking/Winding/Rolling'), style={'textAlign':'justify', 'font-size':'25px', 'font-weight':'bold'}),    
                                dbc.Col([
                                        html.H5('-	All layers including electrodes and separators are wound into a spiral or jelly-rolled to be inserted in a cylindrical cell. In pouch cells, all layers are stacked layer by layer or via Z-stacking.'),                                                 
                                        ], width={"size": 8},
                                        xs=16, sm=16, md=10, lg=8, xl=8
                                        ), 
                                dbc.Col([
                                        html.Div( html.Img(src='https://www.dropbox.com/scl/fi/7yzf3xn86wnlgacl5ecd3/stacking.png?rlkey=wlahugx7hq56paf1q1hk4ovcr&raw=1', 
                                                                   style={"width":"80%", "display": "block", "margin": "auto", "align-items":"center", "justify-content":"center"},
                                                                   ), 
                                                ),
                                        ], width={"size": 4},
                                        xs=12, sm=12, md=6, lg=4, xl=4
                                    ),                               
                        ]),
                        html.Br(),
                        dmc.Divider(size="md", variant="dotted", color="grey"),
                        html.Br(),
                        dbc.Row([
                                dcc.Markdown(('- Welding'), style={'textAlign':'justify', 'font-size':'25px', 'font-weight':'bold'}),    
                                dbc.Col([
                                        html.H5('-	Contact resistance determines the quality of welding between tabs and current collectors. Ultrasonic welding uses high frequency to induce heat under applied pressure for welding. Resistance spot welding uses materials’ resistance for heat generation to join materials.'),                                                 
                                        ], width={"size": 8},
                                        xs=16, sm=16, md=10, lg=8, xl=8
                                        ), 
                                dbc.Col([
                                        html.Div( html.Img(src='https://www.dropbox.com/scl/fi/ivf9r4p2cclsxps0xud49/welding.png?rlkey=tip6417rbdewygdimnglz7nzp&raw=1', 
                                                                   style={"width":"60%", "display": "block", "margin": "auto", "align-items":"center", "justify-content":"center"},
                                                                   ), 
                                                ),
                                        ], width={"size": 4},
                                        xs=12, sm=12, md=6, lg=4, xl=4
                                    ),                               
                        ]),
                        html.Br(),
                        dmc.Divider(size="md", variant="dotted", color="grey"),
                        html.Br(),
                        dbc.Row([
                                dcc.Markdown(('- Enclosing'), style={'textAlign':'justify', 'font-size':'25px', 'font-weight':'bold'}),    
                                dbc.Col([
                                        html.H5('-Enclosing includes packaging and electrolyte filling. The filling process is done in vacuum through the desired pressure level using a high-precision injection device and is followed by wetting.'),                                                 
                                        html.H5('-Electrolyte wetting is influenced by electrode surface energy and morphology (e.g. pore structures), electrolyte viscosity and surface tension, etc.'),    
                                        ], width={"size": 8},
                                        xs=16, sm=16, md=10, lg=8, xl=8
                                        ), 
                                dbc.Col([
                                        html.Div( html.Img(src='https://www.dropbox.com/scl/fi/z8m8c2hh13qn07t6pjfwp/enclosing.png?rlkey=ekutn2m26ryu02a54qrwpghtm&raw=1', 
                                                                   style={"width":"40%", "display": "block", "margin": "auto", "align-items":"center", "justify-content":"center"},
                                                                   ), 
                                                ),
                                        ], width={"size": 4},
                                        xs=12, sm=12, md=6, lg=4, xl=4
                                    ),                               
                        ]),
                        html.Br(),
                        dmc.Divider(size="md", variant="dotted", color="grey"),
                        html.Br(),
                        dbc.Row([
                                dcc.Markdown(('- Formation/Aging'), style={'textAlign':'justify', 'font-size':'25px', 'font-weight':'bold'}),    
                                dbc.Col([
                                        html.H5('-Formation of the dense and robust SEI layer is needed for good battery performance without over-consumption of the electrolyte, especially for the graphite anode with intercalation potential lower than the reduction potential of electrolyte. The formation and aging process can be delicate and time-consuming as the amount of electrolyte relative to the materials that it covers; temperature, and pressure need to be controlled.'),
                                        html.H5('-Gases generated from formation cycles are released before final sealing or re-sealing.'),                                                 
                                        ], width={"size": 8},
                                        xs=16, sm=16, md=10, lg=8, xl=8
                                        ), 
                                dbc.Col([
                                        html.Div( html.Img(src='https://www.dropbox.com/scl/fi/qbc8fmi6rcx5lserwwnmw/formation.png?rlkey=6z5k47t7v74kgjgnfkpot6twz&raw=1', 
                                                                   style={"width":"40%", "display": "block", "margin": "auto", "align-items":"center", "justify-content":"center"},
                                                                   ), 
                                                ),
                                        ], width={"size": 4},
                                        xs=12, sm=12, md=6, lg=4, xl=4
                                    ),                               
                        ]),
                        html.Br(),
                        dmc.Divider(size="md", variant="dotted", color="grey"),
                        html.Br(),
                        dbc.Row([
                                dcc.Markdown(('- References'), style={'textAlign':'justify', 'font-size':'25px', 'font-weight':'bold'}),  
                                dcc.Markdown(('Jianlin Li, et al., "From Materials to Cell: State-of-the-Art and Prospective Technologies for Lithium-Ion Battery Electrode Processing", _**Chem. Review**_, 122, 903 (2022)'), style={'textAlign':'justify', 'font-size':'20px'}),                                                                                 
                                dcc.Markdown(('Yangtao Liu, et al., "Current and future lithium-ion battery manufacturing", _**iScience**_, 24, 102332 (2021)'), style={'textAlign':'justify', 'font-size':'20px'}),                                                                                      
                                dcc.Markdown(('W. Blake Hawley, et al., "Electrode Manufacturing for Lithium-Ion Batteries - Analysis of Current and Next Generation Processing", _**J. Energy Storage**_, 25, 100862 (2019)'), style={'textAlign':'justify', 'font-size':'20px'}),                                                                                     
                        ]),
                    ]), 
                ],style={'textAlign':'justify', 'margin-left':'30px', 'margin-right':'30px'},),
                html.Div(id='Options-content'),
        ])
