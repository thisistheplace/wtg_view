from .layout import layout

from .tabs import inputs, monitor, outputs, tabs

class Dashboard(tabs.TabBase):

    def __init__(self, app) -> None:
        self._app = app
        self._name = str(self.__class__)
        self._tabs = [
            inputs.Inputs(),
            monitor.Monitor(),
            outputs.Outputs()
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