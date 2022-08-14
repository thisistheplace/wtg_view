from .layout import layout
from ..tabs import TabBase

class Banner(TabBase):

    def __init__(self) -> None:
        self._name = str(self.__class__.__name__)
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
        pass