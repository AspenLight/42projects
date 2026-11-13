This project contains Nginx, Wordpress, and MariaDB.

This project can be started with `make` in the `/Inception` folder accessible from the home of the user. This project can be stopped with `make down` and removed with `make fclean`

The website can be accessed at `https://aspthiba.42.fr` and the admin panel can be accessed at `https://aspthiba.42.fr/wp-admin`

Credentials are accessible in the .env file and passwords can be found in the Secrets folder.

Services can be checked with `docker logs [program name]` (wordpress, mariadb, nginx)
