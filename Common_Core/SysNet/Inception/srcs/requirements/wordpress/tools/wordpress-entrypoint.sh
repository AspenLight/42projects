#!/bin/sh

set -eu

DB_PASSWORD="$(cat /run/secrets/db_password)"
WP_ADMIN_PASSWORD="$(grep '^WP_ADMIN_PASSWORD=' /run/secrets/credentials | cut -d '=' -f2-)"
WP_USER_PASSWORD="$(grep '^WP_USER_PASSWORD=' /run/secrets/credentials | cut -d '=' -f2-)"

admin_name="$(printf "%s" "$WP_ADMIN_USER" | tr '[:upper:]' '[:lower:]')"
case "$admin_name" in
	*admin*|*administrator*)
		echo "the admin name shoudn't contain admin or administrator"
		exit 1
		;;
esac

while ! mariadb -h mariadb -u"$MYSQL_USER" -p"$DB_PASSWORD" -e "SELECT 1;"; do
    echo "Waiting for MariaDB"
    sleep 2
done

cd /var/www/html

if [ ! -f wp-load.php ]; then
    wp core download --allow-root
fi

if [ ! -f wp-config.php ]; then
    wp config create \
        --allow-root \
        --dbname="$MYSQL_DATABASE" \
        --dbuser="$MYSQL_USER" \
        --dbpass="$DB_PASSWORD" \
        --dbhost="mariadb:3306"
fi

if ! wp core is-installed --allow-root; then
    wp core install \
        --allow-root \
        --url="https://$DOMAIN_NAME" \
        --title="$WP_TITLE" \
        --admin_user="$WP_ADMIN_USER" \
        --admin_password="$WP_ADMIN_PASSWORD" \
        --admin_email="$WP_ADMIN_EMAIL"

    wp user create "$WP_USER" "$WP_USER_EMAIL" \
        --allow-root \
        --user_pass="$WP_USER_PASSWORD" \
        --role=author
fi

chown -R www-data:www-data /var/www/html

exec "$@"

