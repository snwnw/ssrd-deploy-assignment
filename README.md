## ssrd-deploy-assignment

FastAPI service with PostgreSQL and Redis, deployed to Kubernetes via GitHub Actions.

## Usage

make up    - start
make test  - run tests
make lint  - lint
make down  - stop

Frontend: [http://localhost](http://localhost)

## API

 `GET /health`  - Health check 
 `GET /version` - App version
 `GET /db`	- PostgreSQL check 
 `GET /cache`   - Redis request counter

## CI/CD
lint -> test -> build & push (GHCR) -> deploy staging -> deploy production

runs on a self-hosted GitHub Actions runner with a local k3s cluster.
Image tagged with commit SHA. Automatic rollback on failed deploy.

## Stack

FastAPI
PostgreSQL
Redis
Docker
GitHub Actions
Kubernetes (k3s)
