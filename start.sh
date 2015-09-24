#!/bin/bash
source /etc/apache2/envvars
tail -F /var/log/apache2/* &
tail -F /var/www/html/app/logs/* &
exec apache2 -D FOREGROUND