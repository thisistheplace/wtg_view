from dash import html, dcc
import dash_bootstrap_components as dbc

# import sys
# sys.path.append("../../dash-ifc-wtg/dash_ifc_wtg")
# sys.path.append("../../dash-ifc-wtg")
# from DashIfcWtg import DashIfcWtg
from dash_ifc_wtg import DashIfcWtg

from .model import list_model_names

def make_toast(id:str):
    return dbc.Toast(
        id=id,
        header="Model load error",
        is_open=False,
        dismissable=True,
        icon="danger",
        duration=3000,
        # top: 66 positions the toast below the navbar
        style={"position": "fixed", "top": 66, "right": 10, "width": 350},
    )

def layout(id:str):
    """Defines the layout of the input tab

    Returns:
        dash.html div
    """
    return html.Div(
        children=[
            make_toast("user-model-load-error"),
            make_toast("default-model-load-error"),
            # Serve local css
            html.Link(
                rel='stylesheet',
                href='/static/css/index.css'
            ),
            dbc.Container([
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
                                        [
                                            dbc.DropdownMenuItem(name, id={
                                                'type': "model-selection",
                                                'index': idx
                                            }) for idx, name in enumerate(list_model_names())
                                        ],
                                        id="select-model",
                                        label="Model"
                                    ),
                                    title="Select model"
                                ),
                            ]
                            ),
                        style={
                            "height":"100%",
                            "paddingTop":"10px"
                        },
                        lg=4,
                        sm=12
                    ),
                    dbc.Col(
                        html.Div(
                            DashIfcWtg(f"{id}", ""),
                            style={
                                "height":"75vh",
                                "width":"100%",
                                "paddingTop":"10px"
                            },
                        ),
                        style={"height":"100%"},
                        lg=8,
                        sm=12
                    )
                ],
                style={"paddingTop":"20px"})
            ]),
        ],
        style={
            "height": "100%",
            "maxWidth": "100%"
        },
    )

