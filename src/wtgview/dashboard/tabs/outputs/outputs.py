from dash import Input, Output, State, no_update

import json

from .layout import layout
from .model import viewer
from ..tabs import TabBase

class Outputs(TabBase):

    def __init__(self) -> None:
        self._name = str(self.__class__.__name__)
        self._layout = layout()

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
            Output("model-load-error", "is_open"),
            Output("model-load-error", "children"),
            Output("viewer", "members"),
            Output("viewer", "nacelle"),
            Output("viewer", "rotor_diameter"),
            Output("viewer", "num_blades"),
            Output("viewer", "max"),
            Output("viewer", "min"),
            Output("viewer", "values"),
            [Input("load-model", "n_clicks")],
            State("json-input", "value")
        )
        def toggle_collapse(n, json_data):
            # load model data
            if json_data is None:
                return no_update
            elif json_data == "":
                return [True, "Could not load an empty string"] + [no_update] * 7
            else:
                try:
                    model_data = viewer(json.loads(json_data))
                    return [no_update, no_update] + list(model_data.values())
                except Exception:
                    return [True, "Invalid json data"] + [no_update] * 7