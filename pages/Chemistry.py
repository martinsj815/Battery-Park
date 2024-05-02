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
    __name__, name="Chemistry", top_nav=True, path="/chemistry"
    )

data_election = OrderedDict(
    [
        (
            "Cathode Name",
            [
                "Lithium Cobalt Oxide (LCO)",
                "Lithium Manganese Oxide",
                "Lithium Iron Phosphate (LFP)",
                "Lithium Nickel Cobalt Manganese Oxide (NCM111)",
                "Lithium Nickel Cobalt Manganese Oxide (NCM622)",
                "Lithium Nickel Cobalt Manganese Oxide (NCM811)",
                "Lithium Nickel Cobalt Aluminum Oxide (NCA)",
            ], 
        ),
        (
            "Crystal Structure",
            [
                "Layered", 
                "Spinel", 
                "Olivine",
                "Layered",
                "Layered",
                "Layered",
                "Layered",             
            ],
        ),
        (
            "Stoichiometry", 
            [
                "LiCoO<sub>2</sub>", 
                "LiMn<sub>2</sub>O<sub>4</sub>",
                "LiFePO<sub>4</sub>",
                "Li[Ni<sub>0.33</sub>Co<sub>0.33</sub>Mn<sub>0.33</sub>]O<sub>2</sub>",
                "Li[Ni<sub>0.6</sub>Co<sub>0.2</sub>Mn<sub>0.2</sub>]O<sub>2</sub>",
                "Li[Ni<sub>0.8</sub>Co<sub>0.1</sub>Mn<sub>0.1</sub>]O<sub>2</sub>",
                "LiNi<sub>0.8</sub>Co<sub>0.15</sub>Al<sub>0.05</sub>O<sub>2</sub>",
            ]
        ),
        (
            "Specific Capacity (mAh/g) \n (The/Exp)",
            [
                "274/148<sup>a</sup>",
                "148/120<sup>a</sup>",
                "170/165<sup>a</sup>",
                "280/160<sup>a</sup>",
                "275/170<sup>b</sup>",
                "275/190<sup>b</sup>",
                "279/200<sup>a</sup>",
            ],
        ),
        (
            "Average Voltage \n (V)",
            [
                "3.8<sup>a</sup>",
                "4.1<sup>a</sup>",
                "3.4<sup>a</sup>",
                "3.7<sup>a</sup>",
                "3.7<sup>b</sup>",
                "3.7<sup>b</sup>",
                "3.7<sup>a</sup>",
            ],
        ),
        (
            "Electrical Conductivity (S/cm)",
            [
                "",
                "",
                "5x10<sup>-8</sup><sup>d</sup>",
                "5.2x10<sup>-8</sup><sup>c</sup>",
                "1.6x10<sup>-6</sup><sup>c</sup>",
                "1.7x10<sup>-5</sup><sup>c</sup>",
                "",
            ],
        ),
        (
            "Exothermic Rxn T (Deg)",
            [
                "",
                "",
                "250-360<sup>d</sup>",
                "306<sup>d</sup>",
                "260<sup>d</sup>",
                "232<sup>d</sup>",
                "",
            ],
        ),
        (
            "Heat Release (J/g)",
            [
                "",
                "",
                "147<sup>d</sup>",
                "512.5<sup>d</sup>",
                "721.4<sup>d</sup>",
                "904.8<sup>d</sup>",
                "",
            ],
        ),
        (
            "Pros",
            [
                "* Good structural stability",
                "* Cost efficient",
                "* Cost affordable \n * Thermal stability",
                "",
                "",
                "* High specific capacity \n * High energy density",
                "* High specific capacity \n * High energy density",
            ],
        ),
        (
            "Cons",
            [
                "* Co expensive \n * Unstable upon charging >50%",
                "* Mn dissolution in electrolyte",
                "* Low ionic conductivity \n * Low energy density",
                "",
                "",
                "* Cycle instability for high Ni content \n * Co expensive",
                "* Cycle/Thermal instability \n * Co expensive",
            ],
        ),
    ],
)

dt = pd.DataFrame(data_election)

