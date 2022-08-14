from dash import html
import dash_bootstrap_components as dbc

def layout():
    """Defines the layout of the page banner

    Returns:
        dash.html.Div
    """
    return html.Div(
        children=[
            dbc.Row(
                [
                    dbc.Col(
                        dbc.Button(
                            html.I(className="fa fa-bars"),
                            id="sidebar-button",
                            className="mb-3",
                            n_clicks=0,
                            style={"zindex": "10", "position":"absolute", "display":"block"}
                        ),
                        style={"padding":"10px"}
                    ),
                    dbc.Col(
                        children=[
                            # Heading data
                            html.H1(children="WTG Flow", style={"paddingBottom": "10px"}),
                            html.Div(
                                children="""
                            workflow for offshore wind turbine simulation
                            """
                            ),
                        ],
                        width=9,
                        style={"textAlign": "right"}
                    )
                ]
            )
        ],
        style={
            "padding": "30px",
            "paddingLeft":"0px",
            "paddingTop":"15px",
            "height": "100%",
            "width": "100%"
        },
    )