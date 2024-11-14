#!/bin/bash
sudo docker build ./uicpc-registration-app/ -t acm-frontend-angular:1.0 # MAKE SURE THIS VALUE IS THE SAME IN .env
# sudo docker run --name frontend -p "127.0.0.1:8000:80" -d --restart=always acm-frontend-angular:1.0
sudo docker compose -f uicpc-registration-backend/docker-compose.yml up --build -d
