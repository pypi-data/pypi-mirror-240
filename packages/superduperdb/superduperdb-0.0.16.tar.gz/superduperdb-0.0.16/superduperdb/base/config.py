"""
The classes in this file define the configuration variables for SuperDuperDB,
which means that this file gets imported before alost anything else, and
canot contain any other imports from this project.
"""
# TODO further simplify these configurations

import re
import typing as t
from enum import Enum

from .jsonable import Factory, JSONable


class Retry(JSONable):
    """Describes how to retry using the `tenacity` library

    :param stop_after_attempt: The number of attempts to make
    :param wait_max: The maximum time to wait between attempts
    :param wait_min: The minimum time to wait between attempts
    :param wait_multiplier: The multiplier for the wait time between attempts
    """

    # TODO - add this to an API mixin instead of project level config

    stop_after_attempt: int = 2
    wait_max: float = 10.0
    wait_min: float = 4.0
    wait_multiplier: float = 1.0


class Apis(JSONable):
    """A container for API connections

    :param retry: A ``Retry`` object
    """

    retry: Retry = Factory(Retry)


class Cluster(JSONable):
    """Describes a connection to distributed work via Dask

    :param distributed: Whether to use distributed task management via Dask or not
    :param deserializers: A list of deserializers
    :param serializers: A list of serializers
    :param dask_scheduler: The Dask scheduler URI
    :param local: Whether the connection is local
    """

    # TODO - none of these are actually used apart from `dask`
    distributed: bool = False
    deserializers: t.List[str] = Factory(list)
    serializers: t.List[str] = Factory(list)
    dask_scheduler: str = 'tcp://localhost:8786'
    local: bool = True
    backfill_batch_size: int = 100


class LogLevel(str, Enum):
    """Enumerate log severity level"""

    DEBUG = 'DEBUG'
    INFO = 'INFO'
    SUCCESS = "SUCCESS"
    WARN = 'WARN'
    ERROR = 'ERROR'


class LogType(str, Enum):
    """Enumerate the standard logs"""

    # SYSTEM uses the systems STDOUT and STDERR for printing the logs.
    # DEBUG, INFO, and WARN go to STDOUT.
    # ERROR goes to STDERR.
    SYSTEM = "SYSTEM"

    # LOKI a format that is compatible with the Loki Log aggregation system.
    LOKI = "LOKI"


class Logging(JSONable):
    """Describe how we are going to log. This isn't yet used.

    :param level: The log level
    :param type: The log type
    :param kwargs: Any additional keyword arguments
    """

    level: LogLevel = LogLevel.INFO
    type: LogType = LogType.SYSTEM
    kwargs: dict = Factory(dict)


class Server(JSONable):
    """Configure the SuperDuperDB server connection information

    :param host: The host for the connection
    :param port: The port for the connection
    :param protocol: The protocol for the connection
    """

    host: str = '127.0.0.1'
    port: int = 3223
    protocol: str = 'http'

    @property
    def uri(self) -> str:
        return f'{self.protocol}://{self.host}:{self.port}'


class Downloads(JSONable):
    """
    Configure how downloads are saved in the database
    or to hybrid filestorage (references to filesystem from datastore)

    :param hybrid: Whether hybrid is being used
    :param root: The root for the connection
    """

    hybrid: bool = False
    root: str = 'data/downloads'


class Config(JSONable):
    """The data class containing all configurable superduperdb values

    :param data_backend: The URI for the data backend
    :param vector_search: The configuration for the vector search {'in_memory', 'lance'}
    :param artifact_store: The URI for the artifact store
    :param metadata_store: The URI for the metadata store
    :param cluster: Settings distributed computing and change data capture
    :param apis: Settings for OPENAI and other APIs
    :param logging: Logging
    :param server: Settings for the experimental Rest server
    :param downloads: Settings for downloading files"""

    @property
    def self_hosted_vector_search(self) -> bool:
        return re.split('://|\+', self.data_backend)[0] == self.vector_search

    data_backend: str = 'mongodb://localhost:27017'

    #: The configuration for the vector search
    vector_search: 'str' = 'in_memory'  # "in_memory" / "lance"

    artifact_store: t.Optional[str] = None
    metadata_store: t.Optional[str] = None
    cluster: Cluster = Factory(Cluster)
    apis: Apis = Factory(Apis)
    logging: Logging = Factory(Logging)
    server: Server = Factory(Server)
    downloads: Downloads = Factory(Downloads)

    #: Probability of validation fold
    fold_probability: float = 0.05

    class Config(JSONable.Config):
        protected_namespaces = ()
