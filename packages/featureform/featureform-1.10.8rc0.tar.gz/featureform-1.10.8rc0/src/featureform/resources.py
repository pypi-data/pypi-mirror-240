# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import sys
import os
import json
import time
import base64
from abc import ABC
from enum import Enum
from typeguard import typechecked
from typing import List, Tuple, Union, Optional, Dict

import dill
import grpc
from .sqlite_metadata import SQLiteMetadata
from google.protobuf.duration_pb2 import Duration

from featureform.proto import metadata_pb2 as pb
from dataclasses import dataclass, field
from .version import check_up_to_date
from .exceptions import *
from .enums import *

NameVariant = Tuple[str, str]

# Constants for Pyspark Versions
MAJOR_VERSION = "3"
MINOR_VERSIONS = ["7", "8", "9", "10", "11"]


@typechecked
def valid_name_variant(nvar: NameVariant) -> bool:
    return nvar[0] != "" and nvar[1] != ""


@typechecked
@dataclass
class Schedule:
    name: str
    variant: str
    resource_type: int
    schedule_string: str

    @staticmethod
    def operation_type() -> OperationType:
        return OperationType.CREATE

    def type(self) -> str:
        return "schedule"

    def _create(self, stub) -> None:
        serialized = pb.SetScheduleChangeRequest(
            resource=pb.ResourceId(
                pb.NameVariant(name=self.name, variant=self.variant),
                resource_type=self.resource_type,
            ),
            schedule=self.schedule_string,
        )
        stub.RequestScheduleChange(serialized)


@typechecked
@dataclass
class RedisConfig:
    host: str
    port: int
    password: str
    db: int

    def software(self) -> str:
        return "redis"

    def type(self) -> str:
        return "REDIS_ONLINE"

    def serialize(self) -> bytes:
        config = {
            "Addr": f"{self.host}:{self.port}",
            "Password": self.password,
            "DB": self.db,
        }
        return bytes(json.dumps(config), "utf-8")


@typechecked
@dataclass
class PineconeConfig:
    project_id: str = ""
    environment: str = ""
    api_key: str = ""

    def software(self) -> str:
        return "pinecone"

    def type(self) -> str:
        return "PINECONE_ONLINE"

    def serialize(self) -> bytes:
        config = {
            "ProjectID": self.project_id,
            "Environment": self.environment,
            "ApiKey": self.api_key,
        }
        return bytes(json.dumps(config), "utf-8")

    def deserialize(self, config):
        config = json.loads(config)
        self.project_id = config["ProjectID"]
        self.environment = config["Environment"]
        self.api_key = config["ApiKey"]
        return self


@typechecked
@dataclass
class WeaviateConfig:
    url: str = ""
    api_key: str = ""

    def software(self) -> str:
        return "weaviate"

    def type(self) -> str:
        return "WEAVIATE_ONLINE"

    def serialize(self) -> bytes:
        if self.url == "":
            raise Exception("URL cannot be empty")
        config = {
            "URL": self.url,
            "ApiKey": self.api_key,
        }
        return bytes(json.dumps(config), "utf-8")

    def deserialize(self, config):
        config = json.loads(config)
        self.url = config["URL"]
        self.api_key = config["ApiKey"]
        return self


@typechecked
@dataclass
class AWSCredentials:
    def __init__(
        self,
        access_key: str,
        secret_key: str,
    ):
        """

        Credentials for an AWS.

        **Example**
        ```
        aws_credentials = ff.AWSCredentials(
            access_key="<AWS_ACCESS_KEY>",
            secret_key="<AWS_SECRET_KEY>"
        )
        ```

        Args:
            access_key (str): AWS Access Key.
            secret_key (str): AWS Secret Key.
        """
        if access_key == "":
            raise Exception("'AWSCredentials' access_key cannot be empty")

        if secret_key == "":
            raise Exception("'AWSCredentials' secret_key cannot be empty")

        self.access_key = access_key
        self.secret_key = secret_key

    def type(self):
        return "AWS_CREDENTIALS"

    def config(self):
        return {
            "AWSAccessKeyId": self.access_key,
            "AWSSecretKey": self.secret_key,
        }


@typechecked
@dataclass
class GCPCredentials:
    def __init__(
        self,
        project_id: str,
        credentials_path: str,
    ):
        """

        Credentials for an GCP.

        **Example**
        ```
        gcp_credentials = ff.GCPCredentials(
            project_id="<project_id>",
            credentials_path="<path_to_credentials>"
        )
        ```

        Args:
            project_id (str): The project id.
            credentials_path (str): The path to the credentials file.
        """
        if project_id == "":
            raise Exception("'GCPCredentials' project_id cannot be empty")

        if credentials_path == "":
            raise Exception("'GCPCredentials' credentials_path cannot be empty")

        if not os.path.isfile(credentials_path):
            raise Exception(
                f"'GCPCredentials' credentials_path '{credentials_path}' file not found"
            )

        self.project_id = project_id
        with open(credentials_path) as f:
            self.credentials = json.load(f)

    def type(self):
        return "GCPCredentials"

    def config(self):
        return {
            "ProjectId": self.project_id,
            "JSON": self.credentials,
        }

    def to_json(self):
        return self.credentials


@typechecked
@dataclass
class GCSFileStoreConfig:
    credentials: GCPCredentials
    bucket_name: str
    bucket_path: str = ""

    def software(self) -> str:
        return "gcs"

    def type(self) -> str:
        return "GCS"

    def serialize(self) -> bytes:
        config = {
            "BucketName": self.bucket_name,
            "BucketPath": self.bucket_path,
            "Credentials": self.credentials.config(),
        }
        return bytes(json.dumps(config), "utf-8")

    def config(self):
        return {
            "BucketName": self.bucket_name,
            "BucketPath": self.bucket_path,
            "Credentials": self.credentials.config(),
        }

    def store_type(self):
        return self.type()


@typechecked
@dataclass
class AzureFileStoreConfig:
    account_name: str
    account_key: str
    container_name: str
    root_path: str

    def software(self) -> str:
        return "azure"

    def type(self) -> str:
        return "AZURE"

    def serialize(self) -> bytes:
        config = {
            "AccountName": self.account_name,
            "AccountKey": self.account_key,
            "ContainerName": self.container_name,
            "Path": self.root_path,
        }
        return bytes(json.dumps(config), "utf-8")

    def config(self):
        return {
            "AccountName": self.account_name,
            "AccountKey": self.account_key,
            "ContainerName": self.container_name,
            "Path": self.root_path,
        }

    def store_type(self):
        return self.type()


@typechecked
@dataclass
class S3StoreConfig:
    def __init__(
        self,
        bucket_path: str,
        bucket_region: str,
        credentials: AWSCredentials,
        path: str = "",
    ):
        bucket_path_ends_with_slash = len(bucket_path) != 0 and bucket_path[-1] == "/"

        if bucket_path_ends_with_slash:
            raise Exception("The 'bucket_path' cannot end with '/'.")

        self.bucket_path = bucket_path
        self.bucket_region = bucket_region
        self.credentials = credentials
        self.path = path

    def software(self) -> str:
        return "S3"

    def type(self) -> str:
        return "S3"

    def serialize(self) -> bytes:
        config = self.config()
        return bytes(json.dumps(config), "utf-8")

    def config(self):
        return {
            "Credentials": self.credentials.config(),
            "BucketRegion": self.bucket_region,
            "BucketPath": self.bucket_path,
            "Path": self.path,
        }

    def store_type(self):
        return self.type()


