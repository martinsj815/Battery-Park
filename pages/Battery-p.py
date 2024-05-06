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
    __name__, name="battery packs", top_nav=True, path="/battery-p"
    )

data_election = OrderedDict(
    [
        (
            "Model",
            [
                "Model 3",
                "Model Y",
                "Model 3 LR Dual Motor",
                "Model Y LR Dual Motor",
                "Model S",
                "Model X",
            ], 
        ),
        (
            "Cell Format",
            [
                "Prismatic", 
                "Prismatic", 
                "Cylindrical",
                "Cylindrical",
                "Cylindrical",
                "Cylindrical",                            
            ],
        ),
        (
            "Material", 
            [
                "LFP", 
                "LFP",
                "NCM",
                "NCM",
                "NCA",
                "NCA",
            ]
        ),
        (
            "Pack Configuration",
            [
                "106s 1p",
                "106s 1p",
                "96s 46p",
                "96s 46p",
                "110s 72p",
                "110s 72p",
            ],
        ),
        (
            "Total Cell #",
            [
                "106",
                "106",
                "4416",
                "4416",
                "7920",
                "7920",
            ],
        ),
        (
            "Energy (Nominal) (kWh)",
            [
                "60",
                "60",
                "78",
                "78",
                "100",
                "100",
            ],
        ),
        (
            "Battery Used",
            [
                "CATL LFP60",
                "CATL LFP60",
                "LG M50 / Panasonic 2170",
                "LG M50 2170",
                "Panasonic 18650",
                "Panasonic 18650",
            ],
        ),
        (
            "Pack Weight (kg)",
            [
                "440",
                "440",
                "481",
                "481",
                "544",
                "536",
            ],
        ),
        (
            "Cell Weight (kg)",
            [
                "328.6",
                "328.6",
                "309.1",
                "309.1",
                "356.4",
                "356.4",
            ],
        ),
    ],
)

