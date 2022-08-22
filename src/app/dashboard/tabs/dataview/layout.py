from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd

from .charts.base import BaseChart

def layout(id:str, charts:BaseChart, data:pd.DataFrame):
    """Defines the layout of the dataview tab

    Args:
        id: id to give data store
        charts: list of BaseChart objects

    Returns:
        dash.html div
    """
    return dbc.Container(
        children=[
            dcc.Store(id=id, storage_type='session', data=data.to_dict()),
            dbc.Row([
                dbc.Col(
                    [
                        # html.Div([
                            dbc.Switch(
                                id="select-scatter",
                                label="Scatter",
                                value=False,
                            ),
                            dbc.Switch(
                                id="select-pie",
                                label="Pie",
                                value=False,
                            ),
                            dbc.Switch(
                                id="select-bar",
                                label="Histogram",
                                value=False,
                            ),
                            # ],
                        #     style={"paddingTop":"20px", "paddingBottom":"20px"}
                        # ),
                        dbc.DropdownMenu(
                            [],
                            label="Select data",
                            style={"paddingTop":"20px", "paddingBottom":"20px"}
                        )
                    ],
                    lg=2,
                    sm=12

                ),
                dbc.Col(
                    dbc.Row(
                        [
                            dbc.Col(
                                chart.layout,
                                id={
                                    'type': "dataview-chart-column",
                                    'index': idx
                                },
                                lg=4,
                                sm=12
                            ) for idx, chart in enumerate(charts)
                        ],
                    ),
                    lg=10,
                    sm=12
                )
            ]),     
        ],
        style={
            "padding": "30px",
            "height": "100%",
        },
    )

