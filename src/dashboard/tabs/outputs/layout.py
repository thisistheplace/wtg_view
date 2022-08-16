from dash import html, dcc
import dash_bootstrap_components as dbc

from dash_wtgviewer import DashWtgviewer
# import sys
# sys.path.append("/Users/bencannell/Documents/dev/dash_wtgviewer")
# from dash_wtgviewer import DashWtgviewer

from .model import viewer

def layout():
    """Defines the layout of the input tab

    Returns:
        dash.html div
    """
    # load model data
    viewer_data = viewer(
        {
            "nodes": {
                "1": {
                    "X": 0.0,
                    "Y": 0.0,
                    "Z": 0.0
                },
                "2": {
                    "X": 1.0,
                    "Y": 0.0,
                    "Z": 0.0
                },
            },
            "elements": {
                "1": {
                    "nodes": [1, 2],
                    "diameter": [0.3],
                    "type": "TUBULAR"
                },
                "10": {
                    "nodes": [1, 2],
                    "width": 0.0,
                    "height": 0.0,
                    "direction": [1.0, 0.0, 0.0],
                    "type": "CUBOID"
                }
            },
            "rotor_diameter": 0.0,
            "number_of_blades": 0
        }
    )

    return html.Div(
        children=[
            dbc.Toast(
                "",
                id="model-load-error",
                header="Model load error",
                is_open=False,
                dismissable=True,
                icon="danger",
                duration=3000,
                # top: 66 positions the toast below the navbar
                style={"position": "fixed", "top": 66, "right": 10, "width": 350},
            ),
            dbc.Row([
                dbc.Col(
                        dbc.Accordion(
                        [
                            dbc.AccordionItem(
                                dcc.Upload(
                                    id='upload-data',
                                    children=html.Div([
                                        'Drag and Drop or ',
                                        html.A('Select Files')
                                    ]),
                                    style={
                                        'width': '100%',
                                        'height': '60px',
                                        'lineHeight': '60px',
                                        'borderWidth': '1px',
                                        'borderStyle': 'dashed',
                                        'borderRadius': '5px',
                                        'textAlign': 'center',
                                        'margin': '10px'
                                    },
                                    multiple=False
                                ),
                                title="Upload file"
                            ),
                            dbc.AccordionItem(
                                dbc.DropdownMenu(
                                    [],
                                    label="Model"
                                ),
                                title="Select model"
                            ),
                            dbc.AccordionItem(
                                [
                                    html.Div(
                                        dbc.Button("Upload JSON", id="load-model", color="success", className="me-1", style={"padding": "10px"}),
                                        style={"paddingTop":"10px", "paddingBottom":"10px"}
                                    ),
                                    # json input
                                    dbc.Textarea(
                                        id="json-input",
                                        valid=True,
                                        className="mb-3",
                                        placeholder="A small, valid Textarea",
                                        style={"height":"100%"}
                                    ),
                                ],
                                title="JSON data input"
                            ),
                        ]
                        ),
                    style={"height":"100%"},
                    width=4
                ),
                dbc.Col(
                    DashWtgviewer(
                        id="viewer",
                        **viewer_data
                    ),
                    style={"height":"500px"},
                )
            ],
            style={"height":"500px"})
        ],
        style={
            "padding": "30px",
            "height": "100%",
        },
    )

