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
                meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1'}]
                )
app.config.suppress_callback_exceptions = True
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True


app.title = "Cell Design"

server = app.server

masthead_content = dbc.Col(
    html.Img(src='https://dl.dropboxusercontent.com/scl/fi/7utukx4f0a1b651d023nw/Masthead_new3.png?rlkey=1gkyhyagdugod601ytmx4i4g3&raw=1', style={"width":"250px"}), 
    width={"size": 8}
)

navbar_children=[
    dbc.NavItem(dbc.NavLink("Home", href="" or "/", id="home-link", className="navbar-link", style={'font-size':'20px', 'font-weight':'bold', 'margin-right':'40px'})),    
    dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Cells", href="/basics-c", className="drop-down"),
                dbc.DropdownMenuItem("Chemistry", href="/chemistry", className="drop-down"),
                dbc.DropdownMenuItem("Parameter & Metrics", href="/basics-pm", className="drop-down"),
                dbc.DropdownMenuItem("Stack Designs", href="/basics-sd", className="drop-down"),
            ],
            nav=True,
            in_navbar=True,
            label=html.Span("Basics", style={"font-size":'20px', 'font-weight':'bold'}),
            id="basic-link",
            className='dropdown',
            style={'margin-right':'40px', 'display':'block'},
    ),
    dbc.NavItem(dbc.NavLink("Modeling", href="/calculator", className="navbar-link", style={'font-size':'20px', 'margin-right':'40px', 'font-weight':'bold'})),
    dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Academic-to-Industry", href="/academic-to-industry", className="drop-down"),
                dbc.DropdownMenuItem("Cell Manufacturing", href="/cell-manufacturing", className="drop-down"),
                dbc.DropdownMenuItem("Battery Packs", href="/battery-p", className="drop-down"),
            ],
            nav=True,
            in_navbar=True,
            label=html.Span("Industry", style={"font-size":'20px', 'font-weight':'bold'}),
            menu_variant=('dark'),
            style={'margin-right':'40px', 'display':'block'},
    ),    
]
container_style = {
    "display": "block", 
    "justifyContent": "center", 
    "alignItems": "left", 
    "height":"160px",
    "background-image": "linear-gradient(to bottom, rgb(234, 228, 228), rgb(78, 81, 244))",
    "width":"auto",
    #"background-color":"rgb(201,76,76)",
    
}  

#navbar_toggler = dbc.NavbarToggler(id="navbar-toggler")

navbar = dbc.NavbarSimple(
            navbar_children,
            color="light",
            dark=False,
            expand="md",
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


