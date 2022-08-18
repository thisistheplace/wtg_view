from dash import Input, Output, State, no_update

import uuid

from .fileutils import parse_contents
from .layout import layout
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
            Output("model-load-error", "is_open"),
            Output("model-load-error", "children"),
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