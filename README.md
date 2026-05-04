## ssrd-deploy-assignment

FastAPI service with PostgreSQL and Redis, deployed to Kubernetes via GitHub Actions.

##
DevOps task: Mini deployment platform
Use a simple demo application (you can build it yourself or use a sample), for example:
API: one endpoint GET /health and GET /version

Frontend (optional): a static page that calls the API

Database (optional): Postgres or Redis

Minimum requirement: one service (API) running in a container

Containerization setup:
Prepare a Dockerfile (use a multi-stage build if it makes sense)
Create docker-compose for local run (API + dependencies)

Provide clear commands:

make up
make test
make down
(or equivalent)
Bonus:
Image size optimization
Run container as a non-root user
CI/CD Pipeline:

Create a pipeline (GitHub Actions / GitLab CI / etc.) that includes:

lint + unit tests (can be minimal)
build Docker image
push to a registry (e.g., GitHub Container Registry)
deploy to an environment (staging)
Required:
Pipeline must have at least 2 stages (build + deploy)
Image versioning (tag = commit SHA or semver)
Bonus:
Manual approval gate for “prod”
Rollback strategy (e.g., kubectl rollout undo)




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
