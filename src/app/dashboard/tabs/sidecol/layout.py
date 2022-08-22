from dash import html
import dash_bootstrap_components as dbc

def layout():
    """Defines the layout of the page banner

    Returns:
        dash.html.Div
    """
    return dbc.Container(
        [
            html.Div(
                dbc.Button(
                    html.I(className="fa-solid fa-xmark"),
                    id="sidebar-close",
                    className="mb-3",
                    n_clicks=0,
                    style={"zindex": "10"}
                ),
                style={"position":"absolute", "display":"block", "top":"0px", "right":"0px", "padding":"20px"}
            ),
            # Heading data
            html.Div(
                "In progress...",
                style={"padding": "30px"}
            ),
        ],
        style={
            "height": "100%",
            "width": "100%",
            "maxWidth":"100%"
        },
    )