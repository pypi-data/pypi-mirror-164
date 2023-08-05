import hashlib
import typing
import inspect
from typing import Dict, Optional, Literal, Union, Type, List
from pydantic import BaseModel, Field
import datetime
import enum
from buffy.buffyserver.api.v1.models_recaching_strategies import ReCachingStrategy
import json

SUPPORTED_HASH_TYPES = typing.Literal[tuple(hashlib.algorithms_guaranteed)]
AVAILABLE_RECHACHING_STRATEGIES = typing.Union[tuple(ReCachingStrategy.list())]
# print("AVAILABLE_RECHACHING_STRATEGIES", AVAILABLE_RECHACHING_STRATEGIES)
# RECACHING_STRATEGIES = typing.Literal[tuple(ReCachingStrategy.str_list())]


class RequestCacheConfiguration(BaseModel):
    """The request cache configuration can be attached to a request to give Buffy server instruction how and when to cache a request.
    At the heart of the configuration is a [ReCachingStrategy](BuffyReCachingStrategies). the other option is how many versions of a request-response should be cached.

    **HINT**: This is pydantic model. Every `class-attribute` is also a `parameter`

    **example usage**
    ```python
    import json
    from buffy.buffypyclient import BuffyPyClient
    c = BuffyPyClient()

    # Define a strategy. Buffy server has to re-cache the target url every 3601 seconds.
    strategy = ReCachingStrategy.age(seconds=3601)
    # Lets pack the strategy in a RequestCacheConfiguration config
    config = RequestCacheConfiguration(recaching_strategy=strategy, max_cached_versions=3)
    # Lets attach the config to our request
    req = c.create_request("https://wikipedia.org",cache_configuration=config)
    ```
    """

    request_id: Optional[str]

    # recaching_strategy: Union[ReCachingStrategy.never, ReCachingStrategy.age] = Field(
    #    discriminator="strategy_name"
    # )
    # d = {"propertyName": "strategy_name"}
    recaching_strategy: AVAILABLE_RECHACHING_STRATEGIES = Field(
        default=ReCachingStrategy.never(),
        discriminator="strategy_name",
    )
    """A [strategy](/BuffyReCachingStrategies) instructs buffy how to cache request-responses. (e.b. by age of the cached file, or regulary by a cron job,...)"""
    max_cached_versions: int = 2
    """When more than `max_cached_versions` request-responses are cached by the Buffy server, any older cached version will be deleted."""

    # To be implemented later # unpack_response: bool = False


class Request_in(BaseModel):
    url: str
    http_method: Literal["get", "post", "put"] = "get"
    http_header_fields: Optional[Dict] = {}

    # https://docs.python-requests.org/en/latest/user/quickstart/#passing-parameters-in-urls
    http_query_params: Optional[Dict] = {}
    http_request_body: Optional[Dict] = {}
    group_name: Optional[str] = "DEFAULT_GROUP"
    description: Optional[str] = None
    documentation_link: Optional[str] = None
    validation_hash_type: Optional[SUPPORTED_HASH_TYPES] = "md5"
    cache_configuration: Optional[RequestCacheConfiguration] = None

    @property
    def signature(self) -> int:
        return hash(
            (
                self.url,
                self.http_method,
                json.dumps(self.http_header_fields),
                json.dumps(self.http_query_params),
                json.dumps(self.http_request_body),
                self.group_name,
            )
        )


class Request(Request_in):
    id: Optional[str]
    inital_request_datetime_utc: datetime.datetime = None
    latest_request_datetime_utc: Optional[datetime.datetime] = None
    latest_request_is_processed: bool = None
    cache_configuration: RequestCacheConfiguration

    @classmethod
    def from_request_in(cls, request_in: Request_in) -> "Request":
        if request_in.cache_configuration is None:
            request_in.cache_configuration = RequestCacheConfiguration()
        return cls(**request_in.dict())


class ResponseContentAttributes(BaseModel):
    media_type: Optional[str] = None
    etag: Optional[str] = None
    content_size_bytes: Optional[int] = None
    last_modified_datetime_utc: Optional[datetime.datetime] = None
    filename: Optional[str] = None
    content_disposition: Optional[str] = None

    def is_empty(self):
        return not all(dict(self).values())


class ResponseDownloadStats(BaseModel):
    """Statistics about the running or finished download of remote HTTP resource

    **HINT**: This is pydantic model. Every `class-attribute` is also a `parameter`
    """

    downloaded_bytes: int = 0
    """How many bytes are allready downloaded"""
    avg_bytes_per_sec: int = None
    """The average download speed."""
    download_running_duration_sec: float = None
    """How long is the download or running or how long did it run when finished."""
    download_start_time_unix_ts: float = None
    """The moment when the Buffy server started the download"""
    total_bytes_to_download: int = None
    """The size of the response content. This value can initaly be unrealiable if the remote webserver reported a wrong value, but will be realiable correct when the download is finished."""
    state: Literal["init", "downloading", "failed", "finished"]
    """State of the download. if `failed` there will be Stacktrace in `error`"""
    error: str = None
    """Stacktrace if download failed"""


class Response(BaseModel):
    """Metadata object for a request response.

    **HINT**: This is pydantic model. Every `class-attribute` is also a `parameter`
    """

    id: str = None
    request_id: str
    version: str
    """A compact date string, declarating the versions name"""
    previous_version: Optional[str] = None
    """If there is a predating version, you can find the version name here"""
    next_version: Optional[str] = None
    """If there is a newer version, you can find the version name here"""
    status: Literal["wait", "in_progress", "ready", "failed"]
    """State of the reponses download on Buffy server side"""
    content_download_path: Optional[str] = None
    """Path to downlaod the responses content from the Buffy server API. No base domain included!"""
    cached_datetime_utc: Optional[datetime.datetime] = None
    """Moment when Buffy server finished the download"""
    request_datetime_utc: Optional[datetime.datetime] = None
    """Moment when a client requested the file. This is not appliable to all strategies."""
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Disposition
    pinned: Optional[bool] = False
    """!WIP!: A pinned response will not be deleted by the garbage collector if `Request.cache_configuration.max_cached_versions` is reached."""
    tags: Optional[List[str]] = None
    """!EXPERIMENTAL!: Clients can add tags to a reponse to manage multiple versions"""
    valid: Optional[bool] = None
    """!OBSOLETE!: Will be replaced by `tags`"""
    download_stats: ResponseDownloadStats = None
    """Statistics about the downlaod by Buffy server"""
    content_attributes: ResponseContentAttributes = None
    """Attributes the download could gather about the content. mostly based on HTTP headers"""
    content_hash_hex: str = None
    """A hex hash of the response content. The hash alg is defined in `Request.validation_hash_type`"""
