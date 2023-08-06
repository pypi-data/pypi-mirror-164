<img align="right" alt=" " height="256px" src="docs/logo.png">
<img align="right" alt=" " width="200px" src="logo.png">

# Buffy

**Versioning caching kinda-proxy for decoupling external HTTP resources**

Maintainer: Tim Bleimehl

status: alpha  (WIP - **do not use productive yet**)

- [Buffy](#buffy)
  - [What is this?](#what-is-this)
  - [Features](#features)
  - [Quick Start Client](#quick-start-client)
  - [Quick Start Server](#quick-start-server)
    - [Requirements](#requirements)
    - [Server start](#server-start)
    - [Connecting the BuffyPyClient](#connecting-the-buffypyclient)


## What is this?

Buffy is a server/client framework to buffer/cache your http requests.  
Buffy decouples your dependency on external webservers that are not under your control.  
Buffy manages HTTP downloads in the background. 
You can ignore any issues with external webservers and just focus on your application.  
At the moment there is only a Python client but also a REST API for language agnostic use.

## Features

* Versioning of changing downloads
* Pre-cache long running downloads before you need them
* Dampen load on external servers - prevent `429 Too Many Requests` errors
* As a "smart" Downloader
    * Resume broken downloads
    * Retry corrupted downloads




At the moment there is only a python client library. But the server has a [REST API](./docs/openapi.json) that can be consumed from any coding language. You are welcome to write a client in your language.
## Quick Start Client

Lets have a small example how your Buffy client code could look like.

```python
from buffy.buffypyclient import BuffyPyClient

# connect to buffy server
c = BuffyPyClient(ssl=False)

# create a request
req = c.create_request(
    url="https://ftp.ncbi.nlm.nih.gov/pubmed/baseline/pubmed22n0003.xml.gz"
)

# save requested file
req.download_response_content_to(dir="/tmp")
```

This is all it takes to request a file. Next time the webserver at `ftp.ncbi.nlm.nih.go`  should be down the buffy client will just serve you the cached answer.
Should your Buffy server be down, the client will fall back to direct downloading the request from the source.

See the [documenation](BuffyPyClient-examples) for more detailed examples on how to use the client


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

### Connecting the BuffyPyClient

Create a python script. 

```python
# connect to buffy server
from buffy.buffypyclient import BuffyPyClient

# connect to buffy server
c = BuffyPyClient(host="localhost", port=8008, ssl=False)
```

See the [documenation](BuffyPyClient-examples) for more detailed examples on how to use the client