FROM python:3.9

WORKDIR app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN pip install .

ENTRYPOINT ["uvicorn", "monitoring_with_prometheus.app:app", "--host", "0.0.0.0", "--reload"]
CMD ["--port", "5000"]
