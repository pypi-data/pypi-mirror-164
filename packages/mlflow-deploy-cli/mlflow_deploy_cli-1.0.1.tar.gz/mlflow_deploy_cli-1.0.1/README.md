# mlflow-deployment

CLI for deployment of [MLFlow](https://mlflow.org/) with support for backend and artifact stores.

Deploy MLFlow with support for PostgreSQL, Azure Blobs, Amazon S3 and Google Cloud Platform with ease.

# Usage

1. [`pip install mlflow-deploy-cli`](https://pypi.org/project/mlflow-deploy-cli/)

2. `python -m mlflow_deploy_cli --artifact-store '<desired_store>'` _can be [`azure`](https://www.mlflow.org/docs/latest/tracking.html#azure-blob-storage), [`s3`](https://www.mlflow.org/docs/latest/tracking.html#id82), [`gcp`](https://www.mlflow.org/docs/latest/tracking.html#id84) or `local`_

3. `cd build`

4. `docker build . -t mlflow`

5. `docker-compose up -f docker-compose.yml up`

MLFlow is up and running 🚀.