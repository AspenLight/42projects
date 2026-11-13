*This activity has been created as part of the 42 curriculum by aspthiba*

## Description
Inception is a project made to teach Docker, Docker Compose, Wordpress, MariaDB, and Nginx. The project requirements are to create a Docker setup to run a Wordpress frontend on the localhost. This is accomplished through Docker Compose and Makefile. This project is accomplished on a virtual machine and the Wordpress frontend is accessible within this machine at `https://aspthiba.42.fr`.

## Instructions
This project can be compiled, installed, and executed onthe virtual machine created for this project. The following commands have been created:
- `make` : compiles, installs, and runs the Docker program.
- `make down` : stops and removes containers created by `make`.
- `make clean` : stops and removes all containers and volumes created by `make`.
- `make fclean` : resets the project to a state before it was first executed.
- `make re` : resets and then restarts the project as if the commands `make fclean` and `make` were used sequentially.
All Makefile commands are protected by a Phony.

Once active, the project can be accessed at `https://aspthiba.42.fr`. The admin account is `the_owner` and all passwords have been set to `password123`.

## Resources
No AI was used during this project.

Information on Docker, Docker Compose, Wordpress, MariaDB, and Nginx were learned through lessons from fellow 42 students.

## Project Description
Docker was used in this project to create 3 environments for MariaDB, Wordpress, and Nginx. There are also 2 volumes, one for MariaDB and one shared between Wordpress and Nginx.

A Virtual Machine is a contained environment holding an OS that functions as a standalone computer while running as software. A Docker is a somewhat temporary environment created to hold a main program as well as any auxiliary programs and data the main program requires or produces. A Docker is removed once the main program stops.

Secrets are variables created to be obfuscated from the end user, stored separately from the main program, for the purpose of security. Environmental variables are variables stored outside the code so as to be accessible to all the programs in the environment.

A host network uses the host machine's network stack and provides no isolation between the host and the container. A default docker network, or bridge network, allows containers to communicate with each other and the host machine, but no access to the outside world.

Bind mounts directly mount a host directory into the container whereas volumes are managed by docker and do not need to exist as directories in the host.
