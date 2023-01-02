#!/bin/bash

#docker swarm init
EG_PORT=18888
KG_PORT=18888
#EG_DOCKER_MODE="swarm"
EG_DOCKER_MODE="docker"

docker-compose up
# echo `"$(cd "$(dirname "$1")" && pwd -P)$(basename "$1")"`
# echo "$(cd "$(dirname "$1")" && pwd -P)/$(basename "$1")"
