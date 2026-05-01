up:
	docker compose up -d --build

down:
	docker compose down

test:
	docker compose run --rm api pytest

lint:
	docker compose run --rm api ruff check . --no-cache

