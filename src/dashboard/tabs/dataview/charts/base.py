from abc import ABC, abstractmethod

from uuid import uuid4
from dash import dcc, html, Input, Output, no_update
import pandas as pd

class BaseChart(ABC):

    def __init__(self, id_data:str, id_toggle:str, data:pd.DataFrame=None):
        self._id = uuid4()
        self._id_data = id_data
        self._id_toggle = id_toggle
        self._data = data
        self._figure = self.update_figure(data)
    
    @property
    def id(self):
        return str(self._id)

    @property
    def figure(self):
        return self._figure

    @property
    def id_data(self):
        return self._id_data

    @property
    def id_toggle(self):
        return self._id_toggle

    @abstractmethod
    def update_figure(self, data):
        pass

    @property
    def layout(self):
        return dcc.Graph(
            id=self.id,
            figure=self.figure,
            style={"position":"relative"}
        )

    def apply_callbacks(self, app):
        """Applies callbacks associated with this chart to the provided app
        
        Args:
            app: dash.Dash app
        """
        @app.callback(
            Output(self.id, "figure"),
            [Input(self.id_data, "data")]
        )
        def update_figure(data):
            return self.update_figure(pd.DataFrame.from_dict(data))

        @app.callback(
            Output(self.id, "style"),
            [Input(self.id_toggle, "value")]
        )
        def toggle_visibility(chart_values):
            if chart_values:
                return {"display":"block"}
            return {"display":"none"}
