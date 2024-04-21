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


layout = html.Div([
    dcc.Markdown('This pages for giving simple numeric estmiation of cell performance.'),
    dcc.Tabs(id="Cells", value='tab-cs', children=[
        dcc.Tab(label='Single Cell', value="tab-lip", style=tabs_styles, selected_style=tab_selected_style, children=[
                dbc.Row([
                    dcc.Markdown('* Estimation of Cycle Life', style={'marginTop':'40px','font-size':'25px','textAlign':'left','font-weight':'bold'}),
                    dcc.Markdown(" This is for estimating cycle life when cells cycle with a specific columbic efficiency each cycles."),
                    dbc.Col([
                        dbc.Row([
                            html.Div([html.P('Coulombic Efficiency (%)', style={"height":"auto","margin-bottom":"auto"}),
                                      dcc.Input(id="input-d2", type="number",value="99", step="0.01", style={"margin-bottom":"1em"})]),
                            html.Div([html.P('Capacity Retention (%)', style={"height":"auto","margin-bottom":"auto"}),
                                      dcc.Input(id="input-d1", type="number", value="80", step="0.1", style={"margin-bottom":"1em"})]),
                            html.Span(id='outcome15', style={"font-size":"150%", "color":"red"}),
                        ],
                        style={"margin-left":"10px","margin-top":"50px"},
                        ),
                    ],
                    width={"size":"6"},
                    xs=12,sm=12, md=10, lg=6, xl=6,
                    ),
                    dbc.Col([
                        dbc.Row([
                            dcc.Graph(id='plot10', style={"width":"120vh", "height":"50vh","margin-top":"0px"})
                        ])
                        ], width={"size":"6"}, xs=12, sm=12, md=10, lg=6, xl=6,
                    ),
                ])
        ]),

        dcc.Tab(label="Stacked Cell", value='tab-sc', style=tabs_styles,selected_style=tab_selected_style, children=[
            dbc.Row([
                dcc.Markdown('* Stacked Cell Design')
            ])
        ]),         
        dcc.Tab(label="Jelly-Roll Cell", value='tab-j', style=tabs_styles,selected_style=tab_selected_style, children=[
            dbc.Row([
                dcc.Markdown('* Jelly-Roll Cell Design')
            ])
        ]),
    ]),
    html.Div(id='options-content'),
])


@callback([Output('outcome15','children'), Output('plot10','figure')],
                [
                Input('tab-lip', 'value'),
                Input('input-d1', 'value'),
                Input('input-d2','value'),  
                ], 
            )

def update_content(tab_lip, input_d1, input_d2):
    if tab_lip and input_d1 and input_d2:    
        outcome15 = np.log10(float(input_d1)/100)/np.log10(float(input_d2)/100)
        #outcome2 = np.exp(float(input_h)*np.log10(float(input_f)/100))*100
        x10=np.arange(98,100,0.05)
        y10=np.log10(float(input_d1)/100)/np.log10(x10/100)
        #y3=np.exp(float(input_h)*np.log10(x2/100))*100
        #z=np.polyfit(x,y,1)
        #f=np.poly1d(z)
        #x_new=np.linspace(0,10,500)
        #y_new=f(x_new)
        trace6 = go.Scatter(x=x10, y=y10, name='data6', mode='lines')
        data6=[trace6]
        fig10 = go.Figure(data=data6)
        fig10.update_layout(
            plot_bgcolor='rgb(234, 228, 228)',
            paper_bgcolor='rgb(211, 211, 211)',
            title="Coulombic Efficiency vs Cycle Number",
            title_x=0.5,
            xaxis_title="Coulombic Efficiency (%)",
            yaxis_title="Cycle Numbers",
            font=dict(
                family="arial, monospace",
                size=16,
                color="black"
            )
        )
        fig10.update_xaxes(
            mirror=False,
            ticks='outside',
            showline=True,
            linecolor='black',
            gridcolor='lightgrey'
        )
        fig10.update_yaxes(
            mirror=True,
            ticks='outside',
            showline=True,
            linecolor='black',
            gridcolor='lightgrey'
        )


        return (
                "The cell is expected to undergo **{}** cycles".format(round(outcome15,2)), 
                fig10
                )
    else:
        return (
                "",
                {}
        )