@typechecked
@dataclass
class HDFSConfig:
    def __init__(self, host: str, port: str, path: str, username: str):
        bucket_path_ends_with_slash = len(path) != 0 and path[-1] == "/"

        if bucket_path_ends_with_slash:
            raise Exception("The 'bucket_path' cannot end with '/'.")

        self.path = path
        self.host = host
        self.port = port
        self.username = username

    def software(self) -> str:
        return "HDFS"

    def type(self) -> str:
        return "HDFS"

    def serialize(self) -> bytes:
        config = {
            "Host": self.host,
            "Port": self.port,
            "Path": self.path,
            "Username": self.username,
        }
        return bytes(json.dumps(config), "utf-8")

    def config(self):
        return {
            "Host": self.host,
            "Port": self.port,
            "Path": self.path,
            "Username": self.username,
        }

    def store_type(self):
        return self.type()


@typechecked
@dataclass
class OnlineBlobConfig:
    store_type: str
    store_config: dict

    def software(self) -> str:
        return self.store_type

    def type(self) -> str:
        return "BLOB_ONLINE"

    def config(self):
        return self.store_config

    def serialize(self) -> bytes:
        config = {
            "Type": self.store_type,
            "Config": self.store_config,
        }
        return bytes(json.dumps(config), "utf-8")


@typechecked
@dataclass
class FirestoreConfig:
    collection: str
    project_id: str
    credentials: GCPCredentials

    def software(self) -> str:
        return "firestore"

    def type(self) -> str:
        return "FIRESTORE_ONLINE"

    def serialize(self) -> bytes:
        config = {
            "Collection": self.collection,
            "ProjectID": self.project_id,
            "Credentials": self.credentials.to_json(),
        }
        return bytes(json.dumps(config), "utf-8")


@typechecked
@dataclass
class CassandraConfig:
    keyspace: str
    host: str
    port: int
    username: str
    password: str
    consistency: str
    replication: int

    def software(self) -> str:
        return "cassandra"

    def type(self) -> str:
        return "CASSANDRA_ONLINE"

    def serialize(self) -> bytes:
        config = {
            "Keyspace": self.keyspace,
            "Addr": f"{self.host}:{self.port}",
            "Username": self.username,
            "Password": self.password,
            "Consistency": self.consistency,
            "Replication": self.replication,
        }
        return bytes(json.dumps(config), "utf-8")


@typechecked
@dataclass
class DynamodbConfig:
    region: str
    access_key: str
    secret_key: str

    def software(self) -> str:
        return "dynamodb"

    def type(self) -> str:
        return "DYNAMODB_ONLINE"

    def serialize(self) -> bytes:
        config = {
            "Region": self.region,
            "AccessKey": self.access_key,
            "SecretKey": self.secret_key,
        }
        return bytes(json.dumps(config), "utf-8")


@typechecked
@dataclass
class MongoDBConfig:
    username: str
    password: str
    host: str
    port: str
    database: str
    throughput: int

    def software(self) -> str:
        return "mongodb"

    def type(self) -> str:
        return "MONGODB_ONLINE"

    def serialize(self) -> bytes:
        config = {
            "Username": self.username,
            "Password": self.password,
            "Host": self.host,
            "Port": self.port,
            "Database": self.database,
            "Throughput": self.throughput,
        }
        return bytes(json.dumps(config), "utf-8")


@typechecked
@dataclass
class SnowflakeConfig:
    username: str
    password: str
    schema: str
    account: str = ""
    organization: str = ""
    database: str = ""
    account_locator: str = ""
    warehouse: str = ""
    role: str = ""

    def __post_init__(self):
        if self.__has_legacy_credentials() and self.__has_current_credentials():
            raise ValueError(
                "Cannot create configure Snowflake with both current and legacy credentials"
            )

        if not self.__has_legacy_credentials() and not self.__has_current_credentials():
            raise ValueError("Cannot create configure Snowflake without credentials")

    def __has_legacy_credentials(self) -> bool:
        return self.account_locator != ""

    def __has_current_credentials(self) -> bool:
        if (self.account != "" and self.organization == "") or (
            self.account == "" and self.organization != ""
        ):
            raise ValueError("Both Snowflake organization and account must be included")
        elif self.account != "" and self.organization != "":
            return True
        else:
            return False

    def software(self) -> str:
        return "Snowflake"

    def type(self) -> str:
        return "SNOWFLAKE_OFFLINE"

    def serialize(self) -> bytes:
        config = {
            "Username": self.username,
            "Password": self.password,
            "Organization": self.organization,
            "AccountLocator": self.account_locator,
            "Account": self.account,
            "Schema": self.schema,
            "Database": self.database,
            "Warehouse": self.warehouse,
            "Role": self.role,
        }
        return bytes(json.dumps(config), "utf-8")


@typechecked
@dataclass
class PostgresConfig:
    host: str
    port: str
    database: str
    user: str
    password: str
    sslmode: str

    def software(self) -> str:
        return "postgres"

    def type(self) -> str:
        return "POSTGRES_OFFLINE"

    def serialize(self) -> bytes:
        config = {
            "Host": self.host,
            "Port": self.port,
            "Username": self.user,
            "Password": self.password,
            "Database": self.database,
            "SSLMode": self.sslmode,
        }
        return bytes(json.dumps(config), "utf-8")


@typechecked
@dataclass
class RedshiftConfig:
    host: str
    port: int
    database: str
    user: str
    password: str

    def software(self) -> str:
        return "redshift"

    def type(self) -> str:
        return "REDSHIFT_OFFLINE"

    def serialize(self) -> bytes:
        config = {
            "Host": self.host,
            "Port": str(self.port),
            "Username": self.user,
            "Password": self.password,
            "Database": self.database,
        }
        return bytes(json.dumps(config), "utf-8")


@typechecked
@dataclass
class BigQueryConfig:
    project_id: str
    dataset_id: str
    credentials: GCPCredentials

    def software(self) -> str:
        return "bigquery"

    def type(self) -> str:
        return "BIGQUERY_OFFLINE"

    def serialize(self) -> bytes:
        config = {
            "ProjectID": self.project_id,
            "DatasetID": self.dataset_id,
            "Credentials": self.credentials.to_json(),
        }
        return bytes(json.dumps(config), "utf-8")


@typechecked
@dataclass
class SparkConfig:
    executor_type: str
    executor_config: dict
    store_type: str
    store_config: dict

    def software(self) -> str:
        return "spark"

    def type(self) -> str:
        return "SPARK_OFFLINE"

    def serialize(self) -> bytes:
        config = {
            "ExecutorType": self.executor_type,
            "StoreType": self.store_type,
            "ExecutorConfig": self.executor_config,
            "StoreConfig": self.store_config,
        }
        return bytes(json.dumps(config), "utf-8")


@typechecked
@dataclass
class K8sResourceSpecs:
    cpu_request: str = ""
    cpu_limit: str = ""
    memory_request: str = ""
    memory_limit: str = ""


@typechecked
@dataclass
class K8sArgs:
    docker_image: str
    specs: Union[K8sResourceSpecs, None] = None

    def apply(self, transformation: pb.Transformation):
        transformation.kubernetes_args.docker_image = self.docker_image
        if self.specs is not None:
            transformation.kubernetes_args.specs.cpu_request = self.specs.cpu_request
            transformation.kubernetes_args.specs.cpu_limit = self.specs.cpu_limit
            transformation.kubernetes_args.specs.memory_request = (
                self.specs.memory_request
            )
            transformation.kubernetes_args.specs.memory_limit = self.specs.memory_limit
        return transformation


