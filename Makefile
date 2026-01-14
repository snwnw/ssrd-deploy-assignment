up:
	docker compose up -d --build

down:
	docker compose down

test:
	docker compose run --rm api pytest
