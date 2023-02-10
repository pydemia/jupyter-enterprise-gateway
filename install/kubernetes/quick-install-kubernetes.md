# Quick Install: Kubernetes(via `minikube`)

See: https://jupyter-enterprise-gateway.readthedocs.io/en/latest/operators/deploy-kubernetes.html

```bash
EG_VERSION=3.1.0
```

```bash
curl -fsSL "https://github.com/jupyter-server/enterprise_gateway/releases/download/v${EG_VERSION}/jupyter_enterprise_gateway_helm-${EG_VERSION}.tar.gz" \
  -o "enterprise_gateway_helmchart.tar.gz" && \
  tar -zxf "enterprise_gateway_helmchart.tar.gz"

```

```bash
kubectl create namespace enterprise-gateway

# cd git/enterprise_gateway
# helm  upgrade --install  enterprise-gateway \
#   etc/kubernetes/helm/enterprise-gateway \
#    --namespace enterprise-gateway

helm  upgrade --install  enterprise-gateway \
  "https://github.com/jupyter-server/enterprise_gateway/releases/download/v${EG_VERSION}/jupyter_enterprise_gateway_helm-${EG_VERSION}.tar.gz" \
   --namespace enterprise-gateway

helm  upgrade --install  enterprise-gateway \
  ./enterprise-gateway \
   --namespace enterprise-gateway \
   --values=custom-values.yaml
```

Then, Port-Forward `-n enterprise-gateway service/enterprise-gateway` (18888:8888)

```bash
./launch_client.sh
```