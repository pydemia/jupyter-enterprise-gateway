#!/bin/bash

EG_HOST_IP="127.0.0.1"
# EG_PORT="18888"
EG_PORT="18888"
KG_PORT="18888"

docker run -t --rm \
  -e JUPYTER_GATEWAY_URL='http://<EG_HOST_IP>:<EG_PORT>' \
  -e JUPYTER_GATEWAY_HTTP_USER=guest \
  -e JUPYTER_GATEWAY_HTTP_PWD=guest-password \
  -e LOG_LEVEL=DEBUG \
  -p 8888:8888 \
  -v `pwd`/../test/notebooks/:/tmp/notebooks \
  -w /tmp/notebooks \
  --network="enterprise-gateway" \
  elyra/nb2kg:2.4.0
