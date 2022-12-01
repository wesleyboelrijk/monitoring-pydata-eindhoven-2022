import time

from loguru import logger
import requests

from monitoring_with_prometheus.train import load_data, parse_pandas_dtypes, split_X_y


if __name__ == "__main__":
    X, _ = (
        load_data("data/prod.csv")
        .reset_index(drop=True)
        .pipe(parse_pandas_dtypes)
        .pipe(split_X_y)
    )

    logger.info(f"Simulating {len(X)} instances")
    time.sleep(3)

    for idx, row in X.iterrows():
        features = row.to_json()
        r = requests.post("http://localhost:5000/predict/model", data=features)
        logger.info(f"instance: {idx}, prediction: {r.json()}")
