from dash import html, dcc

def layout(figure):
    """Defines the layout of a scatter chart

    Returns:
        dash.html div
    """
    return html.Div(
        children=[
            dcc.Graph(
                id="monitor-figure",
                figure=figure
            )
        ],
        style={
            "padding": "30px",
            "height": "100%",
            "width": "100%"
        },
    )

