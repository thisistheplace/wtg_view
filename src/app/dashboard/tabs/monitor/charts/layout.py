from turtle import heading
from dash import html, dcc
import dash_bootstrap_components as dbc

def layout(figure):
    """Defines the layout of a scatter chart

    Returns:
        dash.html div
    """
    return dcc.Graph(
        id="monitor-figure",
        figure=figure,
        style={
            "width":"100%",
            "height":"100%"
        }
    )

