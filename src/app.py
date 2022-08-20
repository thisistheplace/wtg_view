"""Landing page"""
from dash import Dash
import dash_bootstrap_components as dbc
from flask import Flask, make_response
from flask_restful import Resource, Api

from dashboard import Dashboard
from dashboard.fileutils import read_wasm

# Serve up wasm file since it doesn't get shipped with dash-ifc-wtg yet
server = Flask('wtg_view')
app = Dash(server=server, external_stylesheets=[dbc.themes.FLATLY, dbc.icons.FONT_AWESOME])
api = Api(server)

class WasmFile(Resource):
    def get(self):
        response = make_response(read_wasm("static/web-ifc.wasm"))
        response.headers["content-type"] = "application/wasm"
        return response

api.add_resource(WasmFile, '/web-ifc.wasm')

app.layout = Dashboard(app).layout

if __name__ == '__main__':
    app.run_server(debug=True)