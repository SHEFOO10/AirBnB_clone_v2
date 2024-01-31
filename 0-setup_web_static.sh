#!/usr/bin/env bash
# 0. Prepare your web servers

sudo apt-get update -y
sudo apt-get install nginx -y

sudo mkdir -p /data
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html

echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

sudo rm -rf /data/web_static/current
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
nginx_conf="
server {
   listen 80 default_server;
   listen [::]:80 default_server;

   server_name _;
   root /var/www/html;
   index index.html index.htm index.nginx-debian.html;

   location /redirect_me {
      rewrite ^ https://github.com/SHEFOO10 permanent;
   }

   location /hbnb_static {
      alias /data/web_static/current;
      index index.html;
   }

   error_page 404 /404.html;

   location = /404.html {
      internal;
   }

}";
echo "$nginx_conf" > /etc/nginx/sites-available/default;
sudo service nginx restart
