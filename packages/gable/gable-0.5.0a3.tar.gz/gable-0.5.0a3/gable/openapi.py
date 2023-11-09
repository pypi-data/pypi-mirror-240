# generated by datamodel-codegen:
#   filename:  bundled.yaml

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, BaseModel, Field


class PingResponse(BaseModel):
    message: str
    success: bool


class Status(Enum):
    ACTIVE = "ACTIVE"
    DEPRECATED = "DEPRECATED"


class NotificationLevel(Enum):
    RECORD = "RECORD"
    NOTIFY = "NOTIFY"
    ALERT = "ALERT"
    BLOCK = "BLOCK"
    INACTIVE = "INACTIVE"


class ContractInput(BaseModel):
    id: UUID = Field(
        ..., description="Unique identifier for the contract in UUID format"
    )
    version: str = Field(
        ..., description="Version of the contract (semantic versioning)"
    )
    status: Status = Field(..., description="status of the contract")
    gitHash: str = Field(
        ...,
        description="full length git hash corresponding to the commit this contract was added/updated",
        max_length=40,
        min_length=40,
    )
    gitRepo: AnyUrl = Field(
        ..., description="full link to the git repo this contract lives in"
    )
    gitUser: str = Field(..., description="git user who added/updated this contract")
    reviewers: Optional[List[str]] = Field(
        None,
        description="optional list of users who reviewed the merged PR that this contract added/updated in",
    )
    filePath: str = Field(
        ...,
        description="path to the contract file from the root of the git repository",
        regex="^([^/]+\\/)*[^/]+$",
    )
    mergedAt: datetime = Field(
        ...,
        description="date time at which the PR that added/updated this contract was merged",
    )
    notificationLevel: Optional[NotificationLevel] = Field(
        "INACTIVE", description="alert level for contract"
    )
    contractSpec: Dict[str, Any] = Field(
        ...,
        description="This is the possible contract specification. If it is valid, it will  match the contract specification schema. However, we have to allow  for invalid contracts to be passed to Gable even if we reject them.",
    )


class PostContractRequest(BaseModel):
    __root__: Union[ContractInput, List[ContractInput]]


class CheckResponse(BaseModel):
    message: str
    success: bool


class ContractOutput(BaseModel):
    id: UUID = Field(
        ..., description="Unique identifier for the contract in UUID format"
    )
    version: str = Field(
        ..., description="Version of the contract (semantic versioning)"
    )
    status: Status = Field(..., description="status of the contract")
    gitHash: str = Field(
        ...,
        description="full length git hash corresponding to the commit this contract was added/updated",
        max_length=40,
        min_length=40,
    )
    gitRepo: AnyUrl = Field(
        ..., description="full link to the git repo this contract lives in"
    )
    gitUser: str = Field(..., description="git user who added/updated this contract")
    fileUri: AnyUrl = Field(
        ..., description="full link to the file in the repo that contains this contract"
    )
    reviewers: Optional[List[str]] = Field(
        None,
        description="optional list of users who reviewed the merged PR that this contract added/updated in",
    )
    mergedAt: datetime = Field(
        ...,
        description="date time at which the PR that added/updated this contract was merged",
    )
    createdAt: datetime = Field(
        ..., description="date time at which the contract was created"
    )
    updatedAt: datetime = Field(
        ..., description="date time at which the contract was last updated"
    )
    contractSpec: Dict[str, Any] = Field(..., description="contract spec")
    contractSpecRaw: str = Field(..., description="contract spec raw json")
    notificationLevel: Optional[NotificationLevel] = Field(
        "INACTIVE", description="alert level for contract"
    )


class Type(Enum):
    PROTOBUF = "PROTOBUF"
    AVRO = "AVRO"
    JSON_SCHEMA = "JSON_SCHEMA"
    POSTGRES = "POSTGRES"
    SNOWFLAKE = "SNOWFLAKE"


class CheckContractViolationRequest(BaseModel):
    type: Type = Field(
        ..., description="The type of the schema to check for violations"
    )
    schema_contents: str = Field(
        ..., description="The schema contents to check for violations"
    )
    isSchemaBase64: Optional[bool] = Field(
        False, description="Whether the schema is base64 encoded, defaults to false"
    )


class GetContractsResponse(BaseModel):
    __root__: List[ContractOutput]


