#!/bin/bash

# Function to check if Nginx is installed
check_nginx_installed() {
    if ! command -v nginx &> /dev/null; then
        echo "Nginx is not installed. Installing Nginx..."
        sudo apt-get update
        sudo apt-get install nginx -y
    else
        echo "Nginx is already installed."
    fi
}

# Prompt for server name
read -r -p "Enter the server name (e.g., yourdomain.com www.yourdomain.com): " server_name

# Prompt for proxy pass with default value
read -p "Enter the proxy pass [default: http://localhost:8000]: " proxy_pass
proxy_pass=${proxy_pass:-http://localhost:8000}

# Check and install Nginx if necessary
check_nginx_installed

# Create the Nginx configuration file
cat << EOF > website.conf
server {
    listen 80;
    server_name $server_name;

    location /static/ {
        alias /path/to/your/static_root/;
        expires 30d;
    }

    location / {
        proxy_pass $proxy_pass;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
    }

    # other configurations...
}
EOF

# Move the configuration file to Nginx's sites-available and create a symbolic link in sites-enabled
sudo mv website.conf /etc/nginx/sites-available/
sudo ln -s /etc/nginx/sites-available/website.conf /etc/nginx/sites-enabled/

# Test Nginx configuration and reload Nginx
sudo nginx -t && sudo systemctl reload nginx

echo "Nginx configuration file 'website.conf' has been created and Nginx has been reloaded."
