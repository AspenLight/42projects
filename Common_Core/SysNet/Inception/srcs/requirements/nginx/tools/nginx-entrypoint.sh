#!/bin/sh

set -eu

if grep -q "__DOMAIN_NAME__" /etc/nginx/nginx.conf; then
	sed -i "s/__DOMAIN_NAME__/${DOMAIN_NAME}/g" /etc/nginx/nginx.conf
fi

mkdir -p /etc/nginx/ssl

if [ ! -f /etc/nginx/ssl/inception.crt ] || [ ! -f /etc/nginx/ssl/inception.key ]; then
	openssl req -x509 -nodes -days 365 \
		-newkey rsa:2048 \
		-keyout /etc/nginx/ssl/inception.key \
		-out /etc/nginx/ssl/inception.crt \
		-subj "/CN=${DOMAIN_NAME}"
fi

exec "$@"
