#!/bin/zsh
# builds local docker image (needs docker to be running)
cp ./openastro.package/dist/** ./package.deployment/
app="open-astro-web-service"
docker build -t ${app} .
docker run -d -p 5050:5050 ${app}:latest
