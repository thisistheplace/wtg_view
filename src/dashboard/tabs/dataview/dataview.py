from uuid import uuid4
import pandas as pd

from .layout import layout
from ..tabs import TabBase

from .charts import ScatterChart, PieChart, BarChart

class Dataview(TabBase):

    def __init__(self) -> None:
        self._name = str(self.__class__.__name__)
        self._data = pd.DataFrame.from_dict({"X":[1, 2], "Y":[4,5]})
        self._id = uuid4()
        self._charts = [
            ScatterChart(
                self.id,
                "select-scatter",
                self._data
            ),
            PieChart(
                self.id,
                "select-pie",
                self._data
            ),
            BarChart(
                self.id,
                "select-bar",
                self._data
            )
        ]
        self._layout = layout(self.id, self.charts, self._data)

    @property
    def id(self):
        return str(self._id)

    @property
    def charts(self):
        return self._charts

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
        for chart in self.charts:
            chart.apply_callbacks(app)