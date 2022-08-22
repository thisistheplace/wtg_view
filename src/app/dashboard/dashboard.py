from dash import Input, Output, no_update, callback_context

from .layout import layout

from .tabs import inputs, monitor, outputs, dataview, tabs

class Dashboard(tabs.TabBase):

    def __init__(self, app) -> None:
        self._app = app
        self._name = str(self.__class__)
        self._tabs = [
            inputs.Inputs(),
            monitor.Monitor(),
            outputs.Outputs(),
            dataview.Dataview()
        ]
        self._layout = layout(self._tabs)
        self.apply_callbacks(self._app)

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
        for tab in self._tabs:
            tab.apply_callbacks(self._app)

        @app.callback(
            Output("sidebar-column", "is_open"),
            [Input("sidebar-open", "n_clicks"),
            Input("sidebar-close", "n_clicks")],
            prevent_initial_callback=True
        )
        def toggle_collapse(n_open, n_close):
            button_id = callback_context.triggered[0]["prop_id"].split(".")[0]
            if button_id == "sidebar-open":
                return True
            elif button_id == "sidebar-close":
                return False
            else:
                return no_update