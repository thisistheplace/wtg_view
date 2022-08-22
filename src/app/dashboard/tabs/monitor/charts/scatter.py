from .layout import layout
from .figure import figure
from ...tabs import TabBase

def modify_figure(create_figure, *args, **kwargs):
    def inner(self, *args, **kwargs):
        fig = create_figure(self, *args, **kwargs)
        self.set_legend()
        self.set_margins()
        return fig
    return inner

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

    @modify_figure
    def update_figure(self, count):
        self._data, self._figure = figure(self._data, count)
        return self.figure

    def set_legend(self):
        self.figure.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))

    def set_margins(self):
        """Sets the margins around the plot (defined in px)"""
        self.figure.update_layout(margin=dict(
            b=0,
            t=100,
            l=0,
            r=0
        ))

    @modify_figure
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