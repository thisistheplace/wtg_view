from dash import html, dcc
import dash_bootstrap_components as dbc

def layout():
    """Defines the layout of the input tab

    Returns:
        dash.html div
    """
    return html.Div(
        children=[
            # Heading data
            html.H1(children="Monitor tab"),
            html.Div(
                children="""
            UI for monitoring
            """
            ),
            dcc.Store(id='monitor-store', storage_type='session'),
            html.Div(children=[
                dbc.Button("Start", id="start", color="success", className="me-1", style={"padding": "20px"}),
                dbc.Button("Stop", id="stop", color="danger", className="me-1", style={"padding": "20px"}),
            ],
            style={"padding-bottom": "10px"}
            ),
            dcc.Interval(id="progress-interval", n_intervals=0, interval=500),
            dbc.Progress(id="progress"),
        ],
        style={
            "padding": "30px",
            "height": "100%",
        },
    )

