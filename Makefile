# Makefile para Inverkids MCP Server

.PHONY: help build up down restart logs shell test clean dev prod

# Variables
COMPOSE_FILE := docker-compose.yml
COMPOSE_DEV_FILE := docker-compose.dev.yml
SERVICE_NAME := inverkids-mcp
SERVICE_NAME_DEV := inverkids-mcp-dev

help: ## Mostrar esta ayuda
	@echo "Comandos disponibles:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

# Producción
build: ## Construir imagen de producción
	docker-compose -f $(COMPOSE_FILE) build

up: ## Iniciar contenedor de producción
	docker-compose -f $(COMPOSE_FILE) up -d
	@echo "Contenedor iniciado. Ver logs con: make logs"

down: ## Detener contenedor de producción
	docker-compose -f $(COMPOSE_FILE) down

restart: ## Reiniciar contenedor de producción
	docker-compose -f $(COMPOSE_FILE) restart

logs: ## Ver logs de producción
	docker-compose -f $(COMPOSE_FILE) logs -f $(SERVICE_NAME)

ps: ## Ver estado de contenedores
	docker-compose -f $(COMPOSE_FILE) ps

# Desarrollo
dev-build: ## Construir imagen de desarrollo
	docker-compose -f $(COMPOSE_DEV_FILE) build

dev-up: ## Iniciar contenedor de desarrollo
	docker-compose -f $(COMPOSE_DEV_FILE) up -d
	@echo "Contenedor de desarrollo iniciado"

dev-down: ## Detener contenedor de desarrollo
	docker-compose -f $(COMPOSE_DEV_FILE) down

dev-logs: ## Ver logs de desarrollo
	docker-compose -f $(COMPOSE_DEV_FILE) logs -f $(SERVICE_NAME_DEV)

dev-restart: ## Reiniciar contenedor de desarrollo
	docker-compose -f $(COMPOSE_DEV_FILE) restart

# Shell y depuración
shell: ## Abrir shell en contenedor de producción
	docker-compose -f $(COMPOSE_FILE) exec $(SERVICE_NAME) bash

dev-shell: ## Abrir shell en contenedor de desarrollo
	docker-compose -f $(COMPOSE_DEV_FILE) exec $(SERVICE_NAME_DEV) bash

python: ## Abrir Python interactivo en contenedor
	docker-compose -f $(COMPOSE_FILE) exec $(SERVICE_NAME) python

ipython: ## Abrir IPython en contenedor de desarrollo
	docker-compose -f $(COMPOSE_DEV_FILE) exec $(SERVICE_NAME_DEV) ipython

# Testing
test: ## Ejecutar tests en contenedor
	docker-compose -f $(COMPOSE_FILE) exec $(SERVICE_NAME) pytest

test-dev: ## Ejecutar tests en contenedor de desarrollo
	docker-compose -f $(COMPOSE_DEV_FILE) exec $(SERVICE_NAME_DEV) pytest

test-coverage: ## Ejecutar tests con cobertura
	docker-compose -f $(COMPOSE_DEV_FILE) exec $(SERVICE_NAME_DEV) pytest --cov=src --cov-report=html

lint: ## Ejecutar linter
	docker-compose -f $(COMPOSE_DEV_FILE) exec $(SERVICE_NAME_DEV) ruff check src/

format: ## Formatear código
	docker-compose -f $(COMPOSE_DEV_FILE) exec $(SERVICE_NAME_DEV) ruff format src/

# Limpieza
clean: ## Limpiar contenedores y volúmenes
	docker-compose -f $(COMPOSE_FILE) down -v
	docker-compose -f $(COMPOSE_DEV_FILE) down -v

clean-all: clean ## Limpiar todo (contenedores, volúmenes, imágenes)
	docker system prune -af --volumes

# Información
info: ## Mostrar información del sistema
	@echo "Docker Version:"
	@docker --version
	@echo ""
	@echo "Docker Compose Version:"
	@docker-compose --version
	@echo ""
	@echo "Images:"
	@docker images | grep inverkids || echo "No images found"
	@echo ""
	@echo "Running Containers:"
	@docker ps --filter "name=inverkids" || echo "No containers running"

# Setup inicial
setup: ## Configuración inicial del proyecto
	@echo "Configurando proyecto Inverkids MCP..."
	@if [ ! -f .env ]; then \
		cp .env.example .env; \
		echo "Archivo .env creado. Por favor, configura las variables."; \
	else \
		echo ".env ya existe."; \
	fi
	@mkdir -p logs
	@echo "Directorio de logs creado"
	@echo "Setup completado. Ejecuta 'make build && make up' para iniciar."

# Comandos combinados
rebuild: down build up ## Reconstruir y reiniciar contenedor

dev-rebuild: dev-down dev-build dev-up ## Reconstruir y reiniciar contenedor de desarrollo

prod: build up ## Alias para producción rápida

dev: dev-build dev-up ## Alias para desarrollo rápido