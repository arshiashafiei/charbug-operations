#!/bin/bash
set -e

args=("$@")
sudo docker build ./uicpc-registration-app/ -t acm-frontend-angular:${args[0]} # MAKE SURE THIS VALUE IS THE SAME IN .env

sudo docker compose -f uicpc-registration-backend/docker-compose.yml up --build -d
