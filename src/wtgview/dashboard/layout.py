""" Defines dashboard layout """
# imports
from abc import ABC
from dash import html, dcc
import pandas as pd

from panels

# functions
def dashboard_layout(app, db):
    """Applies the dashboard layout to the app.

    The layouts of individual panels are defined in subpackages.

    Args:
        app (Dash app): the app to setup
        db: (DataStore): object providing database access
    """
    # build dataframe from data
    if "device" in db:
        device_data = db["device"]
    else:
        device_data = pd.DataFrame()

    # create figure
    device_fig = update_figure(device_data ,"device")

    # format figure
    device_fig.update_layout(template="plotly_white")
    
    # build dataframe from data
    if "zone" in db:
        zone_data = db["zone"]
    else:
        zone_data = pd.DataFrame()

    # create figure
    zone_fig = update_figure(zone_data, "zone")

    # format figure
    device_fig.update_layout(template="plotly_white")

    # add everything to the app
    app.layout = html.Div(
        children=[
            # Error messaging box
            dcc.ConfirmDialog(
                id="figure-error",
                message="",
            ),

            # filesystem monitoring
            dcc.Interval(
                id="monitor-filesystem",
                interval=POLL_RATE * 1000,  # in milliseconds
                n_intervals=0,
            ),

            # Heading data
            html.H1(children="Heat Pump Dashboard"),
            html.Div(
                children="""
            visualize live heat pump data
            """
            ),

            # Holder for figures
            html.Div(
                children=[
                    dcc.Graph(id="device-figure", figure=device_fig),
                    dcc.Graph(id="zone-figure", figure=zone_fig),
                ],
                style={
                    "height": "50%",
                    "width": "90%",
                    "padding": "20px",
                },
            ),
        ],
        style={
            "padding": "30px",
            "height": "100%",
        },
    )
