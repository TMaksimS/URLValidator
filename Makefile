up_db:
	docker compose -f docker-compose-local.yaml up -d
up_local: up_db
	python3 main.py
down_local:
	docker compose -f docker-compose-local.yaml down --remove-orphans

up_cd:
	docker compose -f docker-compose-cd.yaml up -d
up_uor: up_cd
	python3 uor.py
down_cd:
	docker compose -f docker-compose-cd.yaml down --remove-orphans && docker rmi webapp