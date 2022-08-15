from dash import html
import dash_bootstrap_components as dbc

def layout():
    """Defines the layout of the dataview tab

    Returns:
        dash.html div
    """
    return html.Div(
        children=[
            dbc.Row([
                dbc.Col(
                    [
                        dbc.Checklist(
                            id="select-chart-types",
                            options=[
                                {"label": "Scatter", "value": 1},
                                {"label": "Pie", "value": 2},
                                {"label": "Histogram", "value": 3},
                            ],
                            labelCheckedClassName="text-success",
                            inputCheckedClassName="border border-success bg-success",
                            style={"paddingTop":"20px", "paddingBottom":"20px"}
                        ),
                        dbc.DropdownMenu(
                            [],
                            label="Select data",
                            style={"paddingTop":"20px", "paddingBottom":"20px"}
                        )
                    ],
                    width = 3
                ),
                dbc.Col(
                    [
                        # selected charts go here
                    ],
                    width=9
                )
            ]),
        ],
        style={
            "padding": "30px",
            "height": "100%",
        },
    )

