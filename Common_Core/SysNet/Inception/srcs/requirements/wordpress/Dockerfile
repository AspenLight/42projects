FROM debian:12

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl ca-certificates php-fpm php-cli php-curl php-gd php-zip \
	php-mbstring php-mysql php-xml mariadb-client

RUN mkdir -p /run/php /var/www/html

RUN curl -fsSL https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar -o /usr/local/bin/wp \
	&& chmod +x /usr/local/bin/wp

COPY conf/www.conf /etc/php/8.2/fpm/pool.d/www.conf
COPY tools/wordpress-entrypoint.sh /usr/local/bin/wordpress-entrypoint.sh

RUN chmod +x /usr/local/bin/wordpress-entrypoint.sh \
	&& chown -R www-data:www-data /var/www/html /run/php

WORKDIR /var/www/html

EXPOSE 9000

ENTRYPOINT ["/usr/local/bin/wordpress-entrypoint.sh"]
CMD ["php-fpm8.2", "-F"]
