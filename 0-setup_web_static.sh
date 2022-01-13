#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static.

apt-get update -y
apt-get install nginx -y
mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared/
touch /data/web_static/releases/test/index.html
echo "Holberton School" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data/
cp /etc/nginx/sites-available/default /etc/nginx/sites-available/default.backup
sed -i '/listen 80 default_server/a location /hbnb_static {\n\talias /data/web_static/current/;\n\tautoindex off;\n}' /etc/nginx/sites-available/default
service nginx restart
