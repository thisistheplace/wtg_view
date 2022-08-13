from dash import Dash
import dash_bootstrap_components as dbc

from dashboard.layout import layout

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = layout()