data_election2 = OrderedDict(
    [
        (
            "EV Manufacturer",
            [
                "Nissan",
                "Audi",
                "BMW",
                "Hyundai",
                "Kia",
                "GM",
                "Chevrolet",
                "Volkswagen",
                "Ford",
                "Rivian",
                "Tesla",
            ], 
        ),
        (
            "Model",
            [
                "Leaf", 
                "Q6 E-tron Quattro",
                "i3", 
                "Ioniq 5",
                "EV9",
                "Ultium(Cell)",
                "Bolt",
                "MEB (ID.4, ID.5, Buzz)",
                "Mach-E SR (2023)",
                "R1T/R1S Standard/Large",      
                "Model S Plaid"               
            ],
        ),
        (
            "Battery Module", 
            [
                "2s2p2u", 
                "15s1p",
                "12s1p",
                "6s2p",
                "4s3p",
                "24<sup>b</sup> cells",
                "8 x 10s3p + 2 x 8s3p",
                "8s3p",
                "",
                "12s72p",
                "22s72p",
            ]
        ),
        (
            "Capacity (Ah)",
            [
                "112.6",
                "152",
                "120",
                "111.2",
                "180.9",
                "103<sup>c</sup>",
                "~55/60<sup>f</sup>",
                "234",
                "302<sup>d</sup>",
                "360",
                "",
            ],
        ),
        (
            "Nominal Voltage (V)",
            [
                "14.6",
                "55",
                "45",
                "21.8",
                "14.5",
                "3.7<sup>c</sup>",
                "3.65<sup>f</sup>",
                "29.6",
                "3.2<sup>d</sup>",
                "43.56",
                "81.4",
            ],
        ),
        (
            "Modules per Pack",
            [
                "24",
                "12",
                "8",
                "32<sup>a</sup>",
                "38",
                "6-24",
                "",
                "12",
                "",
                "9",
                "5",
            ],
        ),
        (
            "Battery Supplier",
            [
                "Envision AESC (NCM523 Pouch)",
                "Samsung SDI (NCM811 Prismatic)",
                "Samsung SDI (NCM622 Prismatic)",
                "SK Innovation (NCM811 Pouch)",
                "SK On (NCM)",
                "Ultium Cells LLC (LG ES Joint) (NCMA Pouch) \n CATL (China, NCM Cylindrical)",
                "LG ES (Pouch Cell)",
                "LG ES (Europe) (NCM712 Pouch) \n SK On (North America) \n CATL, VWAC (China)",
                "CATL (LFP Prismatic)",
                "Samsung SDI (NCA Cylindrical)",
                "Panasonic (NCA Cylindrical)",
            ],
        ),
        (
            "Note",
            [
                "40 kWh",
                "100 kWh",
                "42 kWh",
                "<sup>a</sup>For 77.4 kWh pack",
                "99.8 kWh",
                "<sup>b</sup>Different configuration possible, <sup>c</sup>Cell Level",
                "Cell Level",
                "82 kWh",
                "<sup>d</sup>Cell Level \n 75 kWh",
                "2170 cell \n 141 kWh",
                "18650 cell \n 100 kWh",
            ],
        ),
        (
            "Source",
            [
                "[https://www.nissan-global.com/EN/INNOVATION/TECHNOLOGY/ARCHIVE/LI_ION_EV/](https://www.nissan-global.com/EN/INNOVATION/TECHNOLOGY/ARCHIVE/LI_ION_EV/) \n [https://pushevs.com/2018/01/29/2018-nissan-leaf-battery-real-specs/](https://pushevs.com/2018/01/29/2018-nissan-leaf-battery-real-specs/) \n [https://www.automotivemanufacturingsolutions.com/ev-battery-production/nissan-and-envision-aesc-to-build-new-ev-battery-plant-in-japan-reports/42168.article](https://www.automotivemanufacturingsolutions.com/ev-battery-production/nissan-and-envision-aesc-to-build-new-ev-battery-plant-in-japan-reports/42168.article)",
                "[https://www.audi-mediacenter.com/en/the-audi-q6-e-tron-electric-mobility-on-a-new-level-15929/battery-and-charging-15933](https://www.audi-mediacenter.com/en/the-audi-q6-e-tron-electric-mobility-on-a-new-level-15929/battery-and-charging-15933) \n [https://electrichasgoneaudi.net/models/q6-e-tron/drivetrain/battery](https://electrichasgoneaudi.net/models/q6-e-tron/drivetrain/battery)/",
                "[https://evshop.eu/en/batteries/298-bmwi3-42kwh-battery-pack.html](https://evshop.eu/en/batteries/298-bmwi3-42kwh-battery-pack.html) \n [https://www.secondlife-evbatteries.com/products/bmw-i3-120ah-42kwh-pack](https://www.secondlife-evbatteries.com/products/bmw-i3-120ah-42kwh-pack)",
                "[https://insideevs.com/news/539940/hyundai-ioniq5-battery-pack-opened/](https://insideevs.com/news/539940/hyundai-ioniq5-battery-pack-opened/) \n [https://openinverter.org/forum/viewtopic.php?t=4181](https://openinverter.org/forum/viewtopic.php?t=4181)",
                "[https://www.kia.com/content/dam/kwcms/kme/se/sv/assets/contents/utility/specifications/ev9/kia-ev9-keyfacts.pdf ](https://www.kia.com/content/dam/kwcms/kme/se/sv/assets/contents/utility/specifications/ev9/kia-ev9-keyfacts.pdf) \n [https://www.kiamedia.com/us/en/models/ev9/2024/specifications](https://www.kiamedia.com/us/en/models/ev9/2024/specifications)",
                "[https://en.wikipedia.org/wiki/Ultium](https://en.wikipedia.org/wiki/Ultium)",
                "[https://allev.info/2023/12/chevy-bolt-ev-battery-disassembly/](https://allev.info/2023/12/chevy-bolt-ev-battery-disassembly/)",
                "[https://www.evcreate.com/using-volkswagen-meb-battery-modules/](https://www.evcreate.com/using-volkswagen-meb-battery-modules/) \n [https://www.secondlife-evbatteries.com/products/vw-id-8s-battery-module-0z1915599h](https://www.secondlife-evbatteries.com/products/vw-id-8s-battery-module-0z1915599h)",
                "[https://www.macheforum.com/site/threads/new-mach-e-lfp-battery-specs-revealed.26099/](https://www.macheforum.com/site/threads/new-mach-e-lfp-battery-specs-revealed.26099/)",
                "[https://www.motortrend.com/reviews/2022-rivian-r1t-electric-pickup-truck-second-drive-review/](https://www.motortrend.com/reviews/2022-rivian-r1t-electric-pickup-truck-second-drive-review/) \n [https://insideevs.com/news/500474/rivian-samsung-sdi-battery-supplier/](https://insideevs.com/news/500474/rivian-samsung-sdi-battery-supplier/)",
                "[https://insideevs.com/news/540380/tesla-models-plaid-battery-open/](https://insideevs.com/news/540380/tesla-models-plaid-battery-open/) \n [https://insideevs.com/news/513181/samsungsdi-cylindrical-nca-cells-91nickel/](https://insideevs.com/news/513181/samsungsdi-cylindrical-nca-cells-91nickel/) \n [https://ev-database.org/car/1405/Tesla-Model-S-Plaid](https://ev-database.org/car/1405/Tesla-Model-S-Plaid)",
            ],
        ),
    ],
)

