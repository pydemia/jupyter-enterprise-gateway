# pydemia/enterprise-gateway:3.1.0
FROM elyra/enterprise-gateway:3.1.0

USER root
COPY --chown=jovyan:users ./enterprise_gateway /tmp/enterprise_gateway

RUN pip install --no-cache-dir /tmp/enterprise_gateway && \
    chown jovyan:users /usr/local/bin/start-enterprise-gateway.sh && \
    chmod 0755 /usr/local/bin/start-enterprise-gateway.sh && \
    touch /usr/local/share/jupyter/enterprise-gateway.log && \
    cp -Trf /tmp/enterprise_gateway/etc/kernel-launchers/kubernetes/scripts /usr/local/share/jupyter/kernels/python_kubernetes/scripts && \
    chown -R jovyan:users /usr/local/share/jupyter /usr/local/bin/kernel-launchers && \
    chmod 0666 /usr/local/share/jupyter/enterprise-gateway.log && \
    rm -f /usr/local/bin/bootstrap-kernel.sh && \
    rm -rf /tmp/enterprise_gateway

USER jovyan