@typechecked
@dataclass
class K8sConfig:
    store_type: str
    store_config: dict
    docker_image: str = ""

    def software(self) -> str:
        return "k8s"

    def type(self) -> str:
        return "K8S_OFFLINE"

    def serialize(self) -> bytes:
        config = {
            "ExecutorType": "K8S",
            "ExecutorConfig": {"docker_image": self.docker_image},
            "StoreType": self.store_type,
            "StoreConfig": self.store_config,
        }
        return bytes(json.dumps(config), "utf-8")


@typechecked
@dataclass
class EmptyConfig:
    def software(self) -> str:
        return ""

    def type(self) -> str:
        return ""

    def serialize(self) -> bytes:
        return bytes("", "utf-8")

    def deserialize(self, config):
        return self


@typechecked
@dataclass
class LocalConfig:
    def software(self) -> str:
        return "localmode"

    def type(self) -> str:
        return "LOCAL_ONLINE"

    def serialize(self) -> bytes:
        return bytes(json.dumps({}), "utf-8")


Config = Union[
    RedisConfig,
    PineconeConfig,
    SnowflakeConfig,
    PostgresConfig,
    RedshiftConfig,
    PineconeConfig,
    LocalConfig,
    BigQueryConfig,
    FirestoreConfig,
    SparkConfig,
    OnlineBlobConfig,
    AzureFileStoreConfig,
    S3StoreConfig,
    K8sConfig,
    MongoDBConfig,
    GCSFileStoreConfig,
    EmptyConfig,
    HDFSConfig,
    WeaviateConfig,
    DynamodbConfig,
    CassandraConfig,
]


@typechecked
@dataclass
class Properties:
    properties: dict

    def __post_init__(self):
        self.serialized = pb.Properties()
        for key, val in self.properties.items():
            self.serialized.property[key].string_value = val


@typechecked
@dataclass
class Provider:
    name: str
    description: str
    team: str
    config: Config
    function: str
    status: str = "NO_STATUS"
    tags: list = field(default_factory=list)
    properties: dict = field(default_factory=dict)
    error: Optional[str] = None

    def __post_init__(self):
        self.software = self.config.software() if self.config is not None else None

    @staticmethod
    def operation_type() -> OperationType:
        return OperationType.CREATE

    @staticmethod
    def type() -> str:
        return "provider"

    def get(self, stub) -> "Provider":
        name = pb.Name(name=self.name)
        provider = next(stub.GetProviders(iter([name])))

        return Provider(
            name=provider.name,
            description=provider.description,
            function=provider.type,
            team=provider.team,
            config=EmptyConfig(),  # TODO add deserializer to configs
            tags=list(provider.tags.tag),
            properties={k: v for k, v in provider.properties.property.items()},
            status=provider.status.Status._enum_type.values[
                provider.status.status
            ].name,
            error=provider.status.error_message,
        )

    def _create(self, stub) -> None:
        serialized = pb.Provider(
            name=self.name,
            description=self.description,
            type=self.config.type(),
            software=self.config.software(),
            team=self.team,
            serialized_config=self.config.serialize(),
            tags=pb.Tags(tag=self.tags),
            properties=Properties(self.properties).serialized,
        )
        stub.CreateProvider(serialized)

    def _create_local(self, db) -> None:
        db.insert(
            "providers",
            self.name,
            "Provider",
            self.description,
            self.config.type(),
            self.config.software(),
            self.team,
            "sources",
            "ready",
            str(self.config.serialize(), "utf-8"),
        )
        if len(self.tags):
            db.upsert("tags", self.name, "", "providers", json.dumps(self.tags))
        if len(self.properties):
            db.upsert(
                "properties", self.name, "", "providers", json.dumps(self.properties)
            )

    def __eq__(self, other):
        for attribute in vars(self):
            if getattr(self, attribute) != getattr(other, attribute):
                return False
        return True

    def to_dictionary(self):
        return {
            "name": self.name,
            "description": self.description,
            "team": self.team,
            "config": "todox",
            "function": "todox",
            "status": self.status,
            "tags": self.tags,
            "properties": self.properties,
            "error": self.error,
        }


@typechecked
@dataclass
class User:
    name: str
    status: str = ""
    tags: list = field(default_factory=list)
    properties: dict = field(default_factory=dict)

    @staticmethod
    def operation_type() -> OperationType:
        return OperationType.CREATE

    def type(self) -> str:
        return "user"

    def _create(self, stub) -> None:
        serialized = pb.User(
            name=self.name,
            tags=pb.Tags(tag=self.tags),
            properties=Properties(self.properties).serialized,
        )
        stub.CreateUser(serialized)

    def _create_local(self, db) -> None:
        db.insert("users", self.name, "User", "ready")
        if len(self.tags):
            db.upsert("tags", self.name, "", "users", json.dumps(self.tags))
        if len(self.properties):
            db.upsert("properties", self.name, "", "users", json.dumps(self.properties))

    def __eq__(self, other):
        for attribute in vars(self):
            if getattr(self, attribute) != getattr(other, attribute):
                return False
        return True

    def to_dictionary(self):
        return {
            "name": self.name,
            "status": self.status,
            "tags": self.tags,
            "properties": self.properties,
        }


@typechecked
@dataclass
class SQLTable:
    name: str


@typechecked
@dataclass
class Directory:
    path: str


Location = Union[SQLTable, Directory]


@typechecked
@dataclass
class PrimaryData:
    location: Location

    def kwargs(self):
        return {
            "primaryData": pb.PrimaryData(
                table=pb.PrimarySQLTable(
                    name=self.location.name,
                ),
            ),
        }

    def name(self):
        return self.location.name

    def path(self):
        return self.location.path


class Transformation:
    pass


@typechecked
@dataclass
class SQLTransformation(Transformation):
    query: str
    args: K8sArgs = None

    def type(self):
        return SourceType.SQL_TRANSFORMATION.value

    def kwargs(self):
        transformation = pb.Transformation(
            SQLTransformation=pb.SQLTransformation(
                query=self.query,
            )
        )

        if self.args is not None:
            transformation = self.args.apply(transformation)

        return {"transformation": transformation}


@typechecked
@dataclass
class DFTransformation(Transformation):
    query: bytes
    inputs: list
    args: K8sArgs = None
    source_text: str = ""

    def type(self):
        return SourceType.DF_TRANSFORMATION.value

    def kwargs(self):
        transformation = pb.Transformation(
            DFTransformation=pb.DFTransformation(
                query=self.query,
                inputs=[pb.NameVariant(name=v[0], variant=v[1]) for v in self.inputs],
                source_text=self.source_text,
            )
        )

        if self.args is not None:
            transformation = self.args.apply(transformation)

        return {"transformation": transformation}


SourceDefinition = Union[PrimaryData, Transformation, str]


@typechecked
@dataclass
class Source:
    name: str
    default_variant: str
    variants: List[str]

    def to_dictionary(self):
        return {
            "name": self.name,
            "default_variant": self.default_variant,
            "variants": self.variants,
        }


