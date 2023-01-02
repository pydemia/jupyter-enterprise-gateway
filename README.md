# jupyter-enterprise-gateway

This content is based on `enterprise_gateway==v3.1.0`.

See:
* Github: https://github.com/jupyter-server/enterprise_gateway
* Docs: https://jupyter-enterprise-gateway.readthedocs.io/en/latest/users/index.html

## Installation

1. Prepare a client: Jupyter Server(`jupyterlab`) or `jupyter notebook`
2. Prepare an Enterprise Gateway Server
3. Connect the client to the Enterprise Gateway


### Prepare a Jupyter Client

#### Install a Jupyter Client

`jupyter_client < 7.0.`
See: https://jupyter-enterprise-gateway.readthedocs.io/en/latest/operators/installing-eg.html#installing-enterprise-gateway-common

* `jupyterlab` 

```bash
pip install jupyter_server
```

* `jupyter notebook`

```bash
pip install notebook
```

* use a Docker Image

See: https://jupyter-enterprise-gateway.readthedocs.io/en/latest/users/connecting-to-eg.html#docker-image

```bash
docker pull elyra/nb2kg:2.4.0
```

```bash
docker run -t --rm \
  -e JUPYTER_GATEWAY_URL='http://<EG_HOST_IP>:<EG_PORT>' \
  -e JUPYTER_GATEWAY_HTTP_USER=guest \
  -e JUPYTER_GATEWAY_HTTP_PWD=guest-password \
  -e LOG_LEVEL=DEBUG \
  -p 8888:8888 \
  -v ${HOME}/notebooks/:/tmp/notebooks \
  -w /tmp/notebooks \
  elyra/nb2kg:2.4.0
```

### Prepare an Enterprise Gateway Server

See: https://jupyter-enterprise-gateway.readthedocs.io/en/latest/operators/index.html

#### Single(recommended: with Anaconda)

See: 
https://jupyter-enterprise-gateway.readthedocs.io/en/latest/operators/deploy-single.html
https://jupyter-enterprise-gateway.readthedocs.io/en/latest/operators/launching-eg.html

```bash
pip install --upgrade jupyter_enterprise_gateway

jupyter enterprisegateway --ip=0.0.0.0 --port_retries=0
```

Example: Kernelspec

```json
{
  "display_name": "Python 3 Local",
  "language": "python",
  "metadata": {
    "process_proxy": {
      "class_name": "enterprise_gateway.services.processproxies.processproxy.LocalProcessProxy"
    }
  },
  "argv": ["python", "-m", "ipykernel_launcher", "-f", "{connection_file}"]
}
```


* Example: `launch.sh`

```bash
#!/bin/bash

LOG=/var/log/enterprise_gateway.log
PIDFILE=/var/run/enterprise_gateway.pid

jupyter enterprisegateway --ip=0.0.0.0 --port_retries=0 --log-level=DEBUG --RemoteKernelManager.cull_idle_timeout=43200 --MappingKernelManager.cull_interval=60 > $LOG 2>&1 &
if [ "$?" -eq 0 ]; then
  echo $! > $PIDFILE
else
  exit 1
fi
```

#### Docker Compose

```bash
git clone https://github.com/jupyter-server/enterprise_gateway
cd enterprise_gateway/etc/docker

docker-compose up
```

#### Docker Swarm

```bash
git clone https://github.com/jupyter-server/enterprise_gateway
cd enterprise_gateway/etc/docker

docker stack deploy -c docker-compose.yml enterprise-gateway
```

#### Kubernetes

See: https://jupyter-enterprise-gateway.readthedocs.io/en/latest/operators/deploy-kubernetes.html

#### Python-Distributed

Supported Load Balancing Algorithms: `round-robin` or `least-connection`

See: https://jupyter-enterprise-gateway.readthedocs.io/en/latest/operators/deploy-distributed.html

#### Spark on Hadoop


