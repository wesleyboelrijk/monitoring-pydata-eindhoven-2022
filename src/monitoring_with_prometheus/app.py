import asyncio

from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import joblib
import numpy as np
from prometheus_async.aio import time
from prometheus_client import generate_latest

from monitoring_with_prometheus.base_models import Features
from monitoring_with_prometheus.metrics import REQUEST_COUNT, REQUEST_LATENCY, REQUEST_ERROR, RESPONSE_DIST
from monitoring_with_prometheus.train import parse_features


app = FastAPI()

# Load prediction model
MODEL_VERSION = "DecisionTree_version_1"
model = joblib.load(f"models/{MODEL_VERSION}.pkl")


@app.get("/")
def root():
    """Root of the prometheus monitoring app"""
    return {"message": "Hello PyData, welcome from the Prometheus monitoring app root"}


@app.get('/metrics', response_class=PlainTextResponse)
def metrics():
    """This endpoint automatically exposes the metrics for Prometheus to scrape"""
    return generate_latest()


@app.get("/predict/random")
@time(REQUEST_LATENCY.labels(model_version="random"))  # async time functionality
async def get_random_prediction(time_delay_scale: float = 0.1, error_rate: float = 0.01) -> float:
    """Get a random uniform prediction with an exponential time delay"""
    REQUEST_COUNT.labels(model_version="random").inc()

    time_delay = np.random.exponential(time_delay_scale)
    await asyncio.sleep(time_delay)

    if np.random.uniform() < error_rate:
        REQUEST_ERROR.labels(model_version="random").inc()
        raise ValueError("Could not make a prediction")

    prediction = np.random.uniform()
    RESPONSE_DIST.labels(model_version="random").observe(prediction)

    return prediction


@app.post("/predict/model")
@REQUEST_LATENCY.labels(model_version=MODEL_VERSION).time()
def post_model_prediction(features: Features) -> int:
    """Get a prediction from the deployed model based on input features"""
    REQUEST_COUNT.labels(model_version=MODEL_VERSION).inc()

    X = parse_features(features)
    prediction = model.predict(X).item()

    RESPONSE_DIST.labels(model_version=MODEL_VERSION).observe(prediction)

    return prediction
