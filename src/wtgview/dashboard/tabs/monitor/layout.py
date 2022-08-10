from dash import html

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
        ],
        style={
            "padding": "30px",
            "height": "100%",
        },
    )

