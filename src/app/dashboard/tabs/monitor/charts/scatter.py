from operator import truediv
from dash import Input, Output, no_update, ctx

from .layout import layout
from .figure import figure
from ...tabs import TabBase

class Scatter(TabBase):

    def __init__(self) -> None:
        self._name = str(self.__class__.__name__)
        self._data, self._figure = figure(None, 0)
        self._layout = layout(self._figure)
        self._df = None

    @property
    def layout(self):
        return self._layout

    @property
    def figure(self):
        return self._figure

    @property
    def name(self):
        return self._name

    def update_figure(self, count):
        self._data, self._figure = figure(self._data, count)
        return self.figure

    def reset_figure(self):
        self._data, self._figure = figure(None, 0)
        return self.figure

    def apply_callbacks(self, app):
        """ Applies callback functions to app
        
        Layout should be added to the app prior to this being called. This
        method is helpful for apply callbacks to an app defined outside this module.

        Args:
            app: Dash.App
        """
        pass