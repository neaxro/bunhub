.PHONY: help
help: ## Show this help message with available targets and descriptions.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z0-9_-]+:.*?## / {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.PHONY: up
up: ## Runs backend.
	PYTHONPATH=./backend fastapi dev backend/app/main.py

.PHONY: frontend-openapi-generator
frontend-openapi-generator: ## Generates service code based on Swagger docs.
	curl http://127.0.0.1:8000/openapi.json -o openapi.json \
	&& npx openapi-typescript-codegen \
		--input openapi.json \
		--output frontend/src/api \
		--client fetch \
	&& rm openapi.json
