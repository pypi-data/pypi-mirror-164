FROM python:3.10

RUN mkdir -p /opt/buffy
RUN mkdir -p /data
WORKDIR /opt/buffy
ADD . /opt/buffy
ENV CONFIGS_STORAGE_BACKEND_CONFIG='{"file_storage_base_path": "/data","redis_connection_params": {"host":"redis"}}'
RUN pip3 install --no-cache-dir -e .
CMD [ "python3", "buffy/buffyserver/main.py" ]