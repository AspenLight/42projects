#!/bin/sh

set -eu

DB_PASSWORD="$(cat /run/secrets/db_password)"
DB_ROOT_PASSWORD="$(cat /run/secrets/db_root_password)"

mkdir -p /run/mysqld /var/lib/mysql
chown -R mysql:mysql /run/mysqld /var/lib/mysql

FIRST_INIT=0

if [ ! -d /var/lib/mysql/mysql ]; then
	FIRST_INIT=1

	mariadb-install-db \
		--user=mysql \
		--datadir=/var/lib/mysql \
		--skip-test-db
fi

/usr/sbin/mariadbd \
	--user=mysql \
	--datadir=/var/lib/mysql \
	--skip-networking \
	--socket=/run/mysqld/mysqld.sock &

while ! mariadb-admin --socket=/run/mysqld/mysqld.sock ping --silent; do
	sleep 1
done

if [ "$FIRST_INIT" = "1" ]; then
	mariadb --socket=/run/mysqld/mysqld.sock <<EOF
ALTER USER 'root'@'localhost' IDENTIFIED BY '${DB_ROOT_PASSWORD}';
DELETE FROM mysql.user WHERE User='';
DROP DATABASE IF EXISTS test;
DELETE FROM mysql.db WHERE Db='test' OR Db='test\\_%';
CREATE DATABASE IF NOT EXISTS \`${MYSQL_DATABASE}\`;
CREATE USER IF NOT EXISTS '${MYSQL_USER}'@'%' IDENTIFIED BY '${DB_PASSWORD}';
GRANT ALL PRIVILEGES ON \`${MYSQL_DATABASE}\`.* TO '${MYSQL_USER}'@'%';
FLUSH PRIVILEGES;
EOF
fi


mariadb \
	--socket=/run/mysqld/mysqld.sock \
	-uroot \
	-p"${DB_ROOT_PASSWORD}" <<EOF
CREATE DATABASE IF NOT EXISTS \`${MYSQL_DATABASE}\`;
CREATE USER IF NOT EXISTS '${MYSQL_USER}'@'%' IDENTIFIED BY '${DB_PASSWORD}';
ALTER USER '${MYSQL_USER}'@'%' IDENTIFIED BY '${DB_PASSWORD}';
GRANT ALL PRIVILEGES ON \`${MYSQL_DATABASE}\`.* TO '${MYSQL_USER}'@'%';
FLUSH PRIVILEGES;
EOF

mariadb-admin \
	--socket=/run/mysqld/mysqld.sock \
	-uroot \
	-p"${DB_ROOT_PASSWORD}" \
	shutdown

exec "$@"
