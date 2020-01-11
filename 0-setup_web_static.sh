#!/usr/bin/env bash
# Bash script that sets up the web servers for the deployment of web_static

# if [ $which nginx ]; then
#    echo "nginx ya instalado"
# else
sudo apt-get update
sudo apt-get -y install nginx
# fi
sudo mkdir -p data/web_static/shared/
sudo mkdir -p data/web_static/releases/test/
echo Holberton School | sudo tee /data/web_static/releases/test/index.html
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "s/server_name _;/server_name _;\n\tlocation \/hbnb_static\/ {\n\t\talias \/data\/web_static\/current\/;\n\t}/" /etc/nginx/sites-available/default
sudo service nginx restart
exit 0
