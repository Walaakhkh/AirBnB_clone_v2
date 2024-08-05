#!/usr/bin/env bash
# Script that sets up web servers for the deployment of web_static

# Install Nginx if it is not already installed
if ! dpkg -l | grep -q nginx; then
    apt-get update
    apt-get install -y nginx
fi

# Create necessary directories
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# Create a fake HTML file to test Nginx configuration
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

# Create a symbolic link, delete if it exists
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of /data/ folder to the current user and group
chown -R $USER:$USER /data/

# Update the Nginx configuration to serve the content
if ! grep -q "location /hbnb_static/" /etc/nginx/sites-available/default; then
    sed -i '/listen 80 default_server;/a \\n    location /hbnb_static/ {\n        alias /data/web_static/current/;\n    }' /etc/nginx/sites-available/default
fi

# Restart Nginx to apply changes
service nginx restart

exit 0
