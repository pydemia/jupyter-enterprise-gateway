# Quick Install: Single Machine using `docker`

See: https://github.com/jupyter-server/enterprise_gateway/tree/main/etc/docker/enterprise-gateway-demo

## Pre-requisite

```bash
cd jupyter-enterprise-gateway

docker pull elyra/nb2kg:2.4.0
docker pull elyra/enterprise-gateway:3.1.0
docker pull haproxy:alpine

mkdir -p test/notebooks

curl -fsSL https://raw.githubusercontent.com/jupyter-server/enterprise_gateway/main/etc/docker/docker-compose.yml -O

curl -fsSL https://raw.githubusercontent.com/jupyter-server/enterprise_gateway/main/etc/kernel-launchers/docker/scripts/launch_docker.py -O

# docker swarm init
# docker stack deploy -c docker-compose.yml enterprise-gateway
docker stack deploy -c docker-compose.yml
KG_PORT=18888 docker-compose up
```

```log
❯ KG_PORT=18888 docker-compose up
WARNING: Some services (enterprise-gateway) use the 'deploy' key, which will be ignored. Compose does not support 'deploy' configuration - use `docker stack deploy` to deploy to a swarm.
WARNING: The Docker Engine you're using is running in swarm mode.

Compose does not use swarm mode to deploy services to multiple nodes in a swarm. All containers will be scheduled on the current node.

To deploy your application across the swarm, use `docker stack deploy`.

Creating network "enterprise-gateway" with driver "overlay"
Pulling enterprise-gateway (elyra/enterprise-gateway:dev)...
dev: Pulling from elyra/enterprise-gateway
ea362f368469: Already exists
1c2cc406fa63: Already exists
669dbb3f6366: Already exists
3923fd8d3607: Already exists
d5da8a60f05b: Already exists
78722f61450a: Already exists
92fcb4043b45: Already exists
e43cca32fa72: Already exists
d6e059957f76: Already exists
d4c1ac4b2556: Already exists
662cec5dfc0c: Already exists
2c1cefff5d33: Already exists
759c927f13aa: Already exists
8df7585513a9: Pull complete
129b64da4b42: Pull complete
1309bb196b4c: Pull complete
4cb484abaaa3: Pull complete
56821db20a35: Pull complete
c16ef4d099ff: Pull complete
047fb5f8e159: Pull complete
cf6ce6deb444: Pull complete
c3b8d0e24467: Pull complete
1fca32465d06: Pull complete
Digest: sha256:829bf85cd094dd9bcdd5a507679ea7a06fd72626ae441356742e551cf5df8ea7
Status: Downloaded newer image for elyra/enterprise-gateway:dev
Pulling enterprise-gateway-proxy (haproxy:alpine)...
alpine: Pulling from library/haproxy
c158987b0551: Pull complete
66720c2ceff1: Pull complete
47baf2978954: Pull complete
bc9ebd673355: Pull complete
Digest: sha256:83a3495286ceaa3fa74ad06ff21f6300c9d32d3b0bbc09997a0e2cb56f48374a
Status: Downloaded newer image for haproxy:alpine
Creating scripts_enterprise-gateway_1       ... done
Creating scripts_enterprise-gateway-proxy_1 ... done
Attaching to scripts_enterprise-gateway_1, scripts_enterprise-gateway-proxy_1
enterprise-gateway_1        | Starting Jupyter Enterprise Gateway...
enterprise-gateway-proxy_1  | /bin/sh: can't create /usr/local/etc/haproxy/haproxy.cfg: Permission denied
enterprise-gateway-proxy_1  | /bin/sh: exec: line 50: /docker-entrypoint.sh: not found
scripts_enterprise-gateway-proxy_1 exited with code 127
enterprise-gateway_1        | [D 2022-12-20 09:29:57.119 EnterpriseGatewayApp] Searching ['/usr/local/bin', '/home/jovyan/.jupyter', '/home/jovyan/.local/etc/jupyter', '/opt/conda/etc/jupyter', '/usr/local/etc/jupyter', '/etc/jupyter'] for config files
enterprise-gateway_1        | [D 2022-12-20 09:29:57.119 EnterpriseGatewayApp] Looking for jupyter_config in /etc/jupyter
enterprise-gateway_1        | [D 2022-12-20 09:29:57.119 EnterpriseGatewayApp] Looking for jupyter_config in /usr/local/etc/jupyter
enterprise-gateway_1        | [D 2022-12-20 09:29:57.120 EnterpriseGatewayApp] Looking for jupyter_config in /opt/conda/etc/jupyter
enterprise-gateway_1        | [D 2022-12-20 09:29:57.120 EnterpriseGatewayApp] Looking for jupyter_config in /home/jovyan/.local/etc/jupyter
enterprise-gateway_1        | [D 2022-12-20 09:29:57.120 EnterpriseGatewayApp] Looking for jupyter_config in /home/jovyan/.jupyter
enterprise-gateway_1        | [D 2022-12-20 09:29:57.120 EnterpriseGatewayApp] Looking for jupyter_config in /usr/local/bin
enterprise-gateway_1        | [D 2022-12-20 09:29:57.122 EnterpriseGatewayApp] Looking for jupyter_enterprise_gateway_config in /etc/jupyter
enterprise-gateway_1        | [D 2022-12-20 09:29:57.122 EnterpriseGatewayApp] Looking for jupyter_enterprise_gateway_config in /usr/local/etc/jupyter
enterprise-gateway_1        | [D 2022-12-20 09:29:57.122 EnterpriseGatewayApp] Looking for jupyter_enterprise_gateway_config in /opt/conda/etc/jupyter
enterprise-gateway_1        | [D 2022-12-20 09:29:57.122 EnterpriseGatewayApp] Looking for jupyter_enterprise_gateway_config in /home/jovyan/.local/etc/jupyter
enterprise-gateway_1        | [D 2022-12-20 09:29:57.122 EnterpriseGatewayApp] Looking for jupyter_enterprise_gateway_config in /home/jovyan/.jupyter
enterprise-gateway_1        | [D 2022-12-20 09:29:57.122 EnterpriseGatewayApp] Looking for jupyter_enterprise_gateway_config in /usr/local/bin
enterprise-gateway_1        | [D 221220 09:29:57 selector_events:59] Using selector: EpollSelector
enterprise-gateway_1        | [I 2022-12-20 09:29:57.156 EnterpriseGatewayApp] Jupyter Enterprise Gateway 3.2.0.dev0 is available at http://0.0.0.0:8888
```

