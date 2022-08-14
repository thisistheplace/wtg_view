from dash import html
import dash_bootstrap_components as dbc

from .tabs import banner, sidecol

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
            banner.Banner().layout,
            html.Div(
                children=[
                    dbc.Row([
                        dbc.Col(sidecol.Sidecol().layout, width=3),
                        dbc.Col(
                            # tabs
                            html.Div(
                                dbc.Tabs(
                                    [dbc.Tab(tab.layout, label=tab.name) for tab in tabs]
                                )
                            ), width=9
                        )
                    ])
                ]
            )
        ],
        style={
            "padding": "30px",
            "height": "100%",
        },
    )