from prometheus_client import Counter, Histogram


REQUEST_COUNT = Counter(
    "request_count",
    "Total number of requests",
    labelnames=["model_version"]
)

REQUEST_ERROR = Counter(
    "request_error",
    "Total number or errors in the requests",
    labelnames=["model_version"]
)

REQUEST_LATENCY = Histogram(
    "request_latency_seconds",
    "Time spent processing request in seconds",
    labelnames=["model_version"]
)

RESPONSE_DIST = Histogram(
    "response_distribution",
    "Response distribution of the predictions",
    buckets=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
    labelnames=["model_version"],
)

MODEL_CATEGORICAL = Counter(
    "model_categorical",
    "Counts category occurrence for each categorical feature.",
    labelnames=["feature", "category"],
)

IMPUTED = Counter(
    "imputed",
    "The number of values imputed",
    labelnames=["feature", "method"],
)
