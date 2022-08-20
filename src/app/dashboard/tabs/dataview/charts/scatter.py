import plotly.express as px
import pandas as pd

from .base import BaseChart

class ScatterChart(BaseChart):

    def update_figure(self, data: pd.DataFrame):
        """Regenerate a figure using new data
        
        Args:
            data: pd.DataFrame containing new data

        Return:
            plotly.figure object
        """
        self._figure = px.scatter(data)
        return self.figure