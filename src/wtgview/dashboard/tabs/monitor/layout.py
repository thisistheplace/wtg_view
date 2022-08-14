from dash import html
import dash_core_components as dcc
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
                dbc.Button("Start", id="start", color="success", className="me-1"),
                dbc.Button("Stop", id="stop", color="danger", className="me-1"),
            ]),
            dcc.Interval(id="progress-interval", n_intervals=0, interval=500),
            dbc.Progress(id="progress"),
        ],
        style={
            "padding": "30px",
            "height": "100%",
        },
    )

