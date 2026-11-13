FROM debian:12

RUN apt-get update && apt-get install -y --no-install-recommends \
	mariadb-server mariadb-client

RUN mkdir -p /run/mysqld /var/lib/mysql \
	&& chown -R mysql:mysql /run/mysqld /var/lib/mysql

COPY conf/50-server.cnf /etc/mysql/mariadb.conf.d/50-server.cnf
COPY tools/mariadb-entrypoint.sh /usr/local/bin/mariadb-entrypoint.sh

RUN chmod +x /usr/local/bin/mariadb-entrypoint.sh

EXPOSE 3306

ENTRYPOINT ["/usr/local/bin/mariadb-entrypoint.sh"]
CMD ["/usr/sbin/mariadbd", "--user=mysql"]
