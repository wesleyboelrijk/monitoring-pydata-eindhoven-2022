import requests
from loguru import logger


URL = "http://localhost:5000/predict/random"


def synchronous():
    while True:
        try:
            r = requests.get(URL)
            logger.info(r.json())
        except ValueError as e:
            logger.warning(e)


if __name__ == "__main__":
    synchronous()