class PostContractResponse(BaseModel):
    message: str
    contractIds: List[UUID] = Field(
        ...,
        description="List of contract IDs that were updated, if no contracts were updated this will be an empty list",
    )


class Type1(Enum):
    CONTRACT_UPDATED = "CONTRACT_UPDATED"


class ContractActivityUpdateEvent(BaseModel):
    type: Type1 = Field(..., description="type of the event")
    datetime: datetime = Field(
        ..., description="date time at which the contract was updated"
    )
    fileUri: AnyUrl = Field(
        ...,
        description="full link to the file and commit in the repo that contains this updated contract",
    )
    gitUser: Optional[str] = Field(
        None, description="the git user who edited the contract"
    )


class Type2(Enum):
    CONTRACT_CREATED = "CONTRACT_CREATED"


class ContractActivityCreateEvent(BaseModel):
    type: Type2 = Field(..., description="type of the event")
    datetime: datetime = Field(
        ..., description="date time at which the contract was created"
    )
    fileUri: AnyUrl = Field(
        ...,
        description="full link to the file and commit in the repo that contains this created contract",
    )
    gitUser: Optional[str] = Field(
        None, description="the git user who created the contract"
    )


class ContractActivityResponse(BaseModel):
    __root__: List[
        Union[ContractActivityUpdateEvent, ContractActivityCreateEvent]
    ] = Field(
        ...,
        description="List of contract activity events in chronological order (oldest first)",
        min_items=1,
    )


class ErrorResponse(BaseModel):
    id: Optional[float] = None
    title: Optional[str] = None
    message: str


class ContractSubscription(BaseModel):
    id: UUID = Field(..., description="The unique identifier of the subscription")
    dataContractId: UUID = Field(..., description="Unique identifier of the contract")
    userId: Optional[UUID] = Field(
        None, description="The unique identifier of the user"
    )
    email: Optional[str] = Field(
        None,
        description="The email address of the subscriber if provided",
        regex="^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$",
    )
    githubHandle: Optional[str] = Field(
        None, description="The GitHub handle of the subscriber if provided"
    )


class UpdateContractSubscriptionRequest(BaseModel):
    dataContractId: UUID = Field(..., description="Unique identifier of the contract")
    userId: Optional[UUID] = Field(
        None, description="The unique identifier of the user"
    )
    email: Optional[str] = Field(
        None,
        description="The email address of the subscriber if provided",
        regex="^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$",
    )
    githubHandle: Optional[str] = Field(
        None, description="The GitHub handle for the subscriber if provided"
    )


class CreateContractSubscriptionRequest(BaseModel):
    dataContractId: UUID = Field(..., description="Unique identifier of the contract")
    userId: Optional[UUID] = Field(
        None, description="The unique identifier of the user"
    )
    email: Optional[str] = Field(
        None,
        description="The email address of the subscriber if provided",
        regex="^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$",
    )
    githubHandle: Optional[str] = Field(
        None, description="The GitHub handle of the subscriber if provided"
    )


class GetContractSubscriptionsResponse(BaseModel):
    __root__: List[ContractSubscription]


class Type3(Enum):
    SNOWFLAKE = "SNOWFLAKE"


class BaseSnowflakeLineageIntegrationConfig(BaseModel):
    type: Type3 = Field(..., description="Type of the lineage integration")
    account_id: str = Field(..., description="Snowflake account id")
    warehouse: str = Field(..., description="Snowflake warehouse", regex="^\\S{1,255}$")
    role: str = Field(..., description="Snowflake role", regex="^\\S{1,255}$")
    table_ignore_patterns: Optional[List[str]] = Field(
        None,
        description="Optional list of regex patterns to ignore tables when syncing schema & lineage",
    )


class GetSnowflakeCredentials(BaseModel):
    username: str = Field(..., description="Snowflake username", regex="^\\S{1,255}$")


class SnowflakePasswordCredentials(GetSnowflakeCredentials):
    password: str = Field(
        ...,
        description="Password for the Snowflake user",
        regex="^(?=.*\\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$",
    )


class SnowflakeKeyPairCredentials(GetSnowflakeCredentials):
    private_key_base64: str = Field(..., description="Base64 encoded private key")
    private_key_passphrase: Optional[str] = Field(
        None, description="Optional private key passphrase"
    )


class CreateOrUpdateSnowflakeLineageIntegrationConfig1(
    BaseSnowflakeLineageIntegrationConfig
):
    pass


