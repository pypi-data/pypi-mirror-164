
Versionized Caching Proxy for decoupling external responses
buffy

* Caching Proxy for external files and api calls
* versioning of files
* tagging of files (valid,failed)
	* Autofallback to valid files if current online file is tagged as "failed"
* stubborn downloader
	* But when threshold (timeout, n-times erros) is reached and old version is available server old version
* "Always use local cached version" option for certain files
* Server / Client Architecture


ToDo:

* Better server watchdog in buffy/buffyserver/main.py
* Propagate server download errors to client
* Janitour should only wipe cached version when there are no downlads running
  * client should/could set a "pin until"-attr and unset when finished?
  * Old version could be marked as old and be deleted next day?
* Add mkdoc build test to test job

Server Ideas:

* Auth on buffyserver
* unpack compresses file in background so client has an even easier life
* Review response data writing at buffyserver.backend.register_response_data_writing in future when your are a better coder or have the time to read into the issue
* make content serving endpoint byte serving capaple. Clients will be able rejoin broken downloads https://github.com/rvflorian/byte-serving-php
* Proxy interface  https://stackoverflow.com/questions/8287628/proxies-with-python-requests-module

Client Ideas:
* cache local fallback downloads in tmp dir


Errors to investigate

Martin:

```
Traceback (most recent call last):
  File "/Users/mpreusse/daten/consilia/kaiser_und_preusse/code/dzd/dataloading_pubtator/venv/lib/python3.9/site-packages/urllib3/connectionpool.py", line 449, in _make_request
    six.raise_from(e, None)
  File "<string>", line 3, in raise_from
  File "/Users/mpreusse/daten/consilia/kaiser_und_preusse/code/dzd/dataloading_pubtator/venv/lib/python3.9/site-packages/urllib3/connectionpool.py", line 444, in _make_request
    httplib_response = conn.getresponse()
  File "/Users/mpreusse/.pyenv/versions/3.9.9/lib/python3.9/http/client.py", line 1377, in getresponse
    response.begin()
  File "/Users/mpreusse/.pyenv/versions/3.9.9/lib/python3.9/http/client.py", line 320, in begin
    version, status, reason = self._read_status()
  File "/Users/mpreusse/.pyenv/versions/3.9.9/lib/python3.9/http/client.py", line 281, in _read_status
    line = str(self.fp.readline(_MAXLINE + 1), "iso-8859-1")
  File "/Users/mpreusse/.pyenv/versions/3.9.9/lib/python3.9/socket.py", line 704, in readinto
    return self._sock.recv_into(b)
socket.timeout: timed out

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/mpreusse/daten/consilia/kaiser_und_preusse/code/dzd/dataloading_pubtator/venv/lib/python3.9/site-packages/requests/adapters.py", line 489, in send
    resp = conn.urlopen(
  File "/Users/mpreusse/daten/consilia/kaiser_und_preusse/code/dzd/dataloading_pubtator/venv/lib/python3.9/site-packages/urllib3/connectionpool.py", line 787, in urlopen
    retries = retries.increment(
  File "/Users/mpreusse/daten/consilia/kaiser_und_preusse/code/dzd/dataloading_pubtator/venv/lib/python3.9/site-packages/urllib3/util/retry.py", line 550, in increment
    raise six.reraise(type(error), error, _stacktrace)
  File "/Users/mpreusse/daten/consilia/kaiser_und_preusse/code/dzd/dataloading_pubtator/venv/lib/python3.9/site-packages/urllib3/packages/six.py", line 770, in reraise
    raise value
  File "/Users/mpreusse/daten/consilia/kaiser_und_preusse/code/dzd/dataloading_pubtator/venv/lib/python3.9/site-packages/urllib3/connectionpool.py", line 703, in urlopen
    httplib_response = self._make_request(
  File "/Users/mpreusse/daten/consilia/kaiser_und_preusse/code/dzd/dataloading_pubtator/venv/lib/python3.9/site-packages/urllib3/connectionpool.py", line 451, in _make_request
    self._raise_timeout(err=e, url=url, timeout_value=read_timeout)
  File "/Users/mpreusse/daten/consilia/kaiser_und_preusse/code/dzd/dataloading_pubtator/venv/lib/python3.9/site-packages/urllib3/connectionpool.py", line 340, in _raise_timeout
    raise ReadTimeoutError(
urllib3.exceptions.ReadTimeoutError: HTTPConnectionPool(host='localhost', port=8008): Read timed out. (read timeout=3)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/mpreusse/daten/consilia/kaiser_und_preusse/code/dzd/dataloading_pubtator/main.py", line 38, in <module>
    req = c.create_request(url=f)
  File "/Users/mpreusse/daten/consilia/kaiser_und_preusse/code/dzd/dataloading_pubtator/venv/lib/python3.9/site-packages/buffy/buffypyclient/buffypyclient.py", line 423, in create_request
    req.order()
  File "/Users/mpreusse/daten/consilia/kaiser_und_preusse/code/dzd/dataloading_pubtator/venv/lib/python3.9/site-packages/buffy/buffypyclient/buffypyclient.py", line 93, in order
    res: requests.Response = requests.put(
  File "/Users/mpreusse/daten/consilia/kaiser_und_preusse/code/dzd/dataloading_pubtator/venv/lib/python3.9/site-packages/requests/api.py", line 130, in put
    return request("put", url, data=data, **kwargs)
  File "/Users/mpreusse/daten/consilia/kaiser_und_preusse/code/dzd/dataloading_pubtator/venv/lib/python3.9/site-packages/requests/api.py", line 59, in request
    return session.request(method=method, url=url, **kwargs)
  File "/Users/mpreusse/daten/consilia/kaiser_und_preusse/code/dzd/dataloading_pubtator/venv/lib/python3.9/site-packages/requests/sessions.py", line 587, in request
    resp = self.send(prep, **send_kwargs)
  File "/Users/mpreusse/daten/consilia/kaiser_und_preusse/code/dzd/dataloading_pubtator/venv/lib/python3.9/site-packages/requests/sessions.py", line 701, in send
    r = adapter.send(request, **kwargs)
  File "/Users/mpreusse/daten/consilia/kaiser_und_preusse/code/dzd/dataloading_pubtator/venv/lib/python3.9/site-packages/requests/adapters.py", line 578, in send
    raise ReadTimeout(e, request=request)
requests.exceptions.ReadTimeout: HTTPConnectionPool(host='localhost', port=8008): Read timed out. (read timeout=3)

Process finished with exit code 1
```