@typechecked
@dataclass
class SourceVariant:
    name: str
    definition: SourceDefinition
    owner: str
    provider: str
    description: str
    tags: list
    properties: dict
    variant: str
    created: str = None
    status: str = (
        "ready"  # there is no associated status by default but it always stores ready
    )
    schedule: str = ""
    schedule_obj: Schedule = None
    is_transformation = SourceType.PRIMARY_SOURCE.value
    source_text: str = ""
    source_type: str = ""
    transformation: str = ""
    inputs: list = ([],)
    error: Optional[str] = None

    def update_schedule(self, schedule) -> None:
        self.schedule_obj = Schedule(
            name=self.name,
            variant=self.variant,
            resource_type=7,
            schedule_string=schedule,
        )
        self.schedule = schedule

    @staticmethod
    def operation_type() -> OperationType:
        return OperationType.CREATE

    @staticmethod
    def type() -> str:
        return "source"

    def get(self, stub):
        name_variant = pb.NameVariant(name=self.name, variant=self.variant)
        source = next(stub.GetSourceVariants(iter([name_variant])))
        definition = self._get_source_definition(source)

        return SourceVariant(
            created=None,
            name=source.name,
            definition=definition,
            owner=source.owner,
            provider=source.provider,
            description=source.description,
            variant=source.variant,
            tags=list(source.tags.tag),
            properties={k: v for k, v in source.properties.property.items()},
            status=source.status.Status._enum_type.values[source.status.status].name,
            error=source.status.error_message,
        )

    def _get_source_definition(self, source):
        if source.primaryData.table.name:
            return PrimaryData(SQLTable(source.primaryData.table.name))
        elif source.transformation:
            return self._get_transformation_definition(source)
        else:
            raise Exception(f"Invalid source type {source}")

    def _get_transformation_definition(self, source):
        if source.transformation.DFTransformation.query != bytes():
            transformation = source.transformation.DFTransformation
            return DFTransformation(
                query=transformation.query,
                inputs=[(input.name, input.variant) for input in transformation.inputs],
                source_text=transformation.source_text,
            )
        elif source.transformation.SQLTransformation.query != "":
            return SQLTransformation(source.transformation.SQLTransformation.query)
        else:
            raise Exception(f"Invalid transformation type {source}")

    def _create(self, stub) -> None:
        defArgs = self.definition.kwargs()
        serialized = pb.SourceVariant(
            created=None,
            name=self.name,
            variant=self.variant,
            owner=self.owner,
            description=self.description,
            schedule=self.schedule,
            provider=self.provider,
            tags=pb.Tags(tag=self.tags),
            properties=Properties(self.properties).serialized,
            **defArgs,
        )
        stub.CreateSourceVariant(serialized)

    def _create_local(self, db) -> None:
        should_insert_text = False
        source_text = ""
        self.source_type = "Source"
        if type(self.definition) == DFTransformation:
            should_insert_text = True
            self.is_transformation = SourceType.DF_TRANSFORMATION.value
            source_text = self.definition.source_text
            self.inputs = self.definition.inputs
            self.definition = self.definition.query
            self.source_text = source_text
            self.source_type = "Dataframe Transformation"
        elif type(self.definition) == SQLTransformation:
            self.is_transformation = SourceType.SQL_TRANSFORMATION.value
            self.definition = self.definition.query
        elif type(self.definition) == PrimaryData:
            if isinstance(self.definition.location, Directory):
                self.definition = self.definition.path()
                self.is_transformation = SourceType.DIRECTORY.value
            elif isinstance(self.definition.location, SQLTable):
                self.definition = self.definition.name()
                self.is_transformation = SourceType.PRIMARY_SOURCE.value
            else:
                raise ValueError(
                    f"Invalid Primary Data Type {self.definition.location}"
                )
        db.insert_source(
            "source_variant",
            str(time.time()),
            self.description,
            self.name,
            self.source_type,
            self.owner,
            self.provider,
            self.variant,
            "ready",
            self.is_transformation,
            json.dumps(self.inputs),
            self.definition,
        )

        if should_insert_text:
            db.insert_source_variant_text(
                str(time.time()), self.name, self.variant, source_text
            )

        if len(self.tags):
            db.upsert(
                "tags", self.name, self.variant, "source_variant", json.dumps(self.tags)
            )
        if len(self.properties):
            db.upsert(
                "properties",
                self.name,
                self.variant,
                "source_variant",
                json.dumps(self.properties),
            )
        self._create_source_resource(db)

    def _create_source_resource(self, db) -> None:
        db.insert("sources", "Source", self.variant, self.name)

    def get_status(self):
        return ResourceStatus(self.status)

    def is_ready(self):
        return self.status == ResourceStatus.READY.value

    def __eq__(self, other):
        for attribute in vars(self):
            if getattr(self, attribute) != getattr(other, attribute):
                return False
        return True


@typechecked
@dataclass
class Entity:
    name: str
    description: str
    status: str = "NO_STATUS"
    tags: list = field(default_factory=list)
    properties: dict = field(default_factory=dict)

    @staticmethod
    def operation_type() -> OperationType:
        return OperationType.CREATE

    @staticmethod
    def type() -> str:
        return "entity"

    def _create(self, stub) -> None:
        serialized = pb.Entity(
            name=self.name,
            description=self.description,
            tags=pb.Tags(tag=self.tags),
            properties=Properties(self.properties).serialized,
        )
        stub.CreateEntity(serialized)

    def _create_local(self, db) -> None:
        db.insert("entities", self.name, "Entity", self.description, "ready")
        if len(self.tags):
            db.upsert("tags", self.name, "", "entities", json.dumps(self.tags))
        if len(self.properties):
            db.upsert(
                "properties", self.name, "", "entities", json.dumps(self.properties)
            )

    def __eq__(self, other):
        for attribute in vars(self):
            if getattr(self, attribute) != getattr(other, attribute):
                return False
        return True

    def to_dictionary(self):
        return {
            "name": self.name,
            "description": self.description,
            "status": self.status,
            "tags": self.tags,
            "properties": self.properties,
        }


@typechecked
@dataclass
class ResourceColumnMapping:
    entity: str
    value: str
    timestamp: str

    def proto(self) -> pb.Columns:
        return pb.Columns(
            entity=self.entity,
            value=self.value,
            ts=self.timestamp,
        )


ResourceLocation = ResourceColumnMapping


@typechecked
@dataclass
class Feature:
    name: str
    default_variant: str
    variants: List[str]

    def to_dictionary(self):
        return {
            "name": self.name,
            "default_variant": self.default_variant,
            "variants": self.variants,
        }


