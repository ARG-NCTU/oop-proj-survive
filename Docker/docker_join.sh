#!/usr/bin/env bash

BASH_OPTION=bash

REPO_NAME="brian247/aoop2024"
TAG="survive"
IMG="${REPO_NAME}:${TAG}"

xhost +
containerid=$(docker ps -aqf "ancestor=${IMG}") && echo $containerid
docker exec -it \
    --privileged \
    -e DISPLAY=${DISPLAY} \
    -e LINES="$(tput lines)" \
    ${containerid} \
    $BASH_OPTION
xhost -