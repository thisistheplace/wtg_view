from dash import Input, Output

from .layout import layout
from ..tabs import TabBase

class Monitor(TabBase):

    def __init__(self) -> None:
        self._name = str(self.__class__.name)
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
            [Output("progress", "value"), Output("progress", "label")],
            [Input("progress-interval", "n_intervals")],
        )
        def update_progress(n):
            # check progress of some background process, in this example we'll just
            # use n_intervals constrained to be in 0-100
            progress = min(n % 110, 100)
            # only add text after 5% progress to ensure text isn't squashed too much
            return progress, f"{progress} %" if progress >= 5 else ""