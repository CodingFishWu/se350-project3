FROM php:5.6-apache
COPY src/ /var/www/html/
COPY config/php.ini /usr/local/etc/php/

RUN apt-get update && apt-get install -y php5-mysqlnd