@typechecked
@dataclass
class FeatureVariant:
    name: str
    source: NameVariant
    value_type: str
    entity: str
    owner: str
    provider: str
    location: ResourceLocation
    description: str
    variant: str
    created: str = None
    is_embedding: bool = False
    dims: int = 0
    tags: list = None
    properties: dict = None
    schedule: str = ""
    schedule_obj: Schedule = None
    status: str = "NO_STATUS"
    error: Optional[str] = None

    def __post_init__(self):
        col_types = [member.value for member in ScalarType]
        if self.value_type not in col_types:
            raise ValueError(
                f"Invalid feature type ({self.value_type}) must be one of: {col_types}"
            )

    def update_schedule(self, schedule) -> None:
        self.schedule_obj = Schedule(
            name=self.name,
            variant=self.variant,
            resource_type=4,
            schedule_string=schedule,
        )
        self.schedule = schedule

    @staticmethod
    def operation_type() -> OperationType:
        return OperationType.CREATE

    @staticmethod
    def type() -> str:
        return "feature"

    def get(self, stub) -> "FeatureVariant":
        name_variant = pb.NameVariant(name=self.name, variant=self.variant)
        feature = next(stub.GetFeatureVariants(iter([name_variant])))

        return FeatureVariant(
            created=None,
            name=feature.name,
            variant=feature.variant,
            source=(feature.source.name, feature.source.variant),
            value_type=feature.type,
            is_embedding=feature.is_embedding,
            dims=feature.dimension,
            entity=feature.entity,
            owner=feature.owner,
            provider=feature.provider,
            location=ResourceColumnMapping("", "", ""),
            description=feature.description,
            tags=list(feature.tags.tag),
            properties={k: v for k, v in feature.properties.property.items()},
            status=feature.status.Status._enum_type.values[feature.status.status].name,
            error=feature.status.error_message,
        )

    def _create(self, stub) -> None:
        serialized = pb.FeatureVariant(
            name=self.name,
            variant=self.variant,
            source=pb.NameVariant(
                name=self.source[0],
                variant=self.source[1],
            ),
            type=self.value_type,
            is_embedding=self.is_embedding,
            dimension=self.dims,
            entity=self.entity,
            owner=self.owner,
            description=self.description,
            schedule=self.schedule,
            provider=self.provider,
            columns=self.location.proto(),
            mode=ComputationMode.PRECOMPUTED.proto(),
            tags=pb.Tags(tag=self.tags),
            properties=Properties(self.properties).serialized,
        )
        stub.CreateFeatureVariant(serialized)

    def _create_local(self, db) -> None:
        db.insert(
            "feature_variant",
            str(time.time()),
            self.description,
            self.entity,
            self.name,
            self.owner,
            self.provider,
            self.value_type,
            self.variant,
            "ready",
            self.location.entity,
            self.location.timestamp,
            self.location.value,
            self.source[0],
            self.source[1],
            self.is_embedding,
            self.dims,
        )
        if len(self.tags):
            db.upsert(
                "tags",
                self.name,
                self.variant,
                "feature_variant",
                json.dumps(self.tags),
            )
        if len(self.properties):
            db.upsert(
                "properties",
                self.name,
                self.variant,
                "feature_variant",
                json.dumps(self.properties),
            )

        self._write_feature_variant_and_mode(db)

    def _write_feature_variant_and_mode(self, db) -> None:
        db.insert(
            "features",
            self.name,
            self.variant,
            self.value_type,
        )
        is_on_demand = 0
        db.insert(
            "feature_computation_mode",
            self.name,
            self.variant,
            ComputationMode.PRECOMPUTED.value,
            is_on_demand,
        )

    def get_status(self):
        return ResourceStatus(self.status)

    def is_ready(self):
        return self.status == ResourceStatus.READY.value

    def __eq__(self, other):
        for attribute in vars(self):
            if getattr(self, attribute) != getattr(other, attribute):
                return False
        return True


@typechecked
@dataclass
class OnDemandFeatureVariant:
    owner: str
    variant: str
    tags: List[str] = field(default_factory=list)
    properties: dict = field(default_factory=dict)
    name: str = ""
    description: str = ""
    status: str = "READY"
    error: Optional[str] = None

    def __call__(self, fn):
        if self.description == "" and fn.__doc__ is not None:
            self.description = fn.__doc__
        if self.name == "":
            self.name = fn.__name__

        self.query = dill.dumps(fn.__code__)
        fn.name_variant = self.name_variant
        fn.query = self.query
        return fn

    def name_variant(self):
        return (self.name, self.variant)

    @staticmethod
    def operation_type() -> OperationType:
        return OperationType.CREATE

    @staticmethod
    def type() -> str:
        return "ondemand_feature"

    def _create(self, stub) -> None:
        serialized = pb.FeatureVariant(
            name=self.name,
            variant=self.variant,
            owner=self.owner,
            description=self.description,
            function=pb.PythonFunction(query=self.query),
            mode=ComputationMode.CLIENT_COMPUTED.proto(),
            tags=pb.Tags(tag=self.tags),
            properties=Properties(self.properties).serialized,
            status=pb.ResourceStatus(status=pb.ResourceStatus.READY),
        )
        stub.CreateFeatureVariant(serialized)

    def _create_local(self, db) -> None:
        decode_query = base64.b64encode(self.query).decode("ascii")

        db.insert(
            "ondemand_feature_variant",
            str(time.time()),
            self.description,
            self.name,
            self.owner,
            self.variant,
            "ready",
            decode_query,
        )
        if self.tags and len(self.tags):
            db.upsert(
                "tags",
                self.name,
                self.variant,
                "feature_variant",
                json.dumps(self.tags),
            )
        if len(self.properties):
            db.upsert(
                "properties",
                self.name,
                self.variant,
                "feature_variant",
                json.dumps(self.properties),
            )

        self._write_feature_variant_and_mode(db)

    def _write_feature_variant_and_mode(self, db) -> None:
        db.insert(
            "features",
            self.name,
            self.variant,
            "tbd",
        )
        is_on_demand = 1

        db.insert(
            "feature_computation_mode",
            self.name,
            self.variant,
            ComputationMode.CLIENT_COMPUTED.value,
            is_on_demand,
        )

    def get(self, stub) -> "OnDemandFeatureVariant":
        name_variant = pb.NameVariant(name=self.name, variant=self.variant)
        ondemand_feature = next(stub.GetFeatureVariants(iter([name_variant])))

        return OnDemandFeatureVariant(
            name=ondemand_feature.name,
            variant=ondemand_feature.variant,
            owner=ondemand_feature.owner,
            description=ondemand_feature.description,
            tags=list(ondemand_feature.tags.tag),
            properties={k: v for k, v in ondemand_feature.properties.property.items()},
            status=ondemand_feature.status.Status._enum_type.values[
                ondemand_feature.status.status
            ].name,
            error=ondemand_feature.status.error_message,
        )

    def get_status(self):
        return ResourceStatus(self.status)

    def is_ready(self):
        return self.status == ResourceStatus.READY.value

    def __eq__(self, other):
        for attribute in vars(self):
            if getattr(self, attribute) != getattr(other, attribute):
                return False
        return True


@typechecked
@dataclass
class Label:
    name: str
    default_variant: str
    variants: List[str]

    def to_dictionary(self):
        return {
            "name": self.name,
            "default_variant": self.default_variant,
            "variants": self.variants,
        }


