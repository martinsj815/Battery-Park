import os
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import dash
import plotly.graph_objs as go
import plotly.express as px

app = dash.Dash(
    external_stylesheets=[dbc.themes.LUX], suppress_callback_exceptions=True
)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'check, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

