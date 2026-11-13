This project contains Nginx, Wordpress, and MariaDB.

This project can be started with `make` in the `/Inception` folder accessible from the home of the user. This project can be stopped with `make down` and removed with `make fclean`. It can be relaunched with `make re`. 

Each program has a config file under `/srcs/[program name]/conf`. Wordpress/Nginx volume is under `/var/www/html` and MariaDB volume is under `/var/lib/mysql`

Credentials are accessible in the .env file and passwords can be found in the Secrets folder.

Services can be checked with `docker logs [program name]` (wordpress, mariadb, nginx)