class CreateOrUpdateSnowflakeLineageIntegrationConfig2(
    SnowflakePasswordCredentials, CreateOrUpdateSnowflakeLineageIntegrationConfig1
):
    pass


class CreateOrUpdateSnowflakeLineageIntegrationConfig3(
    SnowflakeKeyPairCredentials, CreateOrUpdateSnowflakeLineageIntegrationConfig1
):
    pass


class CreateOrUpdateSnowflakeLineageIntegrationConfig(BaseModel):
    __root__: Union[
        CreateOrUpdateSnowflakeLineageIntegrationConfig2,
        CreateOrUpdateSnowflakeLineageIntegrationConfig3,
    ]


class Type4(Enum):
    BIG_QUERY = "BIG_QUERY"


class BaseBigQueryLineageIntegrationConfig(BaseModel):
    type: Type4 = Field(..., description="Type of the lineage integration")
    project_id: str = Field(
        ...,
        description="BigQuery project id",
        regex="^[a-z][-a-z0-9]{4,28}[a-z0-9]{1}$",
    )
    table_ignore_patterns: Optional[List[str]] = Field(
        None,
        description="Optional list of regex patterns to ignore tables when syncing schema & lineage",
    )


class GetBigQueryCredentials(BaseModel):
    service_account_email: str = Field(
        ...,
        description="BigQuery service account email",
        regex="^[a-z0-9-]{6,30}@[a-z][-a-z0-9]{4,28}[a-z0-9]{1}\\.iam\\.gserviceaccount\\.com$",
    )
    service_account_id: str = Field(
        ..., description="BigQuery service account id", regex="^[a-z0-9-]{6,30}$"
    )
    service_account_private_key_id: str = Field(
        ..., description="BigQuery service account private key id"
    )


class BigQueryServiceAccountKeyCredentials(GetBigQueryCredentials):
    service_account_private_key_base64: str = Field(
        ...,
        description="Base64 encoded private key",
        regex="^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{4})$",
    )


class CreateOrUpdateBigQueryLineageIntegrationConfig(
    BaseBigQueryLineageIntegrationConfig, BigQueryServiceAccountKeyCredentials
):
    pass


class CreateOrUpdateLineageIntegrationRequest(BaseModel):
    name: str = Field(..., description="Name of the lineage integration")
    scheduleCron: str = Field(
        ...,
        description="Cron expression used to schedule runs of the lineage integration",
        regex="^((((\\d+,)+\\d+|(\\d+(/|-|#)\\d+)|\\d+L?|\\*(/\\d+)?|L(-\\d+)?|\\?|[A-Z]{3}(-[A-Z]{3})?) ?){5,7})$",
    )
    config: Union[
        CreateOrUpdateSnowflakeLineageIntegrationConfig,
        CreateOrUpdateBigQueryLineageIntegrationConfig,
    ] = Field(..., description="Configuration for the lineage integration")


class CreateOrUpdateLineageIntegrationResponse(BaseModel):
    id: str = Field(..., description="ID of the created or updated lineage integration")


class GetSnowflakeLineageIntegrationConfig(
    BaseSnowflakeLineageIntegrationConfig, GetSnowflakeCredentials
):
    pass


class GetBigQueryLineageIntegrationConfig(
    BaseBigQueryLineageIntegrationConfig, GetBigQueryCredentials
):
    pass


class GetLineageIntegrationResponse(BaseModel):
    id: str = Field(..., description="ID of the lineage integration")
    name: str = Field(..., description="Name of the lineage integration")
    scheduleCron: str = Field(
        ...,
        description="Cron expression used to schedule runs of the lineage integration",
    )
    config: Union[
        GetSnowflakeLineageIntegrationConfig, GetBigQueryLineageIntegrationConfig
    ] = Field(..., description="Configuration for the lineage integration")


class GetLineageIntegrationsResponse(BaseModel):
    __root__: List[GetLineageIntegrationResponse]


class TestLineageIntegrationRequest(BaseModel):
    name: str = Field(..., description="Name of the lineage integration")
    config: Union[
        CreateOrUpdateSnowflakeLineageIntegrationConfig,
        CreateOrUpdateBigQueryLineageIntegrationConfig,
    ] = Field(..., description="Configuration for the lineage integration")


