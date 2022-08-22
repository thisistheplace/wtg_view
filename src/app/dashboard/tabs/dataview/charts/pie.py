import plotly.express as px
import pandas as pd

from .base import BaseChart, modify_figure

class PieChart(BaseChart):

    @modify_figure
    def update_figure(self, data: pd.DataFrame):
        """Regenerate a figure using new data
        
        Args:
            data: pd.DataFrame containing new data

        Return:
            plotly.figure object
        """
        self._figure = px.pie(data, values="X", names="Y")
        return self.figure