@typechecked
@dataclass
class LabelVariant:
    name: str
    source: NameVariant
    value_type: str
    entity: str
    owner: str
    provider: str
    description: str
    tags: list
    properties: dict
    location: ResourceLocation
    variant: str
    created: str = None
    status: str = "NO_STATUS"
    error: Optional[str] = None

    def __post_init__(self):
        col_types = [member.value for member in ScalarType]
        if self.value_type not in col_types:
            raise ValueError(
                f"Invalid label type ({self.value_type}) must be one of: {col_types}"
            )

    @staticmethod
    def operation_type() -> OperationType:
        return OperationType.CREATE

    @staticmethod
    def type() -> str:
        return "label"

    def get(self, stub) -> "LabelVariant":
        name_variant = pb.NameVariant(name=self.name, variant=self.variant)
        label = next(stub.GetLabelVariants(iter([name_variant])))

        return LabelVariant(
            name=label.name,
            variant=label.variant,
            source=(label.source.name, label.source.variant),
            value_type=label.type,
            entity=label.entity,
            owner=label.owner,
            provider=label.provider,
            location=ResourceColumnMapping("", "", ""),
            description=label.description,
            tags=list(label.tags.tag),
            properties={k: v for k, v in label.properties.property.items()},
            status=label.status.Status._enum_type.values[label.status.status].name,
            error=label.status.error_message,
        )

    def _create(self, stub) -> None:
        serialized = pb.LabelVariant(
            name=self.name,
            variant=self.variant,
            source=pb.NameVariant(
                name=self.source[0],
                variant=self.source[1],
            ),
            type=self.value_type,
            entity=self.entity,
            owner=self.owner,
            description=self.description,
            columns=self.location.proto(),
            tags=pb.Tags(tag=self.tags),
            properties=Properties(self.properties).serialized,
        )
        stub.CreateLabelVariant(serialized)

    def _create_local(self, db) -> None:
        db.insert(
            "label_variant",
            str(time.time()),
            self.description,
            self.entity,
            self.name,
            self.owner,
            self.provider,
            self.value_type,
            self.variant,
            self.location.entity,
            self.location.timestamp,
            self.location.value,
            "ready",
            self.source[0],
            self.source[1],
        )
        if len(self.tags):
            db.upsert(
                "tags", self.name, self.variant, "label_variant", json.dumps(self.tags)
            )
        if len(self.properties):
            db.upsert(
                "properties",
                self.name,
                self.variant,
                "label_variant",
                json.dumps(self.properties),
            )
        self._create_label_resource(db)

    def _create_label_resource(self, db) -> None:
        db.insert("labels", self.value_type, self.variant, self.name)

    def get_status(self):
        return ResourceStatus(self.status)

    def is_ready(self):
        return self.status == ResourceStatus.READY.value

    def __eq__(self, other):
        for attribute in vars(self):
            if getattr(self, attribute) != getattr(other, attribute):
                return False
        return True


@typechecked
@dataclass
class EntityReference:
    name: str
    obj: Union[Entity, None]

    @staticmethod
    def operation_type() -> OperationType:
        return OperationType.GET

    @staticmethod
    def type() -> str:
        return "entity"

    def _get(self, stub):
        entityList = stub.GetEntities(iter([pb.Name(name=self.name)]))
        try:
            for entity in entityList:
                self.obj = entity
        except grpc._channel._MultiThreadedRendezvous:
            raise ValueError(f"Entity {self.name} not found.")

    def _get_local(self, db):
        local_entity = db.query_resource("entities", "name", self.name)
        if local_entity == []:
            raise ValueError(f"Entity {self.name} not found.")
        self.obj = local_entity


@typechecked
@dataclass
class ProviderReference:
    name: str
    provider_type: str
    obj: Union[Provider, None]

    @staticmethod
    def operation_type() -> OperationType:
        return OperationType.GET

    @staticmethod
    def type() -> str:
        return "provider"

    def _get(self, stub):
        providerList = stub.GetProviders(iter([pb.Name(name=self.name)]))
        try:
            for provider in providerList:
                self.obj = provider
        except grpc._channel._MultiThreadedRendezvous:
            raise ValueError(
                f"Provider {self.name} of type {self.provider_type} not found."
            )

    def _get_local(self, db):
        local_provider = db.query_resource("providers", "name", self.name)
        if local_provider == []:
            raise ValueError("Local mode provider not found.")
        self.obj = local_provider


@typechecked
@dataclass
class SourceReference:
    name: str
    variant: str
    obj: Union[SourceVariant, None]

    @staticmethod
    def operation_type() -> OperationType:
        return OperationType.GET

    @staticmethod
    def type() -> str:
        return "source"

    def _get(self, stub):
        sourceList = stub.GetSourceVariants(
            iter([pb.NameVariant(name=self.name, variant=self.variant)])
        )
        try:
            for source in sourceList:
                self.obj = source
        except grpc._channel._MultiThreadedRendezvous:
            raise ValueError(f"Source {self.name}, variant {self.variant} not found.")

    def _get_local(self, db):
        local_source = db.get_source_variant(self.name, self.variant)
        if local_source == []:
            raise ValueError(f"Source {self.name}, variant {self.variant} not found.")
        self.obj = local_source


@typechecked
@dataclass
class TrainingSet:
    name: str
    default_variant: str
    variants: List[str]

    def to_dictionary(self):
        return {
            "name": self.name,
            "default_variant": self.default_variant,
            "variants": self.variants,
        }


@typechecked
@dataclass
class TrainingSetVariant:
    name: str
    owner: str
    label: NameVariant
    features: List[NameVariant]
    description: str
    variant: str
    feature_lags: list = field(default_factory=list)
    tags: list = field(default_factory=list)
    properties: dict = field(default_factory=dict)
    created: str = None
    schedule: str = ""
    schedule_obj: Schedule = None
    provider: str = ""
    status: str = "NO_STATUS"
    error: Optional[str] = None

    def update_schedule(self, schedule) -> None:
        self.schedule_obj = Schedule(
            name=self.name,
            variant=self.variant,
            resource_type=6,
            schedule_string=schedule,
        )
        self.schedule = schedule

    def __post_init__(self):
        if not valid_name_variant(self.label):
            raise ValueError("Label must be set")
        if len(self.features) == 0:
            raise ValueError("A training-set must have atleast one feature")
        for feature in self.features:
            if not valid_name_variant(feature):
                raise ValueError("Invalid Feature")

    @staticmethod
    def operation_type() -> OperationType:
        return OperationType.CREATE

    @staticmethod
    def type() -> str:
        return "training-set"

    def get(self, stub):
        name_variant = pb.NameVariant(name=self.name, variant=self.variant)
        ts = next(stub.GetTrainingSetVariants(iter([name_variant])))

        return TrainingSetVariant(
            created=None,
            name=ts.name,
            variant=ts.variant,
            owner=ts.owner,
            description=ts.description,
            status=ts.status.Status._enum_type.values[ts.status.status].name,
            label=(ts.label.name, ts.label.variant),
            features=[(f.name, f.variant) for f in ts.features],
            feature_lags=[],
            provider=ts.provider,
            tags=list(ts.tags.tag),
            properties={k: v for k, v in ts.properties.property.items()},
            error=ts.status.error_message,
        )

    def _create(self, stub) -> None:
        feature_lags = []
        for lag in self.feature_lags:
            lag_duration = Duration()
            _ = lag_duration.FromTimedelta(lag["lag"])
            feature_lag = pb.FeatureLag(
                feature=lag["feature"],
                variant=lag["variant"],
                name=lag["name"],
                lag=lag_duration,
            )
            feature_lags.append(feature_lag)

        serialized = pb.TrainingSetVariant(
            created=None,
            name=self.name,
            variant=self.variant,
            description=self.description,
            schedule=self.schedule,
            owner=self.owner,
            features=[pb.NameVariant(name=v[0], variant=v[1]) for v in self.features],
            label=pb.NameVariant(name=self.label[0], variant=self.label[1]),
            feature_lags=feature_lags,
            tags=pb.Tags(tag=self.tags),
            properties=Properties(self.properties).serialized,
        )
        stub.CreateTrainingSetVariant(serialized)

    def _create_local(self, db) -> None:
        self._check_insert_training_set_resources(db)
        db.insert(
            "training_set_variant",
            str(time.time()),
            self.description,
            self.name,
            self.owner,
            self.variant,
            self.label[0],
            self.label[1],
            "ready",
        )
        if len(self.tags):
            db.upsert(
                "tags",
                self.name,
                self.variant,
                "training_set_variant",
                json.dumps(self.tags),
            )
        if len(self.properties):
            db.upsert(
                "properties",
                self.name,
                self.variant,
                "training_set_variant",
                json.dumps(self.properties),
            )
        self._create_training_set_resource(db)

    def _create_training_set_resource(self, db) -> None:
        db.insert("training_sets", "TrainingSet", self.variant, self.name)

    def _check_insert_training_set_resources(self, db) -> None:
        try:
            db.get_label_variant(self.label[0], self.label[1])
        except ValueError:
            raise LabelNotFound(
                self.label[0], self.label[1], message="Failed to register training set."
            )

        for feature_name, feature_variant in self.features:
            try:
                is_on_demand = db.get_feature_variant_on_demand(
                    feature_name, feature_variant
                )
                if is_on_demand:
                    raise InvalidTrainingSetFeatureComputationMode(
                        feature_name, feature_variant
                    )
            except InvalidTrainingSetFeatureComputationMode as e:
                raise e
            except Exception as e:
                raise FeatureNotFound(
                    feature_name,
                    feature_variant,
                    message=f"Failed to register training set. Error: {e}",
                )

            db.insert(
                "training_set_features",
                self.name,
                self.variant,
                feature_name,  # feature name
                feature_variant,  # feature variant
            )

        for feature in self.feature_lags:
            feature_name = feature["feature"]
            feature_variant = feature["variant"]
            feature_new_name = feature["name"]
            feature_lag = feature["lag"].total_seconds()

            try:
                db.get_feature_variant(feature_name, feature_variant)
            except Exception as e:
                raise FeatureNotFound(
                    feature_name,
                    feature_variant,
                    message=f"Failed to register training set. Error: {e}",
                )

            db.insert(
                "training_set_lag_features",
                self.name,
                self.variant,
                feature_name,  # feature name
                feature_variant,  # feature variant
                feature_new_name,  # feature new name
                feature_lag,  # feature_lag
            )

    def get_status(self):
        return ResourceStatus(self.status)

    def is_ready(self):
        return self.status == ResourceStatus.READY.value

    def __eq__(self, other):
        for attribute in vars(self):
            if getattr(self, attribute) != getattr(other, attribute):
                return False
        return True


