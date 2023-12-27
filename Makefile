help: ## Show help
	# From https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

# Variables
DOCKER_IMAGE_NAME = tsc
DOCKER_FILE = docker/Dockerfile
DOCKER_COMPOSE_FILE = docker/docker-compose.yml

# Commands
build: ## Builds docker image
	docker-compose -f $(DOCKER_COMPOSE_FILE) build --force-rm

run: ## Runs docker-compose
	docker-compose -f $(DOCKER_COMPOSE_FILE) up --force-recreate

shell: ## Runs inside new container
	docker-compose -f $(DOCKER_COMPOSE_FILE) run --rm api bash

test: ## Runs unittests
	docker-compose -f $(DOCKER_COMPOSE_FILE) up -d mongo
	poetry run pytest

clean: ## Clean project
	docker-compose -f $(DOCKER_COMPOSE_FILE) down
	docker rmi -f $(DOCKER_IMAGE_NAME)

.PHONY: build run run-local test clean
