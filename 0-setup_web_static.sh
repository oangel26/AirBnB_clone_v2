#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static.

sudo apt-get update -y
sudo apt-get install nginx -y
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
echo "Holberton School" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sudo cp /etc/nginx/sites-available/default /etc/nginx/sites-available/default.backup
sudo sed -i "/server_name _/a \\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}" /etc/nginx/sites-available/default
sudo service nginx restart
