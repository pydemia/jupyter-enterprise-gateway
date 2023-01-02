#!/bin/bash

#./launch_client.sh localhost 18888 8888

EG_HOST_IP="${1:-localhost}"
EG_PORT="${2:-18888}"
KG_PORT="${EG_PORT}"
JUPYTER_PORT="${3:-8888}"

# docker run -t --rm \
#   -e JUPYTER_GATEWAY_URL="http://${EG_HOST_IP}:${EG_PORT}" \
#   -e JUPYTER_GATEWAY_HTTP_USER=guest \
#   -e JUPYTER_GATEWAY_HTTP_PWD=guest-password \
#   -e LOG_LEVEL=DEBUG \
#   -p 8888:8888 \
#   -v `pwd`/../test/notebooks/:/tmp/notebooks \
#   -w /tmp/notebooks \
#   --network="enterprise-gateway" \
#   elyra/nb2kg:2.4.0

# # docker run -t --rm \
# #   -e JUPYTER_GATEWAY_URL="http://${EG_HOST_IP}:${EG_PORT}" \
# #   -e LOG_LEVEL=DEBUG \
# #   -p 8888:8888 \
# #   -v `pwd`/../test/notebooks/:/tmp/notebooks \
# #   -w /tmp/notebooks \
# #   --network="enterprise-gateway" \
# #   elyra/nb2kg:2.4.0

# docker run -t --rm \
#   -e JUPYTER_GATEWAY_URL="http://${EG_HOST_IP}:${EG_PORT}" \
#   -e JUPYTER_GATEWAY_HTTP_USER=guest \
#   -e JUPYTER_GATEWAY_HTTP_PWD=guest-password \
#   -e LOG_LEVEL=DEBUG \
#   -p 8888:8888 \
#   -v `pwd`/../test/notebooks/:/tmp/notebooks \
#   -w /tmp/notebooks \
#   elyra/nb2kg:2.4.0


# docker run -t --rm \
#   -e JUPYTER_GATEWAY_URL="http://${EG_HOST_IP}:${EG_PORT}" \
#   -e JUPYTER_GATEWAY_HTTP_USER=guest \
#   -e JUPYTER_GATEWAY_HTTP_PWD=guest-password \
#   -e LOG_LEVEL=DEBUG \
#   -p 8888:8888 \
#   -v `pwd`/../test/notebooks/:/tmp/notebooks \
#   -w /tmp/notebooks \
#   jupyter/minimal-notebook:latest


# #Docker > v20.x
# # docker run -t --rm \
# #   --add-host=host.docker.internal:host-gateway \
# #   -p 8888:8888 \
# #   -v `pwd`/../test/notebooks/:/tmp/notebooks \
# #   -w /tmp/notebooks \
# #   jupyter/minimal-notebook:latest \
# #   start-notebook.sh \
# #   --gateway-url="http://${EG_HOST_IP}:${EG_PORT}" \
# #   --GatewayClient.http_user=guest \
# #   --GatewayClient.http_pwd=guest-password \
# #   --log-level=DEBUG

# docker run -t --rm \
#   -p 8888:8888 \
#   -v `pwd`/../test/notebooks/:/tmp/notebooks \
#   -w /tmp/notebooks \
#   jupyter/minimal-notebook:latest \
#   start-notebook.sh \
#   --gateway-url='http://host.docker.internal:18888' \
#   --GatewayClient.http_user=guest \
#   --GatewayClient.http_pwd=guest-password \
#   --log-level=DEBUG



jupyter lab \
  --gateway-url="http://${EG_HOST_IP}:${EG_PORT}"
  --GatewayClient.http_user=guest \
  --GatewayClient.http_pwd=guest-password \
  --ip=0.0.0.0 \
  --port="${JUPYTER_PORT}"
