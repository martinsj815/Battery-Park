import os
import dash
from dash import Dash, html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
from dash_bootstrap_components._components.Container import Container
import dash_mantine_components as dmc


# Initialize the app
app_name = os.getenv("APP_NAME", "Beyond-Cell")

app = dash.Dash(__name__, 
                external_stylesheets=[dbc.themes.SANDSTONE, 'https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css'], 
                suppress_callback_exceptions=True,
                use_pages=True,
                meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1, maximum-scale=1.2'}],
                )
app.config.suppress_callback_exceptions = True
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True


app.title = "Cell Design"

server = app.server

masthead_content = dbc.Row([
    dbc.Col([
        html.Img(src='https://dl.dropboxusercontent.com/scl/fi/7utukx4f0a1b651d023nw/Masthead_new3.png?rlkey=1gkyhyagdugod601ytmx4i4g3&raw=1', 
             style={"margin-top":"10px", "width":"250px"})
    ]),
    dbc.Col([
        html.Div("Battery chemistry and technology", style={"font-size":"24px", "font-style":"italic", "font-variant":"small-caps", "font-weight":"bold", "white-space":"normal", "color":"rgb(240,220,200)", "position":"sticky", "top":"100px"})
    ], style={"text-align":"right"}
    ),
    ])

navbar_children=[
    dbc.NavItem(dbc.NavLink("Home", href="" or "/", id="home-link", className="drop-down", style={'font-size':'20px', 'font-weight':'bold', 'margin-right':'40px'})),    
    dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Cells", href="/basics-c", className="drop-down"),
                dbc.DropdownMenuItem("Primary vs Secondary", href="/basics-prse", className="drop-down"),
                dbc.DropdownMenuItem("Li Chemistry", href="/chemistry", className="drop-down"),
                dbc.DropdownMenuItem("Parameter & Metrics", href="/basics-pm", className="drop-down"),
            ],
            nav=True,
            in_navbar=True,
            label=html.Span("Basics", style={"font-size":'20px', 'font-weight':'bold'}),
            id="basic-link",
            className='drop-down',
            style={'margin-right':'40px', 'display':'block'},
    ),
    dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Introduction", href="/basics-sd", className="drop-down"),
                dbc.DropdownMenuItem("Calculator", href="/modeling-cells", className="drop-down"),
                #dbc.DropdownMenuItem("Pack", href="/modeling-pack", className="drop-down"),
            ],
            nav=True,
            in_navbar=True,
            label=html.Span("Cell Design", style={"font-size":'20px', 'font-weight':'bold'}),
            id="modeling-link",
            className='drop-down',
            style={'margin-right':'40px', 'display':'block'},
    ),
    dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Characterization", href="/characterization", className="drop-down"),
                dbc.DropdownMenuItem("Computation", href="/computation", className="drop-down"),
            ],
            nav=True,
            in_navbar=True,
            label=html.Span("Methologies", style={"font-size":'20px', 'font-weight':'bold'}),
            id="methology-link",
            className='drop-down',
            style={'margin-right':'40px', 'display':'block'},
    ),  
    dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Academic-to-Industry", href="/academic-to-industry", className="drop-down"),
                dbc.DropdownMenuItem("Cell Manufacturing", href="/cell-manufacturing", className="drop-down"),
                dbc.DropdownMenuItem("Battery Packs", href="/battery-p", className="drop-down"),
            ],
            nav=True,
            in_navbar=True,
            label=html.Span("Industry", style={"font-size":'20px', 'font-weight':'bold'}),
            #menu_variant=('dark'),
            className='drop-down',
            style={'margin-right':'40px', 'display':'block'},
    ),    
]
container_style = {
    "display": "block", 
    "justifyContent": "center", 
    "alignItems": "left", 
    "height":"160px",
    #"background-image": "linear-gradient(to bottom, rgb(234, 228, 228), rgb(78, 81, 244))",
    "width":"inherit",
    "background-color":"rgb(70,70,70)",
    
}  

#navbar_toggler = dbc.NavbarToggler(id="navbar-toggler")

navbar = dbc.NavbarSimple(
            navbar_children,
            color="light",
            dark=False,
            expand="lg",
            sticky="top", 
            style={"padding":"15px"},
            links_left=True,
            
        )
       # dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
       #         dbc.Collapse(
       #         id="navbar-collapse",
       #         is_open=False,
       #         navbar=True,
       #         ),
       # ], fluid=True,
#)
page_content = html.Div(id='page-content')


app.layout = html.Div([ 
            #html.Link(rel='stylesheet', href='/assets/background.css'),
            #html.Link(rel='stylesheet', href='/assets/hover.css'),
            #html.Link(rel='stylesheet', href='/assets/header.css'),
            dbc.Container([
                    html.Div([
                    dbc.Row([
                        masthead_content,
                        navbar
                    ], 
                    style=container_style
                    ),
                    #navbar,
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    page_content,
                    dash.page_container,
                    ],
                ),
            ], 
            fluid=False,
            )
])
#@app.callback(
#    Output("navbar-collapse", "is_open"),
#    [Input("navbar-toggler", "n_clicks")],
#    [State("navbar-collapse", "is_open")],
#)
#def toggle_navbar_collapse(n, is_open):
#    if n:
#        return not is_open
#    return is_open

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8050)


