# Lowering the barrier for ML monitoring
Wesley Boelrijk @ PyData Eindhoven 2022

This repository holds the example project used for the PyData Eindhoven 2022 talk: "Lowering the barrier for ML monitoring".
The project uses `FastAPI` to host a trained `scikit-learn` model. Subsequently, the tools `Prometheus` and `Grafana` are used for monitoring and visualisation.


## Project structure

- In `/data`, a subsampled dataset is available, originating from the Kaggle competition: [Expresso Churn](https://www.kaggle.com/datasets/hamzaghanmi/expresso-churn-prediction-challenge?select=Train.csv)
- In `/models`, a pretrained DecisionTree model (accuracy 0.85) is saved as pickle. Feel free to train a model yourself or make changes to the sklearn pipeline.
- In `/dashboards`, the Grafana dashboard from the demo is saved. It can be loaded into Grafana using the import dashboard functionality.
- In `/prometheus`, the configuration for prometheus is defined
- In `/prometheus-data`, the monitored data is saved and volume mounted with the docker container
- In `/grafana`, the configuration for grafana is defined

## Run it yourself

### Install the python package locally
To run the example project yourself, you need to install the python package locally:

- `python3 -m venv venv`
- `source venv/bin/activate`
- `pip install --upgrade pip`
- `pip install .`


### Run the docker-compose
Run the set of applications with docker-compose. 
Make sure you have Docker desktop or an alternative running:

`docker-compose build && docker-compose up`

After that this should give you 3 running containers Docker containers:

- FastAPI application at `0.0.0.0:5000` --> checkout `/docs` to find info on endpoints
- Prometheus at `0.0.0.0:9090`
- Grafana at `0.0.0.0:3000`


### Simulate "Random" endpoint

This calls the `/predict/random` endpoint repeatedly with `GET` requests.

`python src/monitoring_with_prometheus/simulate_random.py`


### Simulate "Decision Tree" endpoint
This calls the `/predict/model` endpoint repeatedly with `POST` requests containing feature values as payload.

`python src/monitoring_with_prometheus/simulate_model.py`

### Available model versions on grafana dashboard
- random
- DecisionTree_version_1

### Questions?
If there are any questions about this repo, feel free to open an issue or send me a personal message.
