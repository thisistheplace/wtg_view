from operator import truediv
from dash import Input, Output, no_update, ctx

from .charts.figure import figure

from .layout import layout
from .charts import Scatter
from ..tabs import TabBase

class Monitor(TabBase):

    def __init__(self) -> None:
        self._name = str(self.__class__.__name__)
        self._charts = [Scatter()]
        self._layout = layout(self._charts)
        self._progress = 0
        self._running = False

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
            # Figure out which button was clicked
            button_id = ctx.triggered_id 
            if button_id == "start":
                if self._running:
                    return no_update
                self._running = True
                self._progress = 0
                self._charts[0].reset_figure()
                return True, {"visibility": "visible"}
            else:
                self._running = False
                return False, {"visibility": "hidden"}

        @app.callback(
            Output("progress", "value"),
            Output("progress", "label"),
            Output("monitor-badge", "children"),
            Input("progress-interval", "n_intervals"),
            Input("start", "n_clicks"),
        )
        def update_progress(n, started):
            if self._running == True:
                # check progress of some background process, in this example we'll just
                # use n_intervals constrained to be in 0-100
                progress = min(self._progress + 1, 100)
                self._progress = progress
                if progress >= 100:
                    self._running = False
                # only add text after 5% progress to ensure text isn't squashed too much
                return progress, f"{progress} %" if progress >= 5 else "", progress
            else:
                return no_update

        @app.callback(
            Output("monitor-figure", "figure"),
            Input("monitor-badge", "children")
        )
        def update_figure(count):
            if self._running == True:
                # create new figure
                # TODO: make the chart components generalized so they can be updated using MATCH
                return self._charts[0].update_figure(int(count))
            else:
                return no_update