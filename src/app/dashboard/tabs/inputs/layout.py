from dash import html, dcc

from dash_react_flowing import DashReactFlowing

def layout(data):
    """Defines the layout of the input tab

    Returns:
        dash.html div
    """
    return html.Div(
        children=[
            dcc.Store(id='workflow-store', storage_type='session', data=data),
            html.Div(
                "Describe your workflow:"
            ),
            html.Button("Add node", id='add-node', n_clicks=0, className="mb-3"),
            DashReactFlowing(
                id="workflow",
                nodes=data["nodes"],
                edges=data["edges"]
            )
        ],
        style={
            "padding": "30px",
            "height": "75vh",
        },
    )

