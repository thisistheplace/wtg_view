# wtg_view
Visualization components in React.js and python Dash specific to Offshore Wind Turbine Generators

## Components
### dash-wtgviewer
The [dash-wtgviewer](https://pypi.org/project/dash-wtgviewer/#description) package provides
3D visualisation of WTG structures using https://threejs.org/.

## Deployment
### Build
To deploy the dashboard in a Docker container, run the following:

```
docker build -t wtg_view:latest -f build/Dockerfile src
```

### Run
To run the docker image:

```
docker run -p 8050:8000 wtg_view
```

Access at: https://127.0.0.1:8050

Build process based on:
https://medium.com/technonerds/a-production-grade-machine-learning-api-using-flask-gunicorn-nginx-and-docker-part-2-c69629199037