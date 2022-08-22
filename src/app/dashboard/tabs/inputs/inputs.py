from dash import Input, Output, State, no_update

import uuid

from .layout import layout
from .data import read_flowchart, Flowcharts
from ..tabs import TabBase

class Inputs(TabBase):

    def __init__(self) -> None:
        self._name = str(self.__class__.__name__)
        self._layout = layout(read_flowchart(Flowcharts.DEMO))

    @property
    def layout(self):
        return self._layout

    @property
    def name(self):
        return self._name

    @staticmethod
    def create_node(num):
        return {
            "id": str(uuid.uuid4()),
            "data": { "label": f'Node {num}' },
            "position": { "x": 5, "y": 5 }
        }

    def apply_callbacks(self, app):
        """ Applies callback functions to app
        
        Layout should be added to the app prior to this being called. This
        method is helpful for apply callbacks to an app defined outside this module.

        Args:
            app: Dash.App
        """
        @app.callback(
            Output('workflow-store', 'data'),
            Input('workflow', 'nodes'),
            Input('workflow', 'edges'),
            State('workflow-store', 'data'),
            prevent_initial_callback=True
        )
        def nodes_updated(nodes, edges, data):
            data["nodes"] = nodes
            data["edges"] = edges
            return data

        @app.callback(
            Output('workflow', 'nodes'),
            Input('add-node', 'n_clicks'),
            State('workflow-store', 'data'),
            prevent_initial_callback=True
        )
        def add_node(n, data):
            if n > 0:
                return data["nodes"] + [self.create_node(len(data["nodes"]) + 1)]
            else:
                return no_update