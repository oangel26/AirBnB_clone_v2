#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static.

apt-get update -y
apt-get install nginx -y
service nginx restart
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
touch /data/web_static/releases/test/index.html
echo "Hello World!" > /data/web_static/releases/test/index.html

