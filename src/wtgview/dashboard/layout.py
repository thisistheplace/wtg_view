from dash import html
import dash_bootstrap_components as dbc

def layout(tabs):
    """Defines the overall layout of the dashboard.

    The layouts of individual panels are defined in subpackages.

    Args:
        tabs: objects defining tabs

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
                    [dbc.Tab(tab.layout, label=tab.name) for tab in tabs]
                )
            ),
        ],
        style={
            "padding": "30px",
            "height": "100%",
        },
    )