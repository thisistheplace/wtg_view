# wtg_view
Visualization components in React.js and python Dash specific to Offshore Wind Turbine Generators

## Components
### dash-wtgviewer
The [dash-wtgviewer](https://pypi.org/project/dash-wtgviewer/#description) package provides
3D visualisation of WTG structures using https://threejs.org/.

## Deployment
### Build
#### On Google Cloud Platform
To deploy the dashboard in a Docker container, open terminal within the git repo, run the following:

```
docker build -t wtg_view_gcp:latest -f src/app/Dockerfile-gcp src/app
```
Access at: https://127.0.0.1:8050

#### With `nginx`
From within the git repo, open terminal and run:

`bash run-docker.sh`

The app is then accessible at https://127.0.0.1:80

Build process based on:
https://medium.com/technonerds/a-production-grade-machine-learning-api-using-flask-gunicorn-nginx-and-docker-part-2-c69629199037