@typechecked
@dataclass
class Model:
    name: str
    description: str = ""
    tags: list = field(default_factory=list)
    properties: dict = field(default_factory=dict)

    @staticmethod
    def operation_type() -> OperationType:
        return OperationType.CREATE

    def type(self) -> str:
        return "model"

    def _create(self, stub) -> None:
        properties = pb.Properties(property=self.properties)
        serialized = pb.Model(
            name=self.name,
            tags=pb.Tags(tag=self.tags),
            properties=Properties(self.properties).serialized,
        )
        stub.CreateModel(serialized)

    def _create_local(self, db) -> None:
        db.insert(
            "models",
            self.name,
            "Model",
        )
        if len(self.tags):
            db.upsert("tags", self.name, "", "models", json.dumps(self.tags))
        if len(self.properties):
            db.upsert(
                "properties", self.name, "", "models", json.dumps(self.properties)
            )

    def __eq__(self, other):
        for attribute in vars(self):
            if getattr(self, attribute) != getattr(other, attribute):
                return False
        return True

    def to_dictionary(self):
        return {
            "name": self.name,
            "description": self.description,
            "tags": self.tags,
            "properties": self.properties,
        }


Resource = Union[
    PrimaryData,
    Provider,
    Entity,
    User,
    FeatureVariant,
    LabelVariant,
    TrainingSetVariant,
    SourceVariant,
    Schedule,
    ProviderReference,
    SourceReference,
    EntityReference,
    Model,
    OnDemandFeatureVariant,
]


class ResourceRedefinedError(Exception):
    @typechecked
    def __init__(self, resource: Resource):
        variantStr = (
            f" variant {resource.variant}" if hasattr(resource, "variant") else ""
        )
        resourceId = f"{resource.name}{variantStr}"
        super().__init__(
            f"{resource.type()} resource {resourceId} defined in multiple places"
        )


class ResourceState:
    def __init__(self):
        self.__state = {}

    def reset(self):
        self.__state = {}

    @typechecked
    def add(self, resource: Resource) -> None:
        if hasattr(resource, "variant"):
            key = (
                resource.operation_type().name,
                resource.type(),
                resource.name,
                resource.variant,
            )
        else:
            key = (resource.operation_type().name, resource.type(), resource.name)
        if key in self.__state:
            if resource == self.__state[key]:
                print(f"Resource {resource.type()} already registered.")
                return
            raise ResourceRedefinedError(resource)
        self.__state[key] = resource
        if hasattr(resource, "schedule_obj") and resource.schedule_obj != None:
            my_schedule = resource.schedule_obj
            key = (my_schedule.type(), my_schedule.name)
            self.__state[key] = my_schedule

    def sorted_list(self) -> List[Resource]:
        resource_order = {
            "user": 0,
            "provider": 1,
            "source": 2,
            "entity": 3,
            "feature": 4,
            "ondemand_feature": 5,
            "label": 6,
            "training-set": 7,
            "schedule": 8,
            "model": 9,
        }

        def to_sort_key(res):
            resource_num = resource_order[res.type()]
            return resource_num

        return sorted(self.__state.values(), key=to_sort_key)

    def create_all_dryrun(self) -> None:
        for resource in self.sorted_list():
            if resource.operation_type() is OperationType.GET:
                print("Getting", resource.type(), resource.name)
            if resource.operation_type() is OperationType.CREATE:
                print("Creating", resource.type(), resource.name)

    def create_all_local(self) -> None:
        db = SQLiteMetadata()
        check_up_to_date(True, "register")
        features = []
        for resource in self.sorted_list():
            if isinstance(resource, FeatureVariant):
                features.append(resource)
            resource_variant = (
                f" {resource.variant}" if hasattr(resource, "variant") else ""
            )
            if resource.operation_type() is OperationType.GET:
                print("Getting", resource.type(), resource.name, resource_variant)
                resource._get_local(db)

            if resource.operation_type() is OperationType.CREATE:
                if resource.name != "default_user":
                    print("Creating", resource.type(), resource.name, resource_variant)
                resource._create_local(db)
        db.close()

        from .serving import LocalClientImpl

        client = LocalClientImpl()
        for feature in features:
            client.compute_feature(feature.name, feature.variant, feature.entity)
        return

    def create_all(self, stub) -> None:
        check_up_to_date(False, "register")
        for resource in self.sorted_list():
            if resource.type() == "provider" and resource.name == "local-mode":
                continue
            if resource.type() == "feature" and resource.provider == "local-mode":
                raise ValueError(
                    f"Inference store must be provided for feature {resource.name} ({resource.variant})"
                )
            try:
                # NOTE: There is an extra space before the variant name to better handle the case
                # where a resource has no variant; ultimately, we should separate data access and
                # logging/CLI output to avoid this unnecessary coupling.
                resource_variant = (
                    f" {resource.variant}" if hasattr(resource, "variant") else ""
                )
                if resource.operation_type() is OperationType.GET:
                    print(
                        f"Getting {resource.type()} {resource.name}{resource_variant}"
                    )
                    resource._get(stub)
                if resource.operation_type() is OperationType.CREATE:
                    if resource.name != "default_user":
                        print(
                            f"Creating {resource.type()} {resource.name}{resource_variant}"
                        )
                    resource._create(stub)
            except grpc.RpcError as e:
                if e.code() == grpc.StatusCode.ALREADY_EXISTS:
                    print(f"{resource.name}{resource_variant} already exists.")
                    continue

                raise e


