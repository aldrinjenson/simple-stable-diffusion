#!/bin/bash
# one click start script

if ! ss -ln | grep -q ':7860'; then
    echo "No service running on port 7860. Please make sure that stable-diffusion-web-ui is running on port 7860 and try again."
    exit 1
fi


docker compose down
docker compose up --build -d