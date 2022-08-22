from dash import html, dcc
import dash_bootstrap_components as dbc

def layout(charts):
    """Defines the layout of the input tab

    Args:
        charts: figures

    Returns:
        dash.html div
    """
    return html.Div(
        children=[
            dcc.Store(id='monitor-store', storage_type='session'),
            dbc.Container(
                dbc.Row([
                    dbc.Col(
                        dbc.Card(
                        dbc.Button("Start", id="start", color="success", className="me-1", style={"padding":"2vw", "paddingTop": "20px", "paddingBottom":"20px"}),
                            body=True,
                            style={"border":"none"}
                        ),
                        lg=2,
                        width=3,
                    ),
                    dbc.Col(
                        dbc.Card(
                            dbc.Button("Stop", id="stop", color="danger", className="me-1", style={"padding":"2vw", "paddingTop": "20px", "paddingBottom":"20px"}),
                            body=True,
                            style={"border":"none"}
                        ),
                        lg=2,
                        width=3
                    ),
                    dbc.Col(
                        dbc.Row(
                            dbc.Col(
                                dbc.Card(
                                    dbc.Button(
                                        [
                                            "Completed",
                                            dbc.Badge("0", id="monitor-badge", color="light", text_color="primary", className="ms-1"),
                                        ],
                                        color="primary",
                                        style={"padding":"10px"}
                                    ),
                                    body=True,
                                    style={"border":"None"}
                                ),
                                lg=4,
                                width=12
                            ),
                            justify="end",
                            # align="center"
                        ),
                        lg=8,
                        width=6,
                    )
                ],
                style={"width":"100%", "padding":"0px"},
                justify="end",
                align="center"
                ),
                style={
                    "padding":"0px",
                    "paddingBottom":"10px",
                    "paddingTop":"10px",
                    "width": "100%"
                }
            ),
            dcc.Interval(id="progress-interval", n_intervals=0, interval=500, max_intervals=0),
            dbc.Progress(id="progress"),
            dbc.Container(
                id="monitor-charts",
                children=[chart.layout for chart in charts],
                style={
                    "padding":"0px"
                }
            )
        ],
        style={
            "padding": "10px",
            "height": "100%",
            "width": "100%"
        },
    )