data_election2 = OrderedDict(
    [
        (
            "Type",
            [
                "Sulfide (S-SIE)",
                "Oxide (O-SIE)",
                "Polymer",
            ], 
        ),
        (
            "Example System",
            [
                "- Li<sub>9.54</sub>Si<sub>1.74</sub>P<sub>1.44</sub>S<sub>11.7</sub>Cl<sub>0.3</sub> \n - Li<sub>3.833</sub>Sn<sub>0.833</sub>As<sub>0.166</sub>S<sub>4</sub> \n - Li<sub>6</sub>PS<sub>5</sub>Br \n - Li<sub>7</sub>P<sub>3</sub>S<sub>11</sub> \n - Li<sub>10</sub>GeP<sub>2</sub>S<sub>12</sub>", 
                "- Li<sub>7</sub>La<sub>3</sub>Zr<sub>2</sub>O<sub>12</sub> (Garnet) \n - Li<sub>0.5</sub>La<sub>0.5</sub>TiO<sub>3</sub> (Perovskite) \n - Li<sub>3</sub>OCl (Antiperovskite) \n - LISICON, NASICON", 
                "- LiTFSI-PEO(Mw=5000000) \n - LiClO<sub>4</sub>-PEO(Mw=600000) \n - LiClO<sub>4</sub>-PEO with 5wt&#37; elliptical TiO<sub>2</sub> rods \n - LiClO4-PEO with 5wt&#37; elliptical TiO<sub>2</sub> rods",          
            ],
        ),
        (
            "Conductivity (mS/cm)", 
            [
                "0.1-50", 
                "0.01-1",
                "0.1-1 (at 90 oC)",
            ]
        ),
        (
            "Advantages",
            [
                "- High ionic condutivity \n - Good mechanical strength and flexibilty",
                "- High chemical and electrochemical stability (High  electrochemical oxidation voltage) \n - High mechanical strength",
                "- Stable with lithium metal \n - Flexibility and low shear modulus \n - Easy to produce a large area membrance",
            ],
        ),
        (
            "Disadvantages",
            [
                "- Sensitive to moisture and produces H<sub>2</sub>S from decomposition \n - Poor compatibiltiy with cathode materials due to low oxidation stability",
                "- Non-flexible and brittle \n - Expensive large-scale production (require sintering process)",
                "- Limited thermal stability \n - Low ionic conductivity \n  - Low oxidation voltage (< 4V)",
            ],
        ),
    ],
)

dt2 = pd.DataFrame(data_election2)

data_election3 = OrderedDict(
    [
        (
            "Company",
            [
                "OneD",
                "Sila",
                "Group14",
                "StoreDot",
                "IonBlox",
                "Amprius",
                "Evonix",
            ], 
        ),
        (
            "Key Technology",
            [
                "Sinanode -  Silicon NW embedded on graphite powder pore via melting",
                "Titan Silicon - Micron-sized Carbon Scaffolded particles consist of nanostructured Si",
                "SCC55 - Carbon scaffolded structure with intraparticle voids for silicon expansion",
                "XFC (Extreme Fast Charging) Si - Slicon synthesized with \"small-molecule organic compounds\"",
                "Pre-lithiated silicon oxide",
                "SiCore - 4 layers: Si Nanostructure/ Stabilization layer/Carbon/Fast ion conductor",
                "100% Silicon crosswise stacked inside the novel mechanical architecture ",    
            ],
        ),
        (
            "Performance Noted", 
            [
                "- 678 mAh/g (at 10 wt&#37;)", 
                "- <6&#37; at EOL (900 cycles) \n - 20&#37; increase in driving range \n - 10-80&#37; recharge in 20 minutes",
                "- Upto 5x capacity than graphite \n - 50&#37; more energy density than graphite",
                "- 100 miles recharge in 5 minutes \n - Energy Density of 330 Wh/kg and 860Wh/L \n - 2000 cycles with 80&#37; initial capacity maintained",
                "- 225 miles in 5 min charge \n - 390 miles in 10 min charge",
                "- Upto 500 Wh/kg or 1300 Wh/L \n - 0-80&#37; recharge in <6 minutes",       
                "- <2&#37; after 500 cycles \n - 43&#37;/65&#37; capacity increase in laptops/cellphones",   
            ]
        ),
        (
            "Link",
            [
                "https://onedsinanode.com/sinanode/",
                "https://www.wired.com/story/panasonic-powder-powered-silicone-ev-batteries/ \n https://www.silanano.com/our-solutions/titan-silicon-anode",
                "https://www.group14.technology/resources/whitepapers/whitepaper-the-transition-to-lithium-silicon-batteries/",
                "https://www.store-dot.com/technology \n https://www.prnewswire.com/news-releases/storedot-hits-commercialization-milestone-with-2-000-extreme-fast-charging-xfc-cycles-elevating-ev-longevity-durability-and-market-value-302107541.html",
                "https://www.ionblox.com/land \n https://www.businesswire.com/news/home/20231004555440/en/Ionblox-Debuts-Lithium-Silicon-Batteries-Breaking-Barriers-of-Extreme-Fast-Charging-and-Extended-Range",
                "https://amprius.com/amprius-broadens-product-portfolio-with-new-commercially-available-silicon-anode-battery-platform-sicoretm/ \n https://amprius.com/technology/",
                "https://www.techhive.com/article/2189816/enovix-silicon-battery-tech-65-more-from-you-li-ion-batteries.html",
            ],
        ),
    ],
)

dt3 = pd.DataFrame(data_election3)

