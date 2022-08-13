from dash import html
import dash_bootstrap_components as dbc

from .tabs import inputs, monitor, outputs

def layout():
    """Defines the overall layout of the dashboard.

    The layouts of individual panels are defined in subpackages.

    Returns:
        dash.html.Div
    """
    return html.Div(
        children=[
            # Heading data
            html.H1(children="WTG Flow"),
            html.Div(
                children="""
            workflow for offshore wind turbine simulation
            """
            ),

            # Holder for figures
            html.Div(
                dbc.Tabs(
                [
                    dbc.Tab(inputs.layout(), label="inputs"),
                    dbc.Tab(monitor.layout(), label="monitor"),
                    dbc.Tab(outputs.layout(), label="outputs"),
                ]
                )
            ),
        ],
        style={
            "padding": "30px",
            "height": "100%",
        },
    )