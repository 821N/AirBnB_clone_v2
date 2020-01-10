#!/usr/bin/env bash
# perpare server

# install nginx
#sudo apt-get -y update
#sudo apt-get -y install nginx

sudo service nginx stop

# create directories
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared

# make test html file
echo "<marquee>heck</marquee>" | sudo tee -a /data/web_static/releases/test/index.html

# link
sudo ln -s -f /data/web_static/releases/test /data/web_static/current

# change owner of everything in /data
sudo chown -R ubuntu:ubuntu /data

# alias
echo "
server {
	add_header X-Served-By $HOSTNAME;
	listen 80 default_server;
	listen [::]:80 default_server;
	root /var/www/html;
	index index.html index.htm index.nginx-debian.html;
	server_name _;
	error_page 404 /404.html;
	location / {
		try_files \$uri \$uri/ =404;
	}
	location /hbnb_static {
		alias /data/web_static/current;
	}
}
" | sudo tee /etc/nginx/sites-available/default

sudo service nginx restart
