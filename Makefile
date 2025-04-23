.PHONY: run
run:
	@if netstat -tulpn | grep -q :8080; then \
		echo "Port 8080 is in use. Finding an alternative port..."; \
		port=8080; \
		while netstat -tulpn | grep -q :$$port; do \
			port=$$(($$port + 1)); \
		done; \
		echo "Starting on port: $$port"; \
		uvicorn backend.main:app --reload --port $$port; \
	else \
		echo "Port 8080 is available. Starting on port 8080"; \
		uvicorn backend.main:app --reload --port 8080; \
	fi

.PHONY: test
test:
	pytest

.PHONY: lint
lint:
	flake8 backend

.PHONY: build
build:
	docker build -t myapp:latest .
