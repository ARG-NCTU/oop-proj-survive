#!/bin/bash

apt-get update
apt-get install -y alsa-utils libasound2 libasound2-dev x11-apps
apt-get clean
pip install --upgrade pip
pip install pymunk
