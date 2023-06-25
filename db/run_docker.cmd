SET COMPOSE_CONVERT_WINDOWS_PATHS=1
:: Bring the cluster online, according to the compose file
docker-compose --file db_compose.yml up --build --detach