class TestLineageIntegrationResponse(BaseModel):
    success: bool = Field(
        ..., description="a boolean indicating if the lineage integration is valid"
    )
    message: Optional[str] = Field(
        None, description="a message indicating why the lineage integration is invalid"
    )


class DataAssetSearchResult(BaseModel):
    id: str = Field(
        ...,
        description="The ID of the data asset a concatenation of the namespace and name.",
        example="dataset:food_delivery:public.delivery_7_days",
    )
    type: Optional[str] = Field(
        None, description="Type of the data asset. It can be either `dataset` or `job`."
    )
    namespace: str = Field(
        ..., description="The namespace of the dataset or job.", example="food_delivery"
    )
    name: str = Field(
        ..., description="The name of the dataset.", example="public.delivery_7_days"
    )
    updatedAt: Optional[str] = Field(
        None,
        description="An [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) timestamp representing the date/time the dataset or job was updated.",
        example="2019-05-09T19:49:24.201361Z",
    )
    nodeId: Optional[str] = Field(
        None,
        description="The ID of the node. A node can either be a dataset node or a job node. The format of nodeId for dataset is `dataset:<namespace_of_dataset>:<name_of_the_dataset>` and for job is `job:<namespace_of_the_job>:<name_of_the_job>`.",
        example="dataset:food_delivery:public.delivery_7_days",
    )


class DataAssetId(BaseModel):
    __root__: str = Field(
        ...,
        description="The unique identifier of the data asset. It follows the pattern '{data_asset_type}://{data_asset_source}:{data_asset_name}'",
        regex="^(protobuf|avro|json_schema|postgres|mysql|snowflake|bigquery)://(?=.*[a-zA-Z0-9])[a-zA-Z0-9_@\\.:/-]+:(?=.*[a-zA-Z0-9])[a-zA-Z0-9_\\./-]+$",
    )


class MarquezId(BaseModel):
    namespace: str = Field(..., description="The namespace of the Marquez dataset.")
    name: str = Field(..., description="The name of the Marquez dataset.")


class FieldModel(BaseModel):
    name: str = Field(..., description="The name of the field.")
    type: str = Field(..., description="The data type of the field.")
    tags: Optional[List[str]] = Field(None, description="List of tags.")
    description: Optional[str] = Field(
        None, description="The description of the field."
    )


class DataAsset(BaseModel):
    id: DataAssetId
    marquezId: MarquezId = Field(..., description="The ID of the dataset.")
    type: str = Field(..., description="The type of the data asset.")
    name: str = Field(..., description="The **logical** name of the data asset.")
    physicalName: Optional[str] = Field(
        None, description="The **physical** name of the data asset."
    )
    createdAt: Optional[datetime] = Field(
        None,
        description="An [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) timestamp representing the date/time the data asset was created.",
    )
    updatedAt: Optional[datetime] = Field(
        None,
        description="An [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) timestamp representing the date/time the data asset was updated.",
    )
    namespace: Optional[str] = Field(
        None, description="The namespace of the data asset."
    )
    sourceName: Optional[str] = Field(
        None, description="The name of the source associated with the data asset."
    )
    fields: List[FieldModel] = Field(..., description="The fields of the data asset.")
    owners: List[str] = Field(
        ..., description="The email addresses of the owners of the data asset."
    )
    dataContractIds: List[UUID] = Field(
        ..., description="The contract IDs associated with the data asset."
    )
    tags: Optional[List[str]] = Field(None, description="List of tags.")
    lastModifiedAt: Optional[datetime] = Field(
        None,
        description="An [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) timestamp representing the date/time the data asset was last modified by a successful run.",
    )
    description: str = Field(..., description="The description of the data asset.")
    currentVersion: Optional[UUID] = Field(
        None, description="The current version of the data asset."
    )
    deleted: Optional[bool] = Field(
        None, description="The deleted state of the data asset."
    )
    isUnderContract: Optional[bool] = Field(
        None, description="Does the data asset have an associated contract."
    )


class CreateOrUpdateDataAssetResponse(BaseModel):
    id: str = Field(..., description="ID of the created or updated data asset")


class Input(BaseModel):
    sourceName: str
    sourceType: str
    schemaContents: str
    realDbName: Optional[str] = None
    realDbSchema: Optional[str] = None


class ResponseType(Enum):
    DETAILED = "DETAILED"
    COMMENT_MARKDOWN = "COMMENT_MARKDOWN"