## Executor Providers
@typechecked
class DatabricksCredentials:
    def __init__(
        self,
        cluster_id: str,
        username: str = "",
        password: str = "",
        host: str = "",
        token: str = "",
    ):
        """

        Credentials for a Databricks cluster.

        **Example**
        ```
        databricks = ff.DatabricksCredentials(
            username="<my_username>",
            password="<my_password>",
            host="<databricks_hostname>",
            token="<databricks_token>",
            cluster_id="<databricks_cluster>",
        )

        spark = ff.register_spark(
            name="spark",
            executor=databricks,
            ...
        )
        ```

        Args:
            username (str): Username for a Databricks cluster.
            password (str): Password for a Databricks cluster.
            host (str): The hostname of a Databricks cluster.
            token (str): The token for a Databricks cluster.
            cluster_id (str): ID of an existing Databricks cluster.
        """
        self.username = username
        self.password = password
        self.host = host
        self.token = token
        self.cluster_id = cluster_id

        host_token_provided = (
            username == "" and password == "" and host != "" and token != ""
        )
        username_password_provided = (
            username != "" and password != "" and host == "" and token == ""
        )

        if (
            not host_token_provided
            and not username_password_provided
            or host_token_provided
            and username_password_provided
        ):
            raise Exception(
                "The DatabricksCredentials requires only one credentials set ('username' and 'password' or 'host' and 'token' set.)"
            )

        if not cluster_id:
            raise Exception("Cluster_id of existing cluster must be provided")

    def type(self):
        return "DATABRICKS"

    def config(self):
        return {
            "Username": self.username,
            "Password": self.password,
            "Host": self.host,
            "Token": self.token,
            "Cluster": self.cluster_id,
        }


@typechecked
@dataclass
class EMRCredentials:
    def __init__(
        self, emr_cluster_id: str, emr_cluster_region: str, credentials: AWSCredentials
    ):
        """

        Credentials for an EMR cluster.

        **Example**
        ```
        emr = ff.EMRCredentials(
            emr_cluster_id="<cluster_id>",
            emr_cluster_region="<cluster_region>",
            credentials="<AWS_Credentials>",
        )

        spark = ff.register_spark(
            name="spark",
            executor=emr,
            ...
        )
        ```

        Args:
            emr_cluster_id (str): ID of an existing EMR cluster.
            emr_cluster_region (str): Region of an existing EMR cluster.
            credentials (AWSCredentials): Credentials for an AWS account with access to the cluster
        """
        self.emr_cluster_id = emr_cluster_id
        self.emr_cluster_region = emr_cluster_region
        self.credentials = credentials

    def type(self):
        return "EMR"

    def config(self):
        return {
            "ClusterName": self.emr_cluster_id,
            "ClusterRegion": self.emr_cluster_region,
            "Credentials": self.credentials.config(),
        }


@typechecked
@dataclass
class SparkCredentials:
    def __init__(
        self,
        master: str,
        deploy_mode: str,
        python_version: str,
        core_site_path: str = "",
        yarn_site_path: str = "",
    ):
        """

        Credentials for a Generic Spark Cluster

        **Example**
        ```
        spark_credentials = ff.SparkCredentials(
            master="yarn",
            deploy_mode="cluster",
            python_version="3.7.12",
            core_site_path="core-site.xml",
            yarn_site_path="yarn-site.xml"
        )

        spark = ff.register_spark(
            name="spark",
            executor=spark_credentials,
            ...
        )
        ```

        Args:
            master (str): The hostname of the Spark cluster. (The same that would be passed to `spark-submit`).
            deploy_mode (str): The deploy mode of the Spark cluster. (The same that would be passed to `spark-submit`).
            python_version (str): The Python version running on the cluster. Supports 3.7-3.11
            core_site_path (str): The path to the core-site.xml file. (For Yarn clusters only)
            yarn_site_path (str): The path to the yarn-site.xml file. (For Yarn clusters only)
        """
        self.master = master.lower()
        self.deploy_mode = deploy_mode.lower()
        self.core_site_path = core_site_path
        self.yarn_site_path = yarn_site_path

        if self.deploy_mode != "cluster" and self.deploy_mode != "client":
            raise Exception(
                f"Spark does not support '{self.deploy_mode}' deploy mode. It only supports 'cluster' and 'client'."
            )

        self.python_version = self._verify_python_version(
            self.deploy_mode, python_version
        )

        self._verify_yarn_config()

    def _verify_python_version(self, deploy_mode, version):
        if deploy_mode == "cluster" and version == "":
            client_python_version = sys.version_info
            client_major = str(client_python_version.major)
            client_minor = str(client_python_version.minor)

            if client_major != MAJOR_VERSION:
                client_major = "3"
            if client_minor not in MINOR_VERSIONS:
                client_minor = "7"

            version = f"{client_major}.{client_minor}"

        if version.count(".") == 2:
            major, minor, _ = version.split(".")
        elif version.count(".") == 1:
            major, minor = version.split(".")
        else:
            raise Exception(
                "Please specify your Python version on the Spark cluster. Accepted formats: Major.Minor or Major.Minor.Patch; ex. '3.7' or '3.7.16"
            )

        if major != MAJOR_VERSION or minor not in MINOR_VERSIONS:
            raise Exception(
                f"The Python version {version} is not supported. Currently, supported versions are 3.7-3.10."
            )

        """
        The Python versions on the Docker image are 3.7.16, 3.8.16, 3.9.16, 3.10.10, and 3.11.2.
        This conditional statement sets the patch number based on the minor version. 
        """
        if minor == "10":
            patch = "10"
        elif minor == "11":
            patch = "2"
        else:
            patch = "16"

        return f"{major}.{minor}.{patch}"

    def _verify_yarn_config(self):
        if self.master == "yarn" and (
            self.core_site_path == "" or self.yarn_site_path == ""
        ):
            raise Exception(
                "Yarn requires core-site.xml and yarn-site.xml files."
                "Please copy these files from your Spark instance to local, then provide the local path in "
                "core_site_path and yarn_site_path. "
            )

    def type(self):
        return "SPARK"

    def config(self):
        core_site = (
            "" if self.core_site_path == "" else open(self.core_site_path, "r").read()
        )
        yarn_site = (
            "" if self.yarn_site_path == "" else open(self.yarn_site_path, "r").read()
        )

        return {
            "Master": self.master,
            "DeployMode": self.deploy_mode,
            "PythonVersion": self.python_version,
            "CoreSite": core_site,
            "YarnSite": yarn_site,
        }


@typechecked
@dataclass
class TrainingSetFeatures:
    training_set_name: str
    training_set_variant: str
    feature_name: str
    feature_variant: str

    def to_dictionary(self):
        return {
            "training_set_name": self.training_set_name,
            "training_set_variant": self.training_set_variant,
            "feature_name": self.feature_name,
            "feature_variant": self.feature_variant,
        }


ExecutorCredentials = Union[EMRCredentials, DatabricksCredentials, SparkCredentials]
