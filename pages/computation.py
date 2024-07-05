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
import math

dash.register_page(
    __name__, name="Computation", top_nav=True, path="/computation"
    )

layout = html.Div([
    dbc.Row([dcc.Markdown('Computational Modeling', style={'font-size':'25px', 'margin-bottom':"10px", 'textAlign':'justify','font-weight':'bold'}),
        html.Div(('Computational modeling plays a crucial role in materials research and design. Various computational modeling methods have been employed to uncover battery reaction mechanisms and derive intrinsic material parameters, which are then used to predict battery performance at the system level based on complex electrochemical transport equations.'), 
                       style={'textAlign':'justify', 'margin-left':'20px','font-size':'16px'}),
        html.Div(('Depending on the modeling approaches and scale, multiscale simulations, such as first-principles calculations, molecular dynamics simulations, phase field modeling, continuum simulations, and (electro-)thermal modeling, have been actively adopted to design batteries from the cell to the pack level.'),
                 style={'textAlign':'justify', 'margin-left':'20px','font-size':'16px','margin-bottom':"30px"}),
        dcc.Markdown('* First-principles calculations:', style={'font-size':'20px', 'margin-bottom':"5px", 'textAlign':'justify','font-weight':'bold'}),
        html.Div(('- First-principles calculations involve atomic-level simulations used to predict the properties of previously unknown materials by solving the many-body time-indepedent Schr\u00F6dinger equation through various numerical approximations, such as the Hartree-Fock (HF) method, Density Functional Theory (DFT), and hybrid approaches. These calculations provide inherent material properties, including atomic coordinates and electronic structure properties, without requiring any input from experiments, thereby aiding in the interpretation of experimental observations.'),
                 style={'textAlign':'justify', 'margin-left':'20px','font-size':'16px'}),
        html.Div(('This computational approach offers key properties of lithium-ion batteries, such as the calculation of equilibrium voltages and voltage profiles, theoretical capacity, ionic mobilities, structural stability and corresponding volume changes, as well as thermal and electrochemical stabilities. This understanding provides significant insights into the intrinsic properties of batteries and aids in optimizing battery materials.'),
                 style={'textAlign':'justify', 'margin-left':'20px','font-size':'16px','margin-bottom':"30px"}),
    ], style={'textAlign':'justify', 'margin-left':'40px', 'margin-right':'60px'},),
])