class CheckDataAssetsRequest(BaseModel):
    inputs: List[Input]
    responseType: ResponseType = Field(
        ...,
        description="Determines the format of the response from the API. Defaults to 'DETAILED' which returns a detailed JSON object for each data asset checked. If 'COMMENT_MARKDOWN' is specified, the response will be a markdown string intended to be used as a comment in a pull request.",
    )


class ResponseType1(Enum):
    NO_CONTRACT = "NO_CONTRACT"


class CheckDataAssetNoContractResponse(BaseModel):
    dataAssetNamespace: str = Field(
        ...,
        description="The namespace of the data asset",
        examples=[
            "postgres://service-one.aaa.eu-west-1.rds.amazonaws.com:5432",
            "protobuf://github.com/org/repo/path/to/file.proto",
        ],
    )
    dataAssetResourceName: str = Field(
        ...,
        description="The full resource name of the data asset, see [Data Assets](https://docs.gable.ai/data_assets_and_lineage/data_assets)",
        examples=[
            "postgres://service-one.aaa.eu-west-1.rds.amazonaws.com:5432:serviceone.public.sales",
            "protobuf://git@github.com/org/repo/path/to/file.proto:company.serviceone.Sales",
        ],
    )
    dataAssetPath: str = Field(
        ...,
        description="The relative path of the data asset within its data store",
        examples=["serviceone.public.sales", "company.serviceone.Sales"],
    )
    responseType: ResponseType1


class ContractViolationType(Enum):
    MISSING_REQUIRED_PROPERTY = "MISSING_REQUIRED_PROPERTY"
    INCOMPATIBLE_TYPE = "INCOMPATIBLE_TYPE"


class Violation(BaseModel):
    message: str
    field: str
    fieldType: str
    violationType: ContractViolationType
    expected: str
    actual: Optional[str] = None


class Subscriber(BaseModel):
    email: Optional[str] = None
    githubHandle: Optional[str] = None


class ResponseType2(Enum):
    DETAILED = "DETAILED"


class CheckDataAssetDetailedResponse(BaseModel):
    dataAssetNamespace: str = Field(
        ...,
        description="The namespace of the data asset",
        examples=[
            "postgres://service-one.aaa.eu-west-1.rds.amazonaws.com:5432",
            "protobuf://github.com/org/repo/path/to/file.proto",
        ],
    )
    dataAssetResourceName: str = Field(
        ...,
        description="The full resource name of the data asset, see [Data Assets](https://docs.gable.ai/data_assets_and_lineage/data_assets)",
        examples=[
            "postgres://service-one.aaa.eu-west-1.rds.amazonaws.com:5432:serviceone.public.sales",
            "protobuf://git@github.com/org/repo/path/to/file.proto:company.serviceone.Sales",
        ],
    )
    dataAssetPath: str = Field(
        ...,
        description="The relative path of the data asset within its data store",
        examples=["serviceone.public.sales", "company.serviceone.Sales"],
    )
    contractId: UUID
    contractUrl: str = Field(..., description="Link to the contract in the Gable UI")
    contractNamespace: str
    contractName: str
    contractOwner: str
    contractOwnerGithubHandle: Optional[str] = None
    violations: Optional[List[Violation]] = None
    subscribers: List[Subscriber]
    responseType: ResponseType2
    notificationLevel: Optional[NotificationLevel] = Field(
        "INACTIVE", description="alert level for contract"
    )


class ResponseType3(Enum):
    ERROR = "ERROR"


class CheckDataAssetErrorResponse(BaseModel):
    dataAssetNamespace: str = Field(
        ...,
        description="The namespace of the data asset",
        examples=[
            "postgres://service-one.aaa.eu-west-1.rds.amazonaws.com:5432",
            "protobuf://github.com/org/repo/path/to/file.proto",
        ],
    )
    dataAssetResourceName: Optional[str] = Field(
        None,
        description="The full resource name of the data asset, see [Data Assets](https://docs.gable.ai/data_assets_and_lineage/data_assets)",
        examples=[
            "postgres://service-one.aaa.eu-west-1.rds.amazonaws.com:5432:serviceone.public.sales",
            "protobuf://git@github.com/org/repo/path/to/file.proto:company.serviceone.Sales",
        ],
    )
    dataAssetPath: Optional[str] = Field(
        None,
        description="The relative path of the data asset within its data store",
        examples=["serviceone.public.sales", "company.serviceone.Sales"],
    )
    message: str = Field(..., description="The error message")
    responseType: ResponseType3
    notificationLevel: Optional[NotificationLevel] = Field(
        "INACTIVE", description="notification tier of error response"
    )


