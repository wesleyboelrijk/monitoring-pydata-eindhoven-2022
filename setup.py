from setuptools import setup, find_packages


base_requirements = [
    "aiohttp>=3.8.1",
    "fastapi>=0.78.0",
    "joblib>=1.1.0",
    "loguru>=0.6.0",
    "numpy>=1.22.3",
    "pandas>=1.4.2",
    "prometheus-async>=22.2.0",
    "prometheus_client>=0.14.1",
    "pydantic>=1.9.0",
    "requests>=2.27.1",
    "scikit-learn>=1.1.0",
    "uvicorn>=0.17.6",
]

dev_requirements = [
    "flake8>=4.0.1",
    "pytest>=7.1.2",
]

setup(
    name="monitoring_with_prometheus",
    version="0.0.1",
    description="Repo for ML monitoring training with prometheus",
    author="Wesley Boelrijk",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=base_requirements,
    extras_require={"dev": dev_requirements},
)
