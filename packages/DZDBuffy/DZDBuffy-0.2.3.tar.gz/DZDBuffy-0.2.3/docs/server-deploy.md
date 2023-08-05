
!!!WIP DOCUMENT!!!
## Quick Start Server

### Requirements

* [Docker](https://docs.docker.com/engine/install/)
* [Docker-compose](https://docs.docker.com/compose/install/compose-plugin/)

### Server start

* Download the buffy docker-compose file 

```bash
wget -O docker-compose.yaml https://git.connect.dzd-ev.de/dzdpythonmodules/buffy/-/raw/main/docker-compose.yaml?inline=false
```

* Start the Buffy server with docker compose

```bash
docker-compose up -d
```