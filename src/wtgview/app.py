"""Landing page"""
from dashboard import app
from dashboard.callbacks import *

if __name__ == '__main__':
    app.run_server(debug=True)