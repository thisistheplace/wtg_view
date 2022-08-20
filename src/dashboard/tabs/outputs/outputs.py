from ast import literal_eval
import base64

from dash import Input, Output, State, no_update, callback_context, ALL

import uuid

from .fileutils import parse_contents
from .layout import layout
from .model import read_model
from ..tabs import TabBase

class Outputs(TabBase):

    def __init__(self) -> None:
        self._id = str(uuid.uuid4())
        self._name = str(self.__class__.__name__)
        self._layout = layout(self.id)

    @property
    def id(self):
        return self._id

    @property
    def layout(self):
        return self._layout

    @property
    def name(self):
        return self._name

    def apply_callbacks(self, app):
        """ Applies callback functions to app
        
        Layout should be added to the app prior to this being called. This
        method is helpful for apply callbacks to an app defined outside this module.

        Args:
            app: Dash.App
        """
        @app.callback(
            Output("user-model-load-error", "is_open"),
            Output("user-model-load-error", "children"),
            Output(self.id, "ifc_file_contents"),
            Input('upload-data', 'contents'),
            State('upload-data', 'filename'),
            prevent_initial_call=True
        )
        def update_output(file_contents, filename):
            try:
                ifc_data = parse_contents(file_contents, filename)
                return False, no_update, ifc_data
            except Exception as e:
                return True, f"Failed to load model:\n{e}", no_update

        @app.callback(
            Output("default-model-load-error", "is_open"),
            Output("default-model-load-error", "children"),
            Output('upload-data', 'contents'),
            Output('upload-data', 'filename'),
            Output('select-model', 'label'),
            Input({'type': 'model-selection', 'index': ALL}, 'n_clicks'),
            State({'type': 'model-selection', 'index': ALL}, 'children'),
            prevent_initial_call=True
        )
        def update_output(n_clicks, labels):
            try:
                button_info = literal_eval(callback_context.triggered[0]["prop_id"].split(".")[0])
                model_name = labels[button_info["index"]]
                fname, model = read_model(model_name)
                model_bytes = base64.b64encode(bytes(model, 'utf-8'))
                return no_update, no_update, f"none,{str(model_bytes, 'utf-8')}", fname, model_name
            except Exception as e:
                return True, f"Failed to load model:\n{e}", no_update, no_update, no_update