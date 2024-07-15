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
        dcc.Markdown('* Molecular dynamics simulations:', style={'font-size':'20px', 'margin-bottom':"5px", 'textAlign':'justify','font-weight':'bold'}),
        html.Div(("- Molecular dynamics (MD) simulations are computational techniques used to study the physical movements of atoms and molecules by solving Newton's equations of motion for a system of interacting particles. Depending on how the system's state is described, MD simulations can be classified into several types: 1) Classical Molecular Dynamics (CMD): Utilizes Newtonian mechanics to model the interactions and movements of particles in the system. 2) Reactive Molecular Dynamics (ReaxFF MD): Employs reactive force fields to simulate chemical reactions by allowing bonds to form and break dynamically. 3) ab-initio Molecular Dynamics (AIMD): Combines quantum mechanics, specifically solving the Schr\u00F6dinger equation, with classical MD to capture electronic structure effects. 4) Coarse-Grained Molecular Dynamics (CGMD): Simplifies the system by grouping atoms into larger particles, reducing the degrees of freedom and computational cost."),
                 style={'textAlign':'justify', 'margin-left':'20px','font-size':'16px'}),
        html.Div(('This computational approach plays an increasingly important role in exploring electrolyte structures, physicochemical properties such as ionic conductivity, and interfacial reaction mechanisms.'),
                 style={'textAlign':'justify', 'margin-left':'20px','font-size':'16px','margin-bottom':"30px"}),
        dcc.Markdown('* Phase field modeling:', style={'font-size':'20px', 'margin-bottom':"5px", 'textAlign':'justify','font-weight':'bold'}),
        html.Div(("- Phase-field modeling is a technique used to predict microstructure eveolution based on fundamental thermodynamic and kinetic principles, utilizing the structures and properties of individual features within a microstructure as input. By solving a set of Nernst-Planck equations or mass (or ion) transport equations and applying appropriate boundary conditions to simplify the equations but effectively describe phenomena, this modeling captures key features, such as the effects of microstructural features and defects on lithiation degradation and the kinetics of morphological and microstructural evolution during localized attacks at the mesoscale."),
                 style={'textAlign':'justify', 'margin-left':'20px','font-size':'16px'}),
        html.Div(('This method is particularly useful for understanding and predicting the morphology, phase changes, and transformations of materials, especially in the context of complex degradation processes in metallic materials used in engineering applications.'),
                 style={'textAlign':'justify', 'margin-left':'20px','font-size':'16px','margin-bottom':"30px"}),
        dcc.Markdown('* Continuum simulations:', style={'font-size':'20px', 'margin-bottom':"5px", 'textAlign':'justify','font-weight':'bold'}),
        html.Div(("-Continuum mechanics considers the different components of a battery as continuous media. By coupling multiple versions of a continuum model, it can describe the joint behavior of multiple cells or pack-level simulations. This approach can handle larger length and time scales."),
                 style={'textAlign':'justify', 'margin-left':'20px','font-size':'16px'}),
        html.Div(("Depending on the numerical approach, continuum battery models generally fall into two categories: empirical and physics-based. Physics-based continuum models, also known as electrochemical battery models, describe the physical phenomena underpinning battery behavior. These models provide insights into the behavior of lithium-ion distribution in the electrolyte, the multiple internal variables depicted, the potential and current distributions in both the porous electrodes and the electrolyte, the lithium-ion concentration within the electrolyte, and the distribution of intercalated lithium within the electrode particles."),
                 style={'textAlign':'justify', 'margin-left':'20px','font-size':'16px'}),
        html.Div(('Due to their fast and accurate predictions of real batteries, these approaches have been used as design tools to facilitate the development of new electrode, cell, and pack architectures and to estimate their potential performance. Based on this modeling, these approaches are used for optimizing operating conditions and battery management systems for thermal management, state of charge (SOC), and state of health (SOH) estimation.'),
                 style={'textAlign':'justify', 'margin-left':'20px','font-size':'16px','margin-bottom':"30px"}),
   
    ], style={'textAlign':'justify', 'margin-left':'40px', 'margin-right':'60px'},),

        html.Br(), 
        html.Br(),               
        dmc.Divider(size="md", variant="dotted", color="grey"),       
        html.Br(), 
        dbc.Row([
            dcc.Markdown('* References', style={'font-size':'25px', 'margin-bottom':"10px", 'textAlign':'justify','font-weight':'bold'}),
            dcc.Markdown(('- Sholl, David S., and Janice A. Steckel., "Density Functional Theory, A practical Introduction", _**Wiley**_,(2009)'), dangerously_allow_html=True,
                    style={'textAlign':'justify', 'margin-left':'30px', 'font-size':'16px'}),  
            dcc.Markdown(('- Alexander Urban, et. al., "Computational understanding of Li-ion batteries", _**Reviews in npj Computational Materials**_, 16002, (2016)'), dangerously_allow_html=True,
                    style={'textAlign':'justify', 'margin-left':'30px', 'font-size':'16px'}), 
            dcc.Markdown(('- Yawen Sun, et. al., "Boosting the Optimization of Lithium Metal Batteries by Molecular Dynamics Simulations:A Perspective", _**Reviews in Advanced Energy Materials**_, 2002373, (2020)'), dangerously_allow_html=True,
                    style={'textAlign':'justify', 'margin-left':'30px', 'font-size':'16px'}),
            dcc.Markdown(('- Talha Qasim Ansari, et. al., "Phase field modeling for the morphological and microstructural evoltuion of metallic materials under environmnental attack", _**Reviews in npj Computational Materials**_, 143, (2021)'), dangerously_allow_html=True,
                    style={'textAlign':'justify', 'margin-left':'30px', 'font-size':'16px'}),  
            dcc.Markdown(('- F Brosa Planella, et. al., "A continuum of physics-based lithium-ion battery models reviewed", _**Reviews in Progress in Energy**_, 4, (2022)'), dangerously_allow_html=True,
                    style={'textAlign':'justify', 'margin-left':'30px', 'font-size':'16px'}),            
                            
                ], style={'textAlign':'justify', 'margin-left':'40px', 'margin-right':'60px'},
             ), 
])