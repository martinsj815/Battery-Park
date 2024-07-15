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
import pymatgen.core as pmg
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer 

si = pmg.Element("Si")
print(si.atomic_mass)
print(si.melting_point)
