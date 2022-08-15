"""Landing page"""
from dashboard import app

# get handle on the flask server for Gunicorn access in Docker
server = app.server

if __name__ == '__main__':
    app.run_server(debug=True)