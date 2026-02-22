# async-logger-k8s-talos

An Asynchronous Python microservice deployed on a Talos Kubernetes cluster.

**Environment Setup:** Requires VirtualBox, Talos Linux ISO, and Docker Desktop.

### 1. Build & Push Image:
```bash
docker build -t async-logger:v1 .
docker tag async-logger:v1 YOUR_DOCKER_USERNAME/async-logger:v1
docker push YOUR_DOCKER_USERNAME/async-logger:v1
```
### 2. Deploy to Talos Cluster:
```bash
./kubectl apply -f /root/namespace.yaml
./kubectl apply -f /root/deployment.yaml
./kubectl apply -f /root/service.yaml
```

### 3. Port Forwarding for Testing:
```bash
./kubectl -n async-logger port-forward svc/async-logger-svc 8080:8080 --address 0.0.0.0
```

### 4. Troubleshooting:
Includes a section for debugging failed port-forwards, Docker push errors, and unreachable Talos nodes.
