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
            html.Div(children=[
                dbc.Button("Start", id="start", color="success", className="me-1", style={"padding": "20px"}),
                dbc.Button("Stop", id="stop", color="danger", className="me-1", style={"padding": "20px"}),
                dbc.Button(
                    [
                        "Completed",
                        dbc.Badge("0", id="monitor-badge", color="light", text_color="primary", className="ms-1"),
                    ],
                    color="primary",
                    style={"float":"right", "padding":"20px"}
                ),
            ],
            style={"paddingBottom": "10px", "width": "100%"}
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