#### Set a configuration on the client side

```bash
jupyter lab --gateway-url=http://<EG_HOST_IP>:<EG_PORT> --GatewayClient.http_user=guest --GatewayClient.http_pwd=guest-password
```

`jupyter_server_config.py` (via `jupyter server --generate-config`):

```py
c.GatewayClient.url = "http://<EG_HOST_IP>:<EG_PORT>"
c.GatewayClient.http_user = "guest"
c.GatewayClient.http_pwd = "guest-password"
```

Kernel Environment Variables:

See: https://jupyter-enterprise-gateway.readthedocs.io/en/latest/users/kernel-envs.html#kernel-environment-variables

```env
  KERNEL_GID=<from user> or 100
    Containers only. This value represents the group id in which the container will run.
    The default value is 100 representing the users group - which is how all kernel images
    produced by Enterprise Gateway are built.  See also KERNEL_UID.
    Kubernetes: Warning - If KERNEL_GID is set it is strongly recommened that feature-gate
    RunAsGroup be enabled, otherwise, this value will be ignored and the pod will run as
    the root group id.  As a result, the setting of this value into the Security Context
    of the kernel pod is commented out in the kernel-pod.yaml file and must be enabled
    by the administrator.
    Docker: Warning - This value is only added to the supplemental group ids.  As a result,
    if used with KERNEL_UID, the resulting container will run as the root group with this
    value listed in its supplemental groups.

  KERNEL_EXECUTOR_IMAGE=<from kernel.json process-proxy stanza> or KERNEL_IMAGE
    Kubernetees Spark only. This indicates the image that Spark on Kubernetes will use
    for the its executors.  Although this value could come from the user, its strongly
    recommended that the process-proxy stanza of the corresponding kernel's kernelspec
    (kernel.json) file be updated to include the image name.  If no image name is
    provided, the value of KERNEL_IMAGE will be used.

  KERNEL_EXTRA_SPARK_OPTS=<from user>
    Spark only. This variable allows users to add additional spark options to the
    current set of options specified in the corresponding kernel.json file.  This
    variable is purely optional with no default value.  In addition, it is the
    responsibility of the user setting this value to ensure the options passed
    are appropriate relative to the target environment.  Because this variable contains
    space-separate values, it requires appropriate quotation.  For example, to use with
    the notebook docker image jupyterhub/k8s-singleuser-sample , the environment variable would look something like
    this:

    docker run ... -e KERNEL_EXTRA_SPARK_OPTS=\"--conf spark.driver.memory=2g
    --conf spark.executor.memory=2g\" ... jupyterhub/k8s-singleuser-sample

  KERNEL_ID=<from user> or <system generated>
    This value represents the identifier used by the Jupyter framework to identify
    the kernel.  Although this value could be provided by the user, it is recommended
    that it be generated by the system.

  KERNEL_IMAGE=<from user> or <from kernel.json process-proxy stanza>
    Containers only. This indicates the image to use for the kernel in containerized
    environments - Kubernetes or Docker.  Although it can be provided by the user, it
    is strongly recommended that the process-proxy stanza of the corresponding kernel's
    kernelspec (kernel.json) file be updated to include the image name.

  KERNEL_LAUNCH_TIMEOUT=<from user> or EG_KERNEL_LAUNCH_TIMEOUT
    Indicates the time (in seconds) to allow for a kernel's launch.  This value should
    be submitted in the kernel startup if that particular kernel's startup time is
    expected to exceed that of the EG_KERNEL_LAUNCH_TIMEOUT set when Enterprise
    Gateway starts.

  KERNEL_NAMESPACE=<from user> or KERNEL_POD_NAME or EG_NAMESPACE
    Kubernetes only.  This indicates the name of the namespace to use or create on
    Kubernetes in which the kernel pod will be located.  For users wishing to use a
    pre-created namespace, this value should be submitted in the kernel startup
    request.  In such cases, the user must also provide KERNEL_SERVICE_ACCOUNT_NAME.
    If not provided, Enterprise Gateway will create a new namespace for the kernel
    whose value is derived from KERNEL_POD_NAME.  In rare cases where
    EG_SHARED_NAMESPACE is True, this value will be set to the value of EG_NAMESPACE.

    Note that if the namespace is created by Enterprise Gateway, it will be removed
    upon the kernel's termination.  Otherwise, the Enterprise Gateway will not
    remove the namespace.

  KERNEL_POD_NAME=<from user> or KERNEL_USERNAME-KERNEL_ID
    Kubernetes only. By default, Enterprise Gateway will use a kernel pod name whose
    value is derived from KERNEL_USERNAME and KERNEL_ID separated by a hyphen
    ('-').  This variable is typically NOT provided by the user, but, in such
    cases, Enterprise Gateway will honor that value.  However, when provided,
    it is the user's responsibility that KERNEL_POD_NAME is unique relative to
    any pods in the target namespace.  In addition, the pod must NOT exist -
    unlike the case if KERNEL_NAMESPACE is provided.

  KERNEL_REMOTE_HOST=<remote host name>
    DistributedProcessProxy only.  When specified, this value will override the
    configured load-balancing algorithm.

  KERNEL_SERVICE_ACCOUNT_NAME=<from user> or EG_DEFAULT_KERNEL_SERVICE_ACCOUNT_NAME
    Kubernetes only.  This value represents the name of the service account that
    Enterprise Gateway should equate with the kernel pod.  If Enterprise Gateway
    creates the kernel's namespace, it will be associated with the cluster role
    identified by EG_KERNEL_CLUSTER_ROLE.  If not provided, it will be derived
    from EG_DEFAULT_KERNEL_SERVICE_ACCOUNT_NAME.

  KERNEL_SPARKAPP_CONFIG_MAP=<from user> or None
    Spark k8s-operator only. The name of a Kubernetes ConfigMap which will be used to configure
    the SparkApplication. See the SparkApplicationSpec
    (https://googlecloudplatform.github.io/spark-on-k8s-operator/docs/api-docs.html#sparkoperator.k8s.io/v1beta2.SparkApplicationSpec)
    sparkConfigMap for more information.

  KERNEL_UID=<from user> or 1000
    Containers only. This value represents the user id in which the container will run.
    The default value is 1000 representing the jovyan user - which is how all kernel images
    produced by Enterprise Gateway are built.  See also KERNEL_GID.
    Kubernetes: Warning - If KERNEL_UID is set it is strongly recommened that feature-gate
    RunAsGroup be enabled and KERNEL_GID also be set, otherwise, the pod will run as
    the root group id. As a result, the setting of this value into the Security Context
    of the kernel pod is commented out in the kernel-pod.yaml file and must be enabled
    by the administrator.

  KERNEL_USERNAME=<from user> or <enterprise-gateway-user>
    This value represents the logical name of the user submitting the request to
    start the kernel. Of all the KERNEL_ variables, KERNEL_USERNAME is the one that
    should be submitted in the request. In environments in which impersonation is
    used it represents the target of the impersonation.

  KERNEL_WORKING_DIR=<from user> or None
    Containers only.  This value should model the directory in which the active
    notebook file is running.   It is intended to be used in conjunction with appropriate volume
    mounts in the kernel container such that the user's notebook filesystem exists
    in the container and enables the sharing of resources used within the notebook.
    As a result, the primary use case for this is for Jupyter Hub users running in
    Kubernetes.  When a value is provided and EG_MIRROR_WORKING_DIRS=True, Enterprise
    Gateway will set the container's working directory to the value specified in
    KERNEL_WORKING_DIR.  If EG_MIRROR_WORKING_DIRS is False, KERNEL_WORKING_DIR will
    not be available for use during the kernel's launch.  See also EG_MIRROR_WORKING_DIRS.
```