layout = html.Div([
             html.Link(rel='stylesheet', href='/assets/table.css'),            
             dbc.Row([
                dbc.Col([
                    html.Div(
                        dcc.Markdown('Li ion battery', style={'font-size':'30px', 'textAlign':'center','font-weight':'bold'},),
                        style={'text-align':'center'}),
                    html.Br(),
                    dbc.Row([
                        dbc.Col([
                         dcc.Markdown(('- Lithium-ion batteries are consisting of a host material with a high redox potential (> 3V vs Li) as a cathode and that of a low electrochemical potential (vs Li) as an anode. Typically, lithium transition metal oxides are cathodes while graphite is an anode, both of which undergo Li (de-)intercalation during charge and discharge.'), 
                                 style={'textAlign':'justify', 'margin-left':'20px', 'font-size':'18px'}),
                        dcc.Markdown(('- Upon discharge, lithium ions migrate from the anode (e.g. lithiated graphite) towards the electrolyte while electrons move through the external circuit. Lithium ions are then carried by the electrolyte and flow into the cathode along with electrons. Upon charge, the process is reversed with the help of electrical energy injected.'), 
                                 style={'textAlign':'justify', 'margin-left':'20px', 'font-size':'18px'}),
                        ], width={"size": 7},
                        xs=7, sm=10, md=10, lg=7, xl=7
                        ),
                        dbc.Col([
                            html.Div( html.Img(src='https://dl.dropboxusercontent.com/scl/fi/2v296fyhu4q2l0fg32xsn/Li-ion-battery.png?rlkey=6a134a2mdyuq88c4ksrgt0xuq&raw=1', style={"width":"100%", "display":"block", "margin":"auto"}), 
                                 ),
                        ], width={"size": 5},
                        xs=4, sm=10, md=8, lg=5, xl=5
                        ),
                    ],
                    ),
                    html.Br(),
                    dmc.Divider(size="md", color="grey", style={"width":"100%", "display":"block", "margin":"auto"}),
                    html.Br(),
                    dbc.Row([
                        dcc.Markdown('* Cathode Materials', style={'font-size':'25px', 'textAlign':'left','font-weight':'bold'}),      
                        html.Br(),
                        dbc.Col([
                            dcc.Markdown(("* Since the voltage is dictated by the redox energy difference between the cathode and the anode, it is imperative to have the cathode to reach the lower energy band of a metal ion at the higher oxidation state to increase the cell voltage."), dangerously_allow_html=True,
                                 style={'textAlign':'justify', 'margin-left':'20px', 'font-size':'18px'}),   
                            dcc.Markdown(("* The use of transition metal oxide instead of sulfide (e.g. TiS<sub>2</sub>) enables an increase in cell voltage by accessing the energy bands lying low in the energy band diagram as the O<sup>2-</sup> 2p band lies at a lower energy below a S<sup>2-</sup> 3p band."), dangerously_allow_html=True,
                                 style={'textAlign':'justify', 'margin-left':'20px', 'font-size':'18px'}),          
                            dcc.Markdown(("* Typical transition metal oxides used for the cathode have spinel, layered, or olivine structures that undergo Li (de-)intercalation."), dangerously_allow_html=True,
                                 style={'textAlign':'justify', 'margin-left':'20px', 'font-size':'18px'}), 
                        ], width={"size": 7},
                        xs=6, sm=10, md=10, lg=7, xl=7
                        ),
                        dbc.Col([
                            html.Div( html.Img(src='https://www.dropbox.com/scl/fi/rh1v74c9n5ssyzd1j69o6/Energy-band-diagram.png?rlkey=3okh20dnktic1w9jflso5wob5&raw=1', style={"width":"80%", "display":"block", "margin":"auto"}), 
                                 ),
                            dcc.Markdown('<b>Image Courtesy</b>: A. Manthiram, Nature Commun. 11, 1550 (2020)', dangerously_allow_html=True, ),
                        ], width={"size": 5},
                        xs=4, sm=10, md=8, lg=5, xl=5
                        ),   
                    ]),    
                    html.Br(), 
                    dcc.Markdown('* Cathode Comparison Table', style={'font-size':'20px', 'textAlign':'left','font-weight':'bold'}),     
                    dash_table.DataTable(
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
                                data=dt.to_dict('records'),
                                columns=[{'id': c, 'name': c,"presentation": "markdown"} for c in dt.columns],
                    ),
                    html.Br(),
                    dbc.Row([
                        dbc.Col([
                            dcc.Markdown('* Global Demand for Cathode Chemistries', style={'font-size':'25px', 'textAlign':'left','font-weight':'bold'}),      
                            html.Br(),
                            dcc.Markdown(("* According to the review paper by Degen et al., both High-Ni NCM cathode and LFP cathode chemistry continue to rise in their demands while those of NCM532/622 and NCA will be stagnant until 2040. It is also forecasted that the market share will be gradually dominated by the post-Li batteries in future although it is currently unknown which of the batteries (e.g. all-solid-state, lithium-sulfur, lithium-air, sodium-ion, etc) will reach industrial-scale production."), dangerously_allow_html=True,
                                 style={'textAlign':'justify', 'margin-left':'20px', 'font-size':'18px'}),   
                        ], width={"size": 7},
                        xs=6, sm=10, md=10, lg=7, xl=7
                        ),
                        dbc.Col([
                            html.Div( html.Img(src='https://www.dropbox.com/scl/fi/xqodsx0n9mtcc1kmvib8z/Global-Demand_Cathode-Chemistry.png?rlkey=1tp61jxqb1l2ida039w5qo7u5&raw=1', style={"width":"80%", "display":"block", "margin":"auto"}), 
                                 ),
                            dcc.Markdown('<b>Image Source</b>: F. Degen, et al., Nature Energy, 8 (2023)', dangerously_allow_html=True, ),
                        ], width={"size": 5},
                        xs=4, sm=10, md=8, lg=5, xl=5
                        ),   
                    ]),
                    dmc.Divider(size="md", color="grey"),
                    html.Br(),
                    dcc.Markdown('* Anode Materials', style={'font-size':'25px', 'textAlign':'left','font-weight':'bold'}),
                    html.Br(),
                    dbc.Row([
                        dcc.Markdown(('1. Intercalation-based:'), 
                                 style={'textAlign':'justify', 'margin-left':'20px', 'font-size':'20px', 'font-weight':'bold'}),
                        dbc.Row([
                            dbc.Col([
                                dcc.Markdown(("Carbon-based anode such as graphite has the theoretical capacity of 372 mAh/g and has a good (de-)lithiation potential vs. Li. Many carbon-based materials are engineered at nanoscale to optimize their morphologies for high structural stability and better electrochemical reversibility and capacity retention.  In terms of safety, stability, and power capability, titanium-based anodes such as Li<sub>4</sub>Ti<sub>5</sub>O<sub>12</sub> and TiO<sub>2</sub> have an advantage over graphite, but their electronic conductivity is poor and specific capacities (175-330 mAh/g) and energy densities are low."), dangerously_allow_html=True,
                                     style={'textAlign':'justify', 'margin-left':'30px', 'font-size':'18px'}),
                            ], width={"size": 8},
                            xs=6, sm=10, md=10, lg=8, xl=8
                            ),
                            dbc.Col([
                                html.Div( html.Img(src='https://dl.dropboxusercontent.com/scl/fi/amcz0cvqdgvjqr3woa3nf/Intercalation.png?rlkey=12vrz2scdi4f4q8to5oiajt2n&raw=1', 
                                               style={"width":"80%", "display":"block", "margin":"auto"}), 
                                    ),
                            ], width={"size": 4},
                            xs=4, sm=10, md=8, lg=6, xl=4
                            ),
                        ], style={"margin-bottom":'5em'},
                        ), 
                        html.Br(),
                        html.Br(),
                        dcc.Markdown(('2. Alloying-based:'), 
                                 style={'textAlign':'justify', 'margin-left':'20px', 'font-size':'20px', 'font-weight':'bold'}), 
                        dbc.Row([
                            dbc.Col([  
                                dcc.Markdown(("Alloying anodes like Si, Ge, and Sn undergo the reaction: M + xLi<sup>+</sup> + xe<sup>-</sup> &rarr; Li<sub>x</sub>M. The biggest advantage of employing these materials as an anode is specific capacity, which is much higher than that of intercalation anode system. For example, Si has a specific capacity of ~4200 mAh/g. However, their large volumetric expansion upon lithiation poses a great threat to its mechanical stability (e.g. delamination from a current collector or loss of inter-particle cohesion) and contributes to a capacity fade of the cell. Nano-structuring of Si as an anode has attracted interest to overcome such problems. In fact, Si or SiO<sub>x</sub> is considered to be added in small percentage amount (e.g. 2-10 wt%) inside the graphite anode to boost energy density of the anode."), dangerously_allow_html=True,
                                     style={'textAlign':'justify', 'margin-left':'30px', 'font-size':'18px'}
                                    ),
                            ], width={"size": 8},
                            xs=6, sm=10, md=10, lg=8, xl=8
                            ),    
                            dbc.Col([
                                html.Div( html.Img(src='https://dl.dropboxusercontent.com/scl/fi/q99hom4wf01a5zdqc4jko/TiO2-Si.gif?rlkey=nnzxks6pzow17fme2yszhyu0v&raw=1', 
                                               style={"width": "60%", "display": "block", "margin": "auto"}
                                               ),
                                    ),
                            ], width={"size": 4},
                            xs=4, sm=10, md=8, lg=6, xl=4
                            ),                             
                        ], style={"margin-bottom":'5em'},
                        ), 
                        html.Br(),
                        html.Br(),
                        dcc.Markdown(('3. Conversion-based:'), 
                                 style={'textAlign':'justify', 'margin-left':'20px', 'font-size':'20px', 'font-weight':'bold'}),
                        dbc.Row([
                            dbc.Col([
                                dcc.Markdown(("Conversion-based anodes such as metal oxides undergo the following reaction: M<sub>x</sub>O<sub>y</sub> + 2yLi<sup>+</sup> + 2ye<sup>-</sup> &rarr; yLi<sub>2</sub>O + xM. Despite their high specific capacities, they suffer from multiple issues including structural instability due to pulverization and voltage hysteresis owing to sluggish kinetics during the conversion process to different phases."), dangerously_allow_html=True,
                                 style={'textAlign':'justify', 'margin-left':'30px', 'font-size':'18px'}),  
                                ], width={"size": 8},
                                xs=6, sm=10, md=10, lg=8, xl=8
                            ),   
                            dbc.Col([
                                html.Div( html.Img(src='https://www.dropbox.com/scl/fi/3ty73w1vp5v44d5x9y94j/ConversionII.png?rlkey=7qw6qqtc8kgaeudroe1556keq&st=aph7cdkg&raw=1', 
                                               style={"width":"100%", "display": "block", "margin": "auto"}), 
                                    ),
                            ], width={"size": 4},
                            xs=4, sm=10, md=8, lg=6, xl=4
                            ),  
                        ], style={"margin-bottom":'5em'},
                        ),  
                        html.Br(),
                        dmc.Divider(size="md", variant="dotted", color="grey"),                
                        html.Br(),
                        dcc.Markdown(('- Silicon-based anode manufacturers'), 
                                 style={'textAlign':'justify', 'font-size':'25px', 'font-weight':'bold'}),                        
                        dash_table.DataTable(   
                                style_cell={'font-family': 'Arial', 'font-size': '16px', 'text-align':'auto', 'margin-top':'auto', 'width':'auto','padding':2}, 
                                markdown_options={"html": True},
                                #virtualization=True,
                                style_table={'overflowX': 'auto', 'margin-bottom':'20px'},
                                style_data={
                                        'whiteSpace': 'break-spaces',
                                        'color': 'black',
                                        'backgroundColor': 'white',
                                        'height':'auto',
                                        'lineheight':'10px',
                                },
                                style_data_conditional=[
                                {
                                    'if': {'column_id': 'Company'},
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
                                data=dt3.to_dict('records'),
                                columns=[{'id': c, 'name': c,"presentation": "markdown"} for c in dt3.columns],
                        ),
                        html.Br(),             
                        html.Br(),               
                        dmc.Divider(size="md", color="grey"),  
                        html.Br(),
                        html.Br(),
                        dcc.Markdown(('* Electrolyte'), 
                                 style={'textAlign':'justify', 'margin-left':'0px', 'font-size':'25px', 'font-weight':'bold'}),
                        html.Br(),
                        dbc.Row([
                            dbc.Col([
                            html.Div(('-Electrolyte acts as a medium for ion transport between the cell cathode and anode during (dis-)charging. It can be in liquid, solid or even polymer gel-type. Liquid non-aqueous electrolyte, most commonly used, consists of salt(s) dissolved in solvent(s) along with additive(s).'), 
                                 style={'textAlign':'justify', 'font-size':'18px', 'margin-left':'30px', 'margin-bottom':'10px'}),  
                            html.Div(('-Ionic transport (i.e. ionic conductivity) is the key aspect of the non-aqueous Li-ion battery electrolyte. It is important for the electrolyte to possess high dielectric constant for salt dissolution, low viscosity for good ion transport, and chemical/thermal stability over a wide operating voltage/temperature range. When inserted in a cell, reductive and oxidative stability against anode and cathode (i.e. wide electrochemical stability window) is also desired for safe/stable operation of the cell.'), 
                                 style={'textAlign':'justify', 'font-size':'18px', 'margin-left':'30px', 'margin-bottom':'10px'}),  
                            dcc.Markdown(dangerously_allow_html=True, children=('-As no single salt and solvent mixture can provide many of desired characteristics above, electrolyte studied typically consists of multiple salts and/or solvents mixed. A good example is lithium hexafluorophosphate (LiPF<sub>6</sub>) dissolved in mixture of cyclic carbonate like ethylene carbonate (for high dielectric constant) and aliphatic carbonate such as diethyl, dimethyl, or ethyl methyl carbonate (for low viscosity and melting point).'), 
                                 style={'textAlign':'justify', 'font-size':'18px', 'margin-left':'30px', 'margin-bottom':'10px'}),    
                              ], width={"size": 7},
                            xs=10, sm=10, md=10, lg=7, xl=7,
                            ),       
                            dbc.Col([
                                html.Div( html.Img(src='https://www.dropbox.com/scl/fi/3xq79frdklaexeloiwezd/Electrolyte.png?rlkey=9cdaj3mnchhm40j1dte7tbd1h&raw=1', 
                                               style={"width":"80%", "display": "block", "margin": "auto"}), 
                                 ),
                            ], width={"size": 5},
                            xs=14, sm=12, md=8, lg=5, xl=5,
                            ),   
                        ],  style={"margin-bottom":'2em'},
                        ),
                        dbc.Row([
                            dbc.Col([
                            dcc.Markdown(('- Salt'), 
                                 style={'textAlign':'justify', 'font-size':'25px', 'font-weight':'bold', 'margin-left':'10px', 'margin-bottom':'10px'}),  
                            dcc.Markdown(dangerously_allow_html=True, children=('-LiPF<sub>6</sub> has no outstanding property but has the combination of its well-balanced characteristics that meet stringent requirements for commercialization. It also has good anodic stability up to >5V when mixed in carbonates and ionic conductivity. However, its poor thermal stability and moisture sensitivity requires the additive for performance enhancement.'), 
                                 style={'textAlign':'justify', 'font-size':'18px', 'margin-left':'30px', 'margin-bottom':'10px'}),  
                            html.Br(),
                            dcc.Markdown(dangerously_allow_html=True, children=('<b>Ion Mobility (Descending order)</b>: LiBF<sub>4</sub> > LiClO<sub>4</sub> > LiPF<sub>6</sub> > LiAsF<sub>6</sub> > LiTFSI' ), 
                                 style={'textAlign':'justify', 'font-size':'18px', 'margin-left':'30px'}),  
                            dcc.Markdown(dangerously_allow_html=True, children=('<b>Dissociation Constant (Descending order)</b>: LiTFSI > LiAsF<sub>6</sub> > LiPF<sub>6</sub> > LiClO<sub>4</sub> > LiBF<sub>4</sub>' ), 
                                 style={'textAlign':'justify', 'font-size':'18px', 'margin-left':'30px'}),                          
                            html.Br(),       
                            dcc.Markdown(dangerously_allow_html=True, children=('<b>- Other salts/additives studied/considered are: </b>'), 
                                 style={'textAlign':'justify', 'font-size':'20px', 'margin-left':'20px', 'margin-bottom':'0px'}),     
                            dcc.Markdown(dangerously_allow_html=True, children=('<b>LiBF<sub>4</sub></b>: Better thermal and stability against hydrolysis than LiPF<sub>6</sub>. However, it has mediocre ionic conductivity due to its low dissociation ability than LiPF<sub>6</sub>.'), 
                                 style={'textAlign':'justify', 'font-size':'18px', 'margin-left':'50px', 'margin-bottom':'10px'}), 
                            dcc.Markdown(dangerously_allow_html=True, children=('<b>LiAsF<sub>6</sub></b>: Good ionic conductivity and enhanced thermal and anodic stability due to strong As-F bonding. However, AsF<sub>3</sub> byproduct is toxic, hindering its commercialization.'), 
                                 style={'textAlign':'justify', 'font-size':'18px', 'margin-left':'50px', 'margin-bottom':'10px'}),  
                            dcc.Markdown(dangerously_allow_html=True, children=('<b>LiTFSI</b>: Good electrochemical stability against oxidation due to delocalized negative charges in TFSI<sup>-</sup> anions. Also has good ionic conductivity and thermal stability. Al corrosion, however, can make it not very applicable.'), 
                                 style={'textAlign':'justify', 'font-size':'18px', 'margin-left':'50px', 'margin-bottom':'10px'}),     
                            dcc.Markdown(dangerously_allow_html=True, children=('<b>LiFSI</b>: Higher conductivity and better hydrolytic and thermal stability than LiPF<sub>6</sub> in carbonate solvents. Al corrosion not happening at the high potential where the cathode redox happens.'), 
                                 style={'textAlign':'justify', 'font-size':'18px', 'margin-left':'50px', 'margin-bottom':'10px'}),        
                            dcc.Markdown(dangerously_allow_html=True, children=('<b>LiBOB (lithium bis(oxalate)borate)</b>: SEI formation at the graphite anode surface through the BOB anion for reversible Li (de-)insertion. Good thermal stability and resistant to Al corrosion at the high potential. However, less versatile for application due to limited solubility in carbonates and low anodic stability (4.2V).'), 
                                 style={'textAlign':'justify', 'font-size':'18px', 'margin-left':'50px', 'margin-bottom':'10px'}),     
                            dcc.Markdown(dangerously_allow_html=True, children=('<b>LiDFOB (lithium difluoro(oxalate)borate)</b>: Hybridized form of LiBOB with LiBF4. Higher solubility than LiBOB in carbonate electrolyte with less viscosity and higher ionic conductivity. Cell impedance comparable to LiPF6-based electrolyte.'), 
                                 style={'textAlign':'justify', 'font-size':'18px', 'margin-left':'50px', 'margin-bottom':'10px'}),   
                            dcc.Markdown(dangerously_allow_html=True, children=('<b>LiPO<sub>2</sub>F<sub>2</sub> (only as additive)</b>: Forms the stable interface film both at cathode and anode surface upon cycling, preventing decomposition/oxidation of the electrolyte. This allows impedance control of both cathode and anode and is conducive to cathode structural stability, high-rate capability, and prolonged cell cycling.'), 
                                 style={'textAlign':'justify', 'font-size':'18px', 'margin-left':'50px', 'margin-bottom':'30px'}),   
                            dcc.Markdown(dangerously_allow_html=True, children=('-Many 18650 cells use the mixture of LiPF<sub>6</sub> and LiFSI inside carbonate electrolyte as the electrolyte. For EV batteries with an increasingly rigorous demand for their performances, some of the salts above are investigated as additive to be mixed with LiPF<sub>6</sub> electrolyte, for which its concentration varies from 5-10%.'), 
                                 style={'textAlign':'justify', 'font-size':'18px', 'margin-left':'20px', 'margin-bottom':'10px'}),       
                            ], width={"size": 16},
                            xs=10, sm=10, md=10, lg=10, xl=16,
                            ),   
                        ],),
                        html.Br(),
                        dcc.Markdown(('* Solid Electrolyte'), 
                                 style={'textAlign':'justify', 'margin-left':'0px', 'font-size':'25px', 'font-weight':'bold','margin-top':'20px'}),
                        html.Br(),
                        dbc.Row([
                            dbc.Col([
                            html.Div(('A solid electrolyte is a solid ionic conductor that acts as a medium for ion transport between the cell cathode and the anode. These materials should be electrically insulating but ionically conductive, and electrochemically stable with both the cathode and anode. The solid electrolyte can replace the liquid electrolyte and separator of the cell.'), 
                                 style={'textAlign':'justify', 'font-size':'18px', 'margin-left':'30px', 'margin-bottom':'10px'}),  
                            html.Div(('Solid electrolytes are attracting a large interest since it enables all-solid-state batteries with excellent thermal stability, high energy density, and fast charge capability. The solid electrolyte materials can be classified into sulfide solid inorganic electrolytes (S-SIE), oxide solid inorganic electrolyte (O-SIE), and solid polymer electrolytes (SPE).'), 
                                 style={'textAlign':'justify', 'font-size':'18px', 'margin-left':'30px', 'margin-bottom':'10px'}),  
                            dcc.Markdown(dangerously_allow_html=True, children=('To be comparable to conventional liquid electrolytes, the ionic conductivity should be in the order of 1 mS/cm at room temperature. S-SIE has generally higher ionic conductivity and forms a good interface with electrodes due to its soft Li-S bonding properties, but has the performance disadvantages of stability due to the narrow electrochemical stability window. O-SEI has good electrochemical stability but is difficult to handle in large-scale production. While SPE has low ionic conductivity and requires high temperature to operate, it is stable with lithium metal, forming a good interface with the electrode, and can be applied in a current roll-to-roll process. '), 
                                 style={'textAlign':'justify', 'font-size':'18px', 'margin-left':'30px', 'margin-bottom':'10px'}),    
                              ], width={"size": 7},
                            xs=10, sm=10, md=10, lg=7, xl=7,
                            ),       
                            dbc.Col([
                                html.Div( html.Img(src='https://www.dropbox.com/scl/fi/dpha6db50capip8eox2y4/LiPS.png?rlkey=tjc5xo629u3w8z3b2wb13v8x0&st=galjz4fk&raw=1', 
                                               style={"width":"90%", "display": "block", "margin": "auto"}), 
                                 ),
                            ], width={"size": 5},
                            xs=14, sm=12, md=8, lg=5, xl=5,
                            ),   
                        ],  style={"margin-bottom":'2em'},
                        ),
                        dbc.Row([
                            dbc.Col([
                            dash_table.DataTable(
                                style_cell={'font-family': 'Arial', 'font-size': '16px', 'text-align':'center', 'margin-top':'10px', 'padding':5}, 
                                markdown_options={"html": True},
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
                                    'if': {'column_id': 'Type'},
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
                                data=dt2.to_dict('records'),
                                columns=[{'id': c, 'name': c,"presentation": "markdown"} for c in dt2.columns],
                                ),
                            ],
                            width={"size": 16}, style={"margin-bottom":'20px'},
                            xs=5, sm=10, md=10, lg=10, xl=16,
                            ),
                        ]),
                        html.Br(),
                        dmc.Divider(size="md", color="grey"),
                        html.Br(),
                        dbc.Col([
                            dcc.Markdown(('* References'), 
                                 style={'textAlign':'justify', 'margin-left':'20px', 'font-size':'30px', 'font-weight':'bold'}),                                               
                            dcc.Markdown(('F. Degen, et al, "Energy consumption of current and future production of lithium-ion and post lithium-ion battery cells", _**Nature Energy**_, 8, 1284 (2023)'), 
                                style={'textAlign':'justify', 'font-size':'18px', 'margin-left':'30px'}),
                            dcc.Markdown(('Naoki Nitta, et al, "Li-ion battery materials: present and future", _**Mater. Today**_, 18, 252 (2015) \n _(a in Cathode Comparison Table)_'), 
                                style={'textAlign':'justify', 'font-size':'18px', 'margin-left':'30px'}),
                            dcc.Markdown(('Florian Schipper, et al, "Review—Recent Advances and Remaining Challenges for Lithium Ion Battery Cathodes", _**J. Electrochem. Soc.**_, 164, A6220 (2017) \n _(b in Cathode Comparison Table)_'), 
                                style={'textAlign':'justify', 'font-size':'18px', 'margin-left':'30px'}),
                            dcc.Markdown(('Hyung-Joo Noh, et al., "Comparison of the structural and electrochemical properties of layered Li\[NixCoyMnz]O2 (x = 1/3, 0.5, 0.6, 0.7, 0.8 and 0.85) cathode material for lithium-ion batteries", _**J. Power Sources**_, 233, 121 (2013) _(c in Cathode Comparison Table)_'), 
                                style={'textAlign':'justify', 'font-size':'18px', 'margin-left':'30px'}),
                            dcc.Markdown(('Yuki Orikasa, et al., "Ionic Conduction in Lithium Ion Battery Composite Electrode Governs Cross-sectional Reaction Distribution", _**Sci. Rep.**_, 6, 26382 (2016) _(d in Cathode Comparison Table)_'), 
                                style={'textAlign':'justify', 'font-size':'18px', 'margin-left':'30px'}),  
                            dcc.Markdown(('Xiao-Guang Yang, et al., "Thermally modulated lithium iron phosphate batteries for mass-market electric vehicles", _**Nature Energy**_, 6, 176 (2021) _(d in Cathode Comparison Table)_'), 
                                style={'textAlign':'justify', 'font-size':'18px', 'margin-left':'30px'}),                          
                            dcc.Markdown(('Arumugam Manthiram, "A reflection on lithium-ion battery cathode chemistry", _**Nature Commun.**_, 11, 1550 (2020)'), 
                                style={'textAlign':'justify', 'font-size':'18px', 'margin-left':'30px'}),
                            dcc.Markdown(('Jun Lu, et al, "High‑Performance Anode Materials for Rechargeable Lithium‑Ion Batteries", _**Electrochemical Energy Reviews**_, 1:35 (2018)'), 
                                style={'textAlign':'justify', 'font-size':'18px', 'margin-left':'30px'}),
                            dcc.Markdown(('Hui Cheng, et al, "Recent progress of advanced anode materials of lithium-ion batteries", _**Journal of Energy Chemistry**_, 57, 451 (2021)'), 
                                 style={'textAlign':'justify', 'font-size':'18px', 'margin-left':'30px'}),                         
                            dcc.Markdown(('Kang Xu, "Electrolytes and Interphases in Li-ion Batteries and Beyond", _**Chemical Review**_, 114, 11503 (2014)'), 
                                 style={'textAlign':'justify', 'font-size':'18px', 'margin-left':'30px'}),                         
                            dcc.Markdown(('E. R. Logan, et al., "A Study of the Physical Properties of Li-Ion Battery Electrolytes Containing Esters", _**J. Electrochem. Soc.**_, 165, A21 (2018)'), 
                                 style={'textAlign':'justify', 'font-size':'18px', 'margin-left':'30px'}),
                            dcc.Markdown(('Kang Xu, "Nonaqueous Liquid Electrolytes for Lithium-Based Rechargeable Batteries", _**Chem. Rev.**_, 104, 4303 (2004)'), 
                                 style={'textAlign':'justify', 'font-size':'18px', 'margin-left':'30px'}),                              
                            dcc.Markdown(('Jiale Xing, et al., "A Review of Nonaqueous Electrolytes, Binders, and Separators for Lithium‑Ion Batteries", _**Electrochem. Energy Rev.**_, 5:14 (2022)'), 
                                 style={'textAlign':'justify', 'font-size':'18px', 'margin-left':'30px'}), 
                            dcc.Markdown(('Hong-Bo Han, et al., "Lithium bis(fluorosulfonyl)imide (LiFSI) as conducting salt for nonaqueous liquid electrolytes for lithium-ion batteries: Physicochemical and electrochemical properties", _**J. Power Sources**_, 196, 3623 (2011)'), 
                                 style={'textAlign':'justify', 'font-size':'18px', 'margin-left':'30px'}),                                 
                            dcc.Markdown(('Weimin Zhao, et al., "Toward a stable solid-electrolyte-interfaces on nickel-rich cathodes: LiPO2F2 salt-type additive and its working mechanism for LiNi0.5Mn0.25Co0.25O2 cathodes", _**J. Power Sources**_, 380, 149 (2018)'), 
                                 style={'textAlign':'justify', 'font-size':'18px', 'margin-left':'30px'}), 
                            dcc.Markdown(('Bowen Yang, et al., "Lithium difluorophosphate as an additive to improve the low temperature performance of LiNi0.5Co0.2Mn0.3O2/graphite cells", _**Electrochim. Acta**_, 221, 107 (2016)'), 
                                 style={'textAlign':'justify', 'font-size':'18px', 'margin-left':'30px'}),    
                            dcc.Markdown(('https://www.linkedin.com/pulse/application-lipo2f2-electrolyte-additive-lithium-ion-batteries-li/'), 
                                 style={'textAlign':'justify', 'font-size':'18px', 'margin-left':'30px'}), 
                            dcc.Markdown(('Qing Zhao, et al, "Designing solid-state electrolytes for safe, energy-dense batteries", _**Nature Reviews**_, 5, 229 (2020)'), 
                                style={'textAlign':'justify', 'font-size':'18px', 'margin-left':'30px'}),
                            dcc.Markdown(('Arumugam Manthiram,"Lithium battery chemistries enabled by solid-state electrolytes", _**Nature Reviews Materials**_, 2, 16103 (2017)'), 
                                style={'textAlign':'justify', 'font-size':'18px', 'margin-left':'30px'}),
                        ],width={"size": 16},
                            xs=10, sm=10, md=10, lg=10, xl=16,
                        )                                   
                    ],
                    ),
                ],
                ),
             ],
             style={'textAlign':'justify', 'margin-left':'30px', 'margin-right':'30px'},
             ),
             html.Div(id='Options-content'),
    ])
