.DEFAULT_GOAL := help

help:
	@echo "Targets: dev test lint format typecheck db-migrate db-reset compose-config"

dev:
	docker compose up --build

test:
	python -m pytest
	pnpm test

lint:
	python -m ruff check backend/src backend/tests sdk/python/src sdk/python/tests
	pnpm lint

format:
	python -m ruff format backend/src backend/tests sdk/python/src sdk/python/tests
	pnpm --filter @agentguard/frontend format

typecheck:
	python -m mypy backend/src sdk/python/src
	pnpm typecheck

db-migrate:
	docker compose run --rm backend alembic upgrade head

db-reset:
	docker compose down -v
	docker compose up -d postgres redis
	docker compose run --rm backend alembic upgrade head

compose-config:
	docker compose config
