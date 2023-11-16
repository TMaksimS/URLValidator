up_db:
	docker compose -f docker-compose-local.yaml up -d
up_local: up_db
	python3 main.py
down_local:
	docker compose -f docker-compose-local.yaml down --remove-orphans
