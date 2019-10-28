# Jupyter Enterprise Gateway On Kubernetes

```sh
#docker tag [SOURCE_IMAGE] [HOSTNAME]/[PROJECT-ID]/[IMAGE]
docker tag elyra/enterprise-gateway:2.0.0 us.gcr.io/ultra-badge-233601/jeg:2.0.0
docker push us.gcr.io/ultra-badge-233601/jeg:2.0.0
```


```sh
export KG_URL=http://<ENTERPRISE_GATEWAY_HOST_IP>:8888
export KG_HTTP_USER=guest
export KG_HTTP_PASS=guest-password
export KERNEL_USERNAME=${KG_HTTP_USER}
jupyter notebook \
  --NotebookApp.session_manager_class=nb2kg.managers.SessionManager \
  --NotebookApp.kernel_manager_class=nb2kg.managers.RemoteKernelManager \
  --NotebookApp.kernel_spec_manager_class=nb2kg.managers.RemoteKernelSpecManager
```

```sh
export KG_URL=http://0.0.0.0:8888
export KG_HTTP_USER=guest
export KG_HTTP_PASS=guest-password
export KERNEL_USERNAME=${KG_HTTP_USER}
jupyter notebook \
  --NotebookApp.session_manager_class=nb2kg.managers.SessionManager \
  --NotebookApp.kernel_manager_class=nb2kg.managers.RemoteKernelManager \
  --NotebookApp.kernel_spec_manager_class=nb2kg.managers.RemoteKernelSpecManager
```


```sh
jupyter notebook \
 --gateway-url=http://<ENTERPRISE_GATEWAY_HOST_IP>:8888
 --GatewayClient.http_user=guest
 --GatewayClient.http_pwd=guest-password

jupyter notebook \
 --ip=0.0.0.0 \
 --port=8888 \
 --gateway-url=http://0.0.0.0:8888 \
 --GatewayClient.http_user=test \
 --GatewayClient.http_pwd=test 
```