## Prepare an Enterprise Gateway Server

```bash
curl -fsSL https://raw.githubusercontent.com/jupyter-server/enterprise_gateway/main/etc/docker/docker-compose.yml -O
```

## Prepare a Client

```bash
EG_HOST_IP="127.0.0.1" EG_PORT="18888" \
docker run -t --rm \
  -e JUPYTER_GATEWAY_URL='http://<EG_HOST_IP>:<EG_PORT>' \
  -e JUPYTER_GATEWAY_HTTP_USER=guest \
  -e JUPYTER_GATEWAY_HTTP_PWD=guest-password \
  -e LOG_LEVEL=DEBUG \
  -p 8888:8888 \
  -v `pwd`/test/notebooks/:/tmp/notebooks \
  -w /tmp/notebooks \
  elyra/nb2kg:2.4.0
```

```log
Starting nb2kg against gateway:  http://localhost:8888
Nootbook port:  8888
Kernel user:  jovyan
/usr/local/bin/start-nb2kg.sh
/usr/local/bin/start-notebook.sh: ignoring /usr/local/bin/start-notebook.d/*

Container must be run with group "root" to update passwd file
Executing the command: jupyter notebook
[I 09:45:20.115 NotebookApp] Writing notebook server cookie secret to /home/jovyan/.local/share/jupyter/runtime/notebook_cookie_secret
[I 09:45:20.871 NotebookApp] JupyterLab extension loaded from /opt/conda/lib/python3.6/site-packages/jupyterlab
[I 09:45:20.871 NotebookApp] JupyterLab application directory is /opt/conda/share/jupyter/lab
[I 09:45:20.874 NotebookApp] Loaded nb2kg extension
[I 09:45:20.874 NotebookApp] Overriding handler URLSpec('/kernelspecs/(?P<kernel_name>[\\w\\.\\-%]+)/(?P<path>.*)$', <class 'nb2kg.handlers.KernelSpecResourceHandler'>, kwargs=None, name=None)
[I 09:45:20.874 NotebookApp] Overriding handler URLSpec('/api/kernelspecs/(?P<kernel_name>[\\w\\.\\-%]+)$', <class 'nb2kg.handlers.KernelSpecHandler'>, kwargs=None, name=None)
[I 09:45:20.874 NotebookApp] Overriding handler URLSpec('/api/kernelspecs$', <class 'nb2kg.handlers.MainKernelSpecHandler'>, kwargs=None, name=None)
[I 09:45:20.874 NotebookApp] Overriding handler URLSpec('/api/kernels/(?P<kernel_id>\\w+-\\w+-\\w+-\\w+-\\w+)/channels$', <class 'nb2kg.handlers.WebSocketChannelsHandler'>, kwargs=None, name=None)
[I 09:45:20.874 NotebookApp] Overriding handler URLSpec('/api/kernels/(?P<kernel_id>\\w+-\\w+-\\w+-\\w+-\\w+)/(?P<action>restart|interrupt)$', <class 'nb2kg.handlers.KernelActionHandler'>, kwargs=None, name=None)
[I 09:45:20.874 NotebookApp] Overriding handler URLSpec('/api/kernels/(?P<kernel_id>\\w+-\\w+-\\w+-\\w+-\\w+)$', <class 'nb2kg.handlers.KernelHandler'>, kwargs=None, name=None)
[I 09:45:20.874 NotebookApp] Overriding handler URLSpec('/api/kernels$', <class 'nb2kg.handlers.MainKernelHandler'>, kwargs=None, name=None)
[I 09:45:20.876 NotebookApp] Serving notebooks from local directory: /tmp/notebooks
[I 09:45:20.876 NotebookApp] The Jupyter Notebook is running at:
[I 09:45:20.876 NotebookApp] http://(237e05e67543 or 127.0.0.1):8888/?token=ddaf312ebc8083049dd3aef37e2630b991b6c496ac6755f8
[I 09:45:20.876 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 09:45:20.877 NotebookApp] 
    
    Copy/paste this URL into your browser when you connect for the first time,
    to login with a token:
        http://(237e05e67543 or 127.0.0.1):8888/?token=ddaf312ebc8083049dd3aef37e2630b991b6c496ac6755f8
```
