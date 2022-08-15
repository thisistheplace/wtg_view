from dash import Dash
import dash_bootstrap_components as dbc

from dashboard.dashboard import Dashboard

app = Dash(__name__, external_stylesheets=[dbc.themes.FLATLY, dbc.icons.FONT_AWESOME])
app.layout = Dashboard(app).layout