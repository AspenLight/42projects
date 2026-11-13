COMPOSE = docker compose -f srcs/docker-compose.yml

all:
	mkdir -p $(HOME)/data/wordpress
	mkdir -p $(HOME)/data/mariadb
	$(COMPOSE) up --build -d

down:
	$(COMPOSE) down

clean:
	$(COMPOSE) down -v

fclean: clean
	docker system prune -af

re: fclean all

.PHONY: all down clean fclean re