class ResponseType4(Enum):
    COMMENT_MARKDOWN = "COMMENT_MARKDOWN"


class CheckDataAssetCommentMarkdownResponse(BaseModel):
    markdown: Optional[str] = None
    errors: Optional[List[CheckDataAssetErrorResponse]] = None
    responseType: ResponseType4


class CheckDataAssetRequest(BaseModel):
    sourceName: str
    sourceType: str
    schemaContents: str
    realDbName: Optional[str] = None
    realDbSchema: Optional[str] = None


class CheckDataAssetResponse(BaseModel):
    message: str


class ErrorResponseDeprecated(BaseModel):
    id: Optional[float] = None
    title: Optional[str] = None
    message: str
    success: Optional[bool] = None


class IngestDataAssetRequest(BaseModel):
    sourceType: str = Field(
        ..., description="The type of the source (e.g. postgres, avro, protobuf, etc.)"
    )
    sourceNames: List[str] = Field(..., description="The names of the sources")
    databaseSchema: str = Field(..., description="The name of the database schema")
    schema_: List[str] = Field(
        ...,
        alias="schema",
        description="Array of schemas. Each schema could be from a db information schema or the contents of a schema file.",
    )


class IngestDataAssetResponse(BaseModel):
    message: str = Field(..., description="Response message")
    registered: List[str] = Field(
        ..., description="List of the registered data asset ids"
    )
    success: bool = Field(..., description="Whether the request was successful")


class InferContractFromDataAssetResponse(BaseModel):
    contractId: UUID = Field(
        ..., description="Unique identifier for the contract in UUID format"
    )
    version: Optional[str] = Field(
        None, description="Version of the contract (semantic versioning)"
    )
    status: Optional[Status] = Field(None, description="status of the contract")
    gitHash: Optional[str] = Field(
        None,
        description="full length git hash corresponding to the commit this contract was added/updated",
        max_length=40,
        min_length=40,
    )
    gitRepo: Optional[AnyUrl] = Field(
        None, description="full link to the git repo this contract lives in"
    )
    gitUser: Optional[str] = Field(
        None, description="git user who added/updated this contract"
    )
    fileUri: Optional[AnyUrl] = Field(
        None,
        description="full link to the file in the repo that contains this contract",
    )
    reviewers: Optional[List[str]] = Field(
        None,
        description="optional list of users who reviewed the merged PR that this contract added/updated in",
    )
    mergedAt: Optional[datetime] = Field(
        None,
        description="date time at which the PR that added/updated this contract was merged",
    )
    createdAt: Optional[datetime] = Field(
        None, description="date time at which the contract was created"
    )
    updatedAt: Optional[datetime] = Field(
        None, description="date time at which the contract was last updated"
    )
    contractSpec: Dict[str, Any] = Field(..., description="contract spec")
    contractSpecRaw: str = Field(..., description="contract spec raw json")


class GetAvailableLineageIntegrationsResponse(BaseModel):
    __root__: List[str]


class GetAvailableLineageIntegrationDetailsResponseItem(BaseModel):
    instructions: Optional[str] = Field(
        None, description="Instructions for setting up the lineage integration"
    )
    requiredInputs: Optional[List[str]] = Field(
        None, description="Required inputs for setting up the lineage integration"
    )


class GetAvailableLineageIntegrationDetailsResponse(BaseModel):
    __root__: List[GetAvailableLineageIntegrationDetailsResponseItem]


class GetApiKeysResponseItem(BaseModel):
    id: Optional[str] = Field(None, description="The identifier of the API key")
    name: Optional[str] = Field(None, description="The name of the API key")
    value: Optional[str] = Field(None, description="The value of the API key")


class GetApiKeysResponse(BaseModel):
    __root__: List[GetApiKeysResponseItem]


