from operator import truediv
from dash import Input, Output, State

from .layout import layout
from ..tabs import TabBase

class Monitor(TabBase):

    def __init__(self) -> None:
        self._name = str(self.__class__.__name__)
        self._layout = layout()
        self._progress = 0

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
            Output("monitor-store", "data"),
            Output("progress", "style"),
            Input("start", "n_clicks"),
            Input("stop", "n_clicks"),
        )
        def start_stop_monitor(start_clicks, stop_clicks):
            if start_clicks != stop_clicks:
                self._progress = 0
                return True, {"visibility": "visible"}
            else:
                return False, {"visibility": "hidden"}

        @app.callback(
            [Output("progress", "value"), Output("progress", "label")],
            Input("progress-interval", "n_intervals"),
            Input("start", "n_clicks"),
        )
        def update_progress(n, started):
            # check progress of some background process, in this example we'll just
            # use n_intervals constrained to be in 0-100
            progress = min(self._progress + 1, 100)
            self._progress = progress
            # only add text after 5% progress to ensure text isn't squashed too much
            return progress, f"{progress} %" if progress >= 5 else ""