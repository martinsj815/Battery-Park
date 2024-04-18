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
    __name__, name="Modeling", top_nav=True, path="/modeling-cells"
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
        dcc.Tab(label='A Single Cell', value="tab-lip", style=tabs_styles, selected_style=tab_selected_style, children=[
            dbc.Row([
                dbc.Row([
                    dcc.Markdown('* Estimation of Cycle Life', style={'marginTop':'40px','font-size':'25px','textAlign':'left','font-weight':'bold'}),
                    dcc.Markdown(" This is for estimating cycle life when cells cycle with a specific columbic efficiency each cycles."),
                    dbc.Col([
                        dbc.Row([
                            html.Div([html.P('Coulombic Efficiency (%)', style={"height":"auto","margin-bottom":"auto"}),
                                      dcc.Input(id="input_zz", type="number",value="99", step="0.01", style={"margin-bottom":"1em"})]),
                            html.Div([html.P('Capacity Retention (%)', style={"height":"auto","margin-bottom":"auto"}),
                                      dcc.Input(id="input_g", type="number", value="80", step="0.1", style={"margin-bottom":"1em"})]),
                            html.Span(id='outcome2', style={"font-size":"150%", "color":"red"}),
                        ],
                        style={"margin-left":"10px","margin-top":"50px"},
                        ),
                    ],
                    width={"size":"6"},
                    xs=12,sm=12, md=10, lg=6, xl=6,
                    ),
                dbc.Col([
                    #dcc.Loading(
                    #    id='loading', type='graph', children=[html.Div(id='cyclelife')]
                    #)
                    dbc.Row([
                        dcc.Graph(id='plot', style={"width":"120vh", "height":"50vh","margin-top":"0px"})
                    ])
                ], width={"size":"6"}, xs=12, sm=12, md=10, lg=6, xl=6,),
                ])
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
    html.Div(id='tabs-content'),
])


@callback([Output('plot','figure'), Output('outcome2','children')],
                [#Input('input-f', 'value'),
                Input('input_g', 'value'),
                #Input('input-h', 'value'),
                Input('input_zz','value'),  
                ], 
            )

def update_figure(input_g, input_zz):
    if input_g is not None and input_zz is not None:
        
        fig=go.Figure()
        outcome = np.log10(float(input_g)/100)/np.log10(float(input_zz)/100)
        #outcome2 = np.exp(float(input_h)*np.log10(float(input_f)/100))*100
        x2=np.arange(98,100,0.05)
        y2=np.log10(float(input_g)/100)/np.log10(x2/100)
        #y3=np.exp(float(input_h)*np.log10(x2/100))*100
        #z=np.polyfit(x,y,1)
        #f=np.poly1d(z)
        #x_new=np.linspace(0,10,500)
        #y_new=f(x_new)
        fig.add_trace(go.Scatter(x=x2, y=y2, name='cyclelife', mode='lines'))
        #trace3 = go.Scatter(x=x2, y=y3, name='data3', mode='lines')
    
        #data3=[trace3]
        
        #fig3 = go.Figure(data=data3)
        fig.update_layout(
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
        fig.update_xaxes(
            mirror=False,
            ticks='outside',
            showline=True,
            linecolor='black',
            gridcolor='lightgrey'
        )
        fig.update_yaxes(
            mirror=True,
            ticks='outside',
            showline=True,
            linecolor='black',
            gridcolor='lightgrey'
        )
        #fig3.update_layout(
        #    plot_bgcolor='rgb(234, 228, 228)',
        #    paper_bgcolor='rgb(211, 211, 211)',
        #    title="Coulombic Efficiency vs Capacity Retention",
        #    title_x=0.5,
        #    xaxis_title="Coulombic Efficiency (%)",
        #    yaxis_title="Capacity Retention (%)",
        #    font=dict(
        #        family="arial, monospace",
        #        size=16,
        #        color="black"
        #    )
        #)
        #fig3.update_xaxes(
        #    mirror=False,
        #    ticks='outside',
        #    showline=True,
        #    linecolor='black',
        #    gridcolor='lightgrey'
        #)
        #fig3.update_yaxes(
        #    mirror=True,
        #    ticks='outside',
        #    showline=True,
        #    linecolor='black',
        #    gridcolor='lightgrey'
        #)


        return dcc.Markdown("The cell is expected to undergo **{}** cycles".format(round(outcome,2)), dangerously_allow_html=True), fig
    else:
        return "",{}