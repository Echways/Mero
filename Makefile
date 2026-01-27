PYTHON ?= python3
MANAGE := $(PYTHON) TimeTicket/manage.py

.PHONY: help venv install install-dev makemigrations migrate run test lint format check clean
.PHONY: docker-up docker-down docker-build docker-logs docker-makemigrations docker-migrate docker-shell
.PHONY: docker-prod-up docker-prod-down docker-reset

help:
	@echo "Targets:"
	@echo "  install           Install runtime deps"
	@echo "  install-dev       Install dev deps"
	@echo "  makemigrations    Create migrations"
	@echo "  migrate           Apply migrations"
	@echo "  run               Run dev server"
	@echo "  test              Run tests"
	@echo "  lint              Run ruff"
	@echo "  format            Run black"
	@echo "  check             Run lint + tests"
	@echo "  docker-up         Start docker compose"
	@echo "  docker-down       Stop docker compose and remove volumes"
	@echo "  docker-makemigrations  Create migrations inside web container"
	@echo "  docker-migrate    Apply migrations inside web container"
	@echo "  docker-prod-up    Start production compose"
	@echo "  docker-prod-down  Stop production compose and remove volumes"
	@echo "  docker-reset      Reset dev compose volumes"

install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements-dev.txt

makemigrations:
	$(MANAGE) makemigrations

migrate:
	$(MANAGE) migrate

run:
	$(MANAGE) runserver 0.0.0.0:8000

test:
	pytest

lint:
	ruff check .

format:
	black .

check: lint test

clean:
	find . -name "__pycache__" -type d -prune -exec rm -rf {} +

# Docker helpers

docker-up:
	docker compose up --build

docker-down:
	docker compose down -v

docker-build:
	docker compose build

docker-logs:
	docker compose logs -f

docker-makemigrations:
	docker compose run --rm web python TimeTicket/manage.py makemigrations

docker-migrate:
	docker compose run --rm web python TimeTicket/manage.py migrate

docker-shell:
	docker compose exec web sh

docker-prod-up:
	docker compose -f docker-compose.prod.yml up --build

docker-prod-down:
	docker compose -f docker-compose.prod.yml down -v

docker-reset:
	docker compose down -v
