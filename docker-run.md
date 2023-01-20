# Docker commands

```bash
docker run --rm -it \
  -p 8888:8888 \
  jupyter/datascience-notebook:latest \
  jupyter lab \
  --NotebookApp.ip=0.0.0.0 \
  --NotebookApp.open_browser=False \
  --NotebookApp.allow_remote_access=True \
  --NotebookApp.log_level=DEBUG \
  --NotebookApp.token=469d212e31badc2e3d1eb11f81d56c9302231897ee3f5941
```