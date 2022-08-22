from uuid import uuid4
import pandas as pd

from dash import Input, Output, ALL, no_update

from .layout import layout
from ..tabs import TabBase

from .charts import ScatterChart, PieChart, BarChart

class Outputs(TabBase):

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

        @app.callback(
            Output({'type': 'dataview-chart-column', 'index': ALL}, 'lg'),
            Output({'type': 'dataview-chart-column', 'index': ALL}, 'style'),
            [Input(chart.id_toggle, "value") for chart in self.charts]
        )
        def resize_chart_columns(*values):
            count_visible = values.count(True)
            if count_visible == 0:
                return no_update
            width = 12 / count_visible
            widths = [visible * width for visible in values]
            styles = []
            for vis in values:
                if vis:
                    styles.append({"display":"block"})
                else:
                    styles.append({"display":"none"})
            return [widths] + [styles]