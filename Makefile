.PHONY: help infra-up infra-down infra-validate infra-reset modules-list

help:
	@echo "LLMOps Course - Makefile Targets"
	@echo ""
	@echo "Infrastructure Commands:"
	@echo "  make infra-up          Start shared infrastructure (Postgres, MinIO, Redis, etc.)"
	@echo "  make infra-down        Stop shared infrastructure"
	@echo "  make infra-validate    Health check all infrastructure services"
	@echo "  make infra-reset       Stop and remove all volumes (hard reset)"
	@echo ""
	@echo "Module Commands:"
	@echo "  make modules-list      List all available modules"
	@echo "  make module-<N>        Enter module N (e.g., make module-03)"
	@echo ""
	@echo "Examples:"
	@echo "  make infra-up"
	@echo "  cd 03-scalable-data-preparation && make up && make validate"

infra-up:
	@echo "Starting LLMOps infrastructure..."
	docker compose up -d
	@echo "Waiting 10s for services to initialize..."
	sleep 10
	@echo "Running health checks..."
	bash infra/scripts/validate-stack.sh

infra-down:
	@echo "Stopping infrastructure..."
	docker compose down

infra-validate:
	@echo "Validating infrastructure health..."
	bash infra/scripts/validate-stack.sh

infra-reset:
	@echo "Hard reset: stopping and removing volumes..."
	docker compose down -v
	@echo "Infrastructure reset complete"

infra-logs:
	docker compose logs -f

modules-list:
	@echo "Available modules:"
	@ls -d [0-9][0-9]-*/ | sed 's/\///' | while read dir; do \
		title=$$(grep "^# " $$dir/README.md 2>/dev/null | head -1 | sed 's/^# //'); \
		echo "  $$dir: $$title"; \
	done

module-%:
	@module_path=$$(find . -maxdepth 1 -type d -name "$*-*" | head -1); \
	if [ -d "$$module_path" ]; then \
		cd "$$module_path" && bash -i; \
	else \
		echo "Module $* not found. Run 'make modules-list' to see available modules."; \
	fi