class GetSsoSamlSetupDetailsResponse(BaseModel):
    ssoUrl: str = Field(
        ...,
        description="The location where the SAML assertion is sent with a HTTP POST, also referred to as the SAML Assertion Consumer Service (ACS) URL.",
    )
    audienceUri: str = Field(
        ...,
        description="(SP Entity Id) The application-defined unique identifier that is the intended audience of the SAML assertion. This is most often the SP Entity ID of your application.",
    )


class Type5(Enum):
    SAML = "SAML"


class SsoSamlUrlConfig(BaseModel):
    type: Type5 = Field(
        ...,
        description="The type of SSO integration, currently only SAML is supported.",
    )
    identityProvider: str = Field(
        ...,
        description='The name of your identity provider. This value will be displayed to users when they log in. \n\nNote: This value cannot be the strings "Google" or "SAML" as they\'re reserved words in our identity management platform.\n',
        examples=["Okta", "GoogleWorkspace", "OneLogin", "JumpCloud"],
        regex="^(?=[a-zA-Z0-9\\(\\)\\.\\-!@]+$)(?!Google|SAML$).*$",
    )
    metadataDocumentEndpointUrl: str = Field(
        ...,
        description="The URL of the SAML metadata document. Either this or metadataFileContents must be provided.",
        example="https://company.okta.com/app/123456789/sso/saml/metadata",
    )


class SsoSamlFileConfig(BaseModel):
    type: Type5 = Field(
        ...,
        description="The type of SSO integration, currently only SAML is supported.",
    )
    identityProvider: str = Field(
        ...,
        description='The name of your identity provider. This value will be displayed to users when they log in. \n\nNote: This value cannot be the strings "Google" or "SAML" as they\'re reserved words in our identity management platform.\n',
        examples=["Okta", "GoogleWorkspace", "OneLogin", "JumpCloud"],
        regex="^(?=[a-zA-Z0-9\\(\\)\\.\\-!@]+$)(?!Google|SAML$).*$",
    )
    metadataFileContents: str = Field(
        ...,
        description="The contents of the metadata document. Either this or metadataDocumentEndpointUrl must be provided.",
    )


class SsoConfig(BaseModel):
    __root__: Union[SsoSamlUrlConfig, SsoSamlFileConfig]


class GetUserRequest(BaseModel):
    email: str = Field(
        ...,
        description="The email address of the user, which is the primary ID in Gable",
        regex="^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$",
    )


class GetUserResponse(BaseModel):
    email: str = Field(
        ...,
        description="The email address of the user",
        regex="^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$",
    )
    firstName: Optional[str] = Field(
        None, description="The first name of the user, if available"
    )
    lastName: Optional[str] = Field(
        None, description="The last name of the user, if available"
    )
    githubHandle: Optional[str] = Field(
        None, description="The GitHub handle of the user or team, if available"
    )


class UpdateUserRequest(BaseModel):
    email: str = Field(
        ...,
        description="The email address of the user, which is the primary ID in Gable",
        regex="^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$",
    )
    firstName: Optional[str] = Field(None, description="The first name of the user")
    lastName: Optional[str] = Field(None, description="The last name of the user")
    githubHandle: Optional[str] = Field(
        None, description="The GitHub handle of the user"
    )


class UpdateUserResponse(BaseModel):
    email: str = Field(
        ...,
        description="The email address of the user, which is the primary ID in Gable",
        regex="^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$",
    )
    firstName: Optional[str] = Field(None, description="The first name of the user")
    lastName: Optional[str] = Field(None, description="The last name of the user")
    githubHandle: Optional[str] = Field(
        None, description="The GitHub handle of the user"
    )


class GetUsersResponseItem(BaseModel):
    email: str = Field(
        ...,
        description="The email address of the user, which is the primary ID in Gable",
        regex="^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$",
    )
    firstName: Optional[str] = Field(
        None, description="The first name of the user, if available"
    )
    lastName: Optional[str] = Field(
        None, description="The last name of the user, if available"
    )


class GetUsersResponse(BaseModel):
    __root__: List[GetUsersResponseItem]


class InviteUserRequest(BaseModel):
    email: str = Field(
        ...,
        description="The email address of the user, which is the primary ID in Gable",
        regex="^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$",
    )
    firstName: Optional[str] = Field(None, description="The first name of the user")
    lastName: Optional[str] = Field(None, description="The last name of the user")


class DeleteUserRequest(BaseModel):
    email: str = Field(
        ...,
        description="The email address of the user, which is the primary ID in Gable",
        regex="^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$",
    )
