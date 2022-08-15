from dash import html
import dash_bootstrap_components as dbc

def layout():
    """Defines the layout of the page banner

    Returns:
        dash.html.Div
    """
    return html.Div(
        children=[
            # Heading data
            html.Div(
                children="Account"
            ),
        ],
        style={
            "padding": "30px",
            "height": "100%",
            "width": "100%"
        },
    )