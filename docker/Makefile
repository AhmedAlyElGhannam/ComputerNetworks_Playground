build:
	docker compose build --no-cache

build_cache:
	docker compose build 

run:
	docker compose up

server:
	docker exec -it server /bin/bash

client:
	docker exec -it client /bin/bash

burn:
	docker rm -v -f $(docker ps -qa)

purge:
	docker system prune -a