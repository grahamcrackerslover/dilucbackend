#!/bin/bash

# Determine the project's name and directory
project_dir=$(dirname "$(pwd)")
project_name=$(basename "$project_dir")

# Determine the number of CPU cores and calculate the number of Gunicorn workers
num_cores=$(nproc)
num_workers=$((num_cores * 2 + 1))

# Prompt for user input for the username
read -r -p "Enter your username: " username

# Define the path to the virtual environment (assuming it's in the project directory)
venv_path="$project_dir/venv"

# Define the service file content
service_file_content="[Unit]
Description=gunicorn daemon for $project_name
After=network.target

[Service]
User=$username
Group=www-data
WorkingDirectory=$project_dir
ExecStart=$venv_path/bin/gunicorn \\
          --access-logfile - \\
          --workers $num_workers \\
          --bind unix:$project_dir/$project_name.sock \\
          $project_name.wsgi:application

[Install]
WantedBy=multi-user.target"

# Create the Gunicorn service file
echo "$service_file_content" > gunicorn_$project_name.service

echo "Gunicorn service file for $project_name with $num_workers workers has been created."
