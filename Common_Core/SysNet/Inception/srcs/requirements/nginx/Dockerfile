FROM debian:12

RUN apt-get update && apt-get install -y --no-install-recommends \
	nginx \
	openssl \
	ca-certificates

RUN mkdir -p /etc/nginx/ssl /var/www/html

COPY conf/nginx.conf /etc/nginx/nginx.conf
COPY tools/nginx-entrypoint.sh /usr/local/bin/nginx-entrypoint.sh

RUN chmod +x /usr/local/bin/nginx-entrypoint.sh

EXPOSE 443

ENTRYPOINT ["/usr/local/bin/nginx-entrypoint.sh"]
CMD ["nginx", "-g", "daemon off;"]