dt = pd.DataFrame(data_election)
dt2 = pd.DataFrame(data_election2)


layout = html.Div([
             dbc.Row([
                dbc.Col([   
                    dbc.Row([
                         dbc.Col([
                         dcc.Markdown('* Battery Module/Pack', style={'font-size':'25px', 'textAlign':'left','font-weight':'bold'}),
                         html.Div(('- A battery Module is a collection of cells connected in series or in parallel to achieve desired voltage and energy density.'), 
                                 style={'textAlign':'justify', 'margin-left':'20px', 'font-size':'18px'}),
                         html.Br(),
                         html.Div(('- A battery Pack is consisting of one or more modules (or cells) that are connected (likely in series if modules), assembled with the electrical interconnects and packaged into a single unit. Packs are usually located at the lower part compartment of the EV chassis for better design flexibility and uniform weight distribution.'), 
                                 style={'textAlign':'justify', 'margin-left':'20px', 'font-size':'18px'}),
                         html.Br(),
                         html.Div(('- The pack usually requires monitoring, sensing (i.e. voltage and temperature), and control through effective battery management system for protection, stability, and safety of the battery.'), 
                                 style={'textAlign':'justify', 'margin-left':'20px', 'font-size':'18px'}),
                         html.Br(),
                        ],
                        xs=8, sm=12, md=7, lg=5, xl=5,
                        ),
                        dbc.Col(
                            [
                            html.Div(html.Img(src='https://dl.dropboxusercontent.com/scl/fi/2dtyvf3krsc03q71zcvty/Cell_module_pack.png?rlkey=6b3vpgy3yy8zbzbat3jxutmxj&raw=1', style={"width":"70%", "display": "block", "margin": "auto"}), ),
                            html.Div(html.Img(src='https://dl.dropboxusercontent.com/scl/fi/tewug7stsy9urx8v8f7d9/e-tron-6-quattro.png?rlkey=f1dprdvgdwhdvz1brc1sbn09n&raw=1', style={"width":"70%", "display": "block", "margin": "auto"}), ),         
                            dcc.Markdown('Audi Q6 E-tron Battery Module & Pack \n\n Source: https://electrichasgoneaudi.net/models/q6-e-tron/drivetrain/battery/', style={"font-size":"18px", "display": "block", "margin": "auto"}),                        
                            ], width={"size": 7},
                            xs=6, sm=12, md=7, lg=7, xl=7,
                        ),
                    ],),
                    html.Br(),
                    html.Br(),
                    dmc.Divider(size="md", color="grey"),
                    html.Br(),
                    dbc.Row([
                         dbc.Col([
                         dcc.Markdown('* Cell Interconnect', style={'font-size':'25px', 'textAlign':'left','font-weight':'bold'}),
                         html.Div(('- Cells are connected electrically using the busbars (typically aluminum) via various joining technologies such as laser welding and ultrasonic wire bonding. Interconnect design can vary depending on the cell form factor. The schematics on the right show the single-sided interconnect of the cells.'), 
                                 style={'textAlign':'justify', 'margin-left':'20px', 'font-size':'18px'}),
                         html.Br(),
                         html.Div(('- Older Tesla Models 3/S/X use wire bonding while newer Model S Plaid and Model Y use laser welding possibly for robustness of the connection, away from the breaking of the fragile wires.'), 
                                 style={'textAlign':'justify', 'margin-left':'20px', 'font-size':'18px'}),
                         html.Br(),
                        ], width={"size": 5},
                        xs=5, sm=6, md=7, lg=5, xl=5,
                        ),
                        dbc.Col(
                            [
                            html.Div(html.Img(src='https://dl.dropboxusercontent.com/scl/fi/7rt7b2kc90oel23u7yeph/Cell-Interconnect.png?rlkey=7wds8k7mwvo4pscqi0g8585qf&st=ydcwny3b&raw=1', style={"width":"70%", "display": "block", "margin": "auto"}), ),
                            ], width={"size": 7},
                            xs=4, sm=7, md=7, lg=7, xl=7,
                        ),
                    ],),
                    html.Br(),
                    dmc.Divider(size="md", color="grey"),
                    html.Br(),                    
                    dcc.Markdown('* Tesla EV Model Specs', style={'font-size':'25px', 'textAlign':'left','font-weight':'bold'}),
                        dash_table.DataTable(
                                style_cell={'font-family': 'Arial', 'font-size': '18px', 'text-align':'left', 'minwidth':'15em', 'margin-top':'10px'}, 
                                style_table={'overflowX': 'auto'},
                                style_data={
                                        'whiteSpace': 'normal',
                                        'color': 'black',
                                        'backgroundColor': 'white',
                                        'height':'auto',
                                        'lineheight':'15px'
                                },
                                style_data_conditional=[
                                {
                                    'if': {'row_index': 'odd'},
                                    'backgroundColor': 'rgb(220, 220, 220)'
                                },
                                {
                                    'if': {'column_id': 'Model'},
                                    'fontWeight': 'bold', 'position':'sticky', 'left':'0px', 
                                },
                                ],
                                style_header={
                                    'backgroundColor': 'rgb(210, 210, 210)',
                                    'color': 'blue',
                                    'fontWeight': 'bold',
                                    'font-size': '20px'
                                },
                                data=dt.to_dict('records'),
                                columns=[{'id': c, 'name': c} for c in dt.columns],
                                
                        ),
                        html.Div(('Sources:'), 
                                style={'textAlign':'justify', 'font-size':'15px', 'font-style':'italic', 'margin-left':'0px'}),
                        dcc.Markdown(('https://ev-database.org/ \n https://vehiclefreak.com/how-much-does-a-tesla-car-battery-weigh-model-s-model-3-model-x-and-model-y/ \n https://cleantechnica.com/2019/01/28/tesla-model-3-battery-pack-cell-teardown-highlights-performance-improvements/ \n https://twitter.com/TroyTeslike/status/1285628571491471360 \n https://www.sciencedirect.com/science/article/pii/S2590116823000802?via%3Dihub#sec2'), 
                                style={'textAlign':'justify', 'font-size':'15px', 'font-style':'italic', 'margin-left':'0px'}),
                        html.Br(),
                        dmc.Divider(size="md", color="grey"),
                        html.Br(),
                        dcc.Markdown('* EV Battery Module Comparison', style={'font-size':'25px', 'textAlign':'left','font-weight':'bold'}),
                        #dbc.Row([
                        #    dbc.Col([
                        #        html.Div( html.Img(src='https://www.dropbox.com/scl/fi/m6yvuhqwi1hrpqvb1aqoh/VW_MEB.png?rlkey=xdf7yaovkgillk5vd93miixzq&raw=1', style={"width":"100%"}), 
                        #         ),
                        #        html.Div(('Source: Volkwagen of America, Inc'), 
                        #        style={'textAlign':'justify', 'font-size':'15px', 'font-style':'italic', 'margin-left':'0px'}),
                        #        html.Br(),
                        #        ], width={"size": 4},
                        #        xs=7, sm=7, md=7, lg=4, xl=5,
                        #        ),
                        #    dbc.Col([
                        #        html.Div( html.Img(src='https://www.dropbox.com/scl/fi/30546zlv1wl7t83uffry5/Hyundai-Ioniq5.png?rlkey=gnr1vkiw0rmz9bpumztnu0o47&raw=1', style={"width":"100%"}), 
                        #         ),
                        #       html.Div(('Source: https://www.motortrend.com/news/hyundai-first-dedicated-ev-platform-rwd-awd-details/'), 
                        #            style={'textAlign':'justify', 'font-size':'15px', 'font-style':'italic', 'margin-left':'0px'}),
                        #        html.Br(),
                        #        ], width={"size": 4},
                        #        xs=7, sm=7, md=7, lg=4, xl=5,
                        #    ),
                        #],),
                        dash_table.DataTable(
                                css=[{'selector': 'table', 'rule': 'table-layout: fixed'}],
                                style_cell={'font-family': 'Arial', 'font-size': '18px', 'text-align':'left', 'margin-top':'10px'}, 
                                markdown_options={"html": True},
                                style_table={'overflowX': 'auto'},
                                style_data={
                                        'whiteSpace': 'normal',
                                        'color': 'black',
                                        'width': 'auto',
                                        'overflow':'auto',
                                        'backgroundColor': 'white',
                                        'height':'auto',
                                        'lineheight':'15px',
                                },
                                style_data_conditional=[
                                {
                                    'if': {'row_index': 'odd'},
                                    'backgroundColor': 'rgb(220, 220, 220)'
                                },
                                {
                                    'if': {'column_id': 'Source'},
                                    'whiteSpace':'pre'
                                },
                                {'if': {'column_id': 'EV Manufacturer'},
                                    'fontWeight': 'bold', 'position':'sticky', 'left':'0px'
                                },
                                ],
                                style_header={
                                    'backgroundColor': 'rgb(210, 210, 210)',
                                    'color': 'blue',
                                    'fontWeight': 'bold',
                                    'whiteSpace': 'pre-wrap',
                                    'font-size': '20px'
                                },
                                data=dt2.to_dict('records'),
                                columns=[{'id': d, 'name': d, "presentation": "markdown"} for d in dt2.columns],     
                        ),
                        html.Br(),
                        dmc.Divider(size="md", color="grey"),
                        html.Br(),
                        dbc.Row([
                                dcc.Markdown('Battery Packaging Efficiency ', style={'font-size':'25px', 'textAlign':'left','font-weight':'bold'}),
                                html.Div(('- A geometric packing principle tells that the prismatic/pouch cells should yield packing efficiency of 90-95%, way higher than the cylindrical cell. However, it is noteworthy that the volumetric efficiency rate of the prismatic/pouch cells in actual EV batteries are lower and even comparable to those of cylindrical. According to the paper by Löbberding et al., after surveying 25 different BEVs (from 10 OEMs between 2010-2019), the average volume utilization rate is 0.353, which is only slightly higher than that of cylindrical (0.295). This discrepancy can be due to incorporation of auxiliary yet important parts such as interconnects, thermal management (i.e. cooling) system, BMS, and sensors. However, a caveat is that the average cell-to-module efficiency for prismatic/pouch cells is much higher than that of the cylindrical cell while the opposite is true for module-pack system efficiency comparison – making cell-to-system efficiencies all comparable after all. Hence, better space utilization has been sought after by many OEMs including BYD, CATL, and Tesla.'), 
                                    style={'textAlign':'justify', 'margin-left':'20px','font-size':'18px'}),
                        ], style={'margin-right':'20px', 'margin-bottom':'20px'}
                        ), 
                        html.Br(),
                        dbc.Row([
                            dbc.Col([
                                dcc.Markdown('* CMP, CTP, and CMB', style={'font-size':'25px', 'textAlign':'left','font-weight':'bold'}),
                                html.Div(('- In the traditional CMP (cell-module-pack) battery structure for the electric vehicle, module size varies among different electric vehicle manufacturers from Nissan’s 8-cell modules to Tesla’s 1584-cell modules. Increasing the module size has improved chassis space utilization to enhance battery capacity but the structure limits the space for other components, thus meeting the performance demand increasingly difficult.'), 
                                    style={'textAlign':'justify', 'margin-left':'20px', 'font-size':'18px'}),
                                html.Br(),
                                html.Div(('- CTP (cell-to-pack) technology improves the space utilization and energy density by skipping the modular arrangements of the cells. This direct integration proposed by CATL, according to their first-generation CTP, can increase space utilization by 15-20%, reduce the part numbers for a pack by 40%, and enhance energy density by 25-30% to 200 Wh/kg, when compared with CMP. Their third generation CTP has boosted volumetric utilization efficiency to 72% (from 55% in the first generation) and allowed energy density to reach 255 Wh/kg using Qilin NMC batteries.'), 
                                    style={'textAlign':'justify', 'margin-left':'20px', 'font-size':'18px'}),
                                html.Br(),
                                html.Div(('- Cell integration to the body (CTB) is the new technology proposed by BYD by launching LFP blade battery and increases volumetric energy density by up to 50% and space utilization by over 50% when compared to the CMP predecessor.'), 
                                    style={'textAlign':'justify', 'margin-left':'20px', 'font-size':'18px'}),
                            ], width={"size": 7},
                            xs=5, sm=8, md=6, lg=7, xl=7,
                            ),
                            dbc.Col([
                                html.Div( html.Img(src='https://dl.dropboxusercontent.com/scl/fi/hqzic08b0o2s5knuknxi6/CATLCTP.png?rlkey=pcevbldc123x6hlnlw0gnn6n1&raw=1', style={"width":"100%"}), 
                                 ),
                                html.Div(('Top- Source: CATL / https://www.catl.com/en/news/958.html'), 
                                    style={'textAlign':'justify', 'font-size':'15px', 'font-style':'italic', 'margin-left':'0px'}),
                                html.Div(('Bottom- Source: medium.com / https://medium.com/batterybits/the-next-generation-battery-pack-design-from-the-byd-blade-cell-to-module-free-battery-pack-2b507d4746d1'), 
                                    style={'textAlign':'justify', 'font-size':'15px', 'font-style':'italic', 'margin-left':'0px'}),
                                html.Br(),
                                ], width={"size": 5},
                            xs=4, sm=4, md=7, lg=7, xl=5,
                            ),
                        ],),
                        dcc.Markdown('- Reference', style={'font-size':'20px', 'textAlign':'left','font-weight':'bold'}),           
                        dcc.Markdown(('Hendrik Löbberding, et al.,"From Cell to Battery System in BEVs: Analysis of System Packing Efficiency and Cell Types", _**World Electric Vehicle Journal**_, 11, 77 (2020)'), 
                                style={'textAlign':'justify', 'font-size':'18px', 'margin-left':'30px'}),                                         
                ],
                ),
             ],style={'textAlign':'justify', 'margin-left':'30px', 'margin-right':'30px'},
             ),
             html.Div(id='Options-content'),
    ])
