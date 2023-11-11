from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HashAlgorithm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN: _ClassVar[HashAlgorithm]
    MD5: _ClassVar[HashAlgorithm]
    SHA1: _ClassVar[HashAlgorithm]
    SHA256: _ClassVar[HashAlgorithm]
    SHA384: _ClassVar[HashAlgorithm]
    SHA512: _ClassVar[HashAlgorithm]
    SHA3_256: _ClassVar[HashAlgorithm]
    SHA3_384: _ClassVar[HashAlgorithm]
    SHA3_512: _ClassVar[HashAlgorithm]
    BLAKE2B_256: _ClassVar[HashAlgorithm]
    BLAKE2B_384: _ClassVar[HashAlgorithm]
    BLAKE2B_512: _ClassVar[HashAlgorithm]
    BLAKE3: _ClassVar[HashAlgorithm]
    MD2: _ClassVar[HashAlgorithm]
    ADLER32: _ClassVar[HashAlgorithm]
    MD4: _ClassVar[HashAlgorithm]
    MD6: _ClassVar[HashAlgorithm]
    SHA224: _ClassVar[HashAlgorithm]

class SoftwareIdentifierType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN_IDENTIFIER_TYPE: _ClassVar[SoftwareIdentifierType]
    PURL: _ClassVar[SoftwareIdentifierType]
    CPE22: _ClassVar[SoftwareIdentifierType]
    CPE23: _ClassVar[SoftwareIdentifierType]
    GITOID: _ClassVar[SoftwareIdentifierType]

class Purpose(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN_PURPOSE: _ClassVar[Purpose]
    APPLICATION: _ClassVar[Purpose]
    ARCHIVE: _ClassVar[Purpose]
    BOM: _ClassVar[Purpose]
    CONFIGURATION: _ClassVar[Purpose]
    CONTAINER: _ClassVar[Purpose]
    DATA: _ClassVar[Purpose]
    DEVICE: _ClassVar[Purpose]
    DEVICE_DRIVER: _ClassVar[Purpose]
    DOCUMENTATION: _ClassVar[Purpose]
    EVIDENCE: _ClassVar[Purpose]
    EXECUTABLE: _ClassVar[Purpose]
    FILE: _ClassVar[Purpose]
    FIRMWARE: _ClassVar[Purpose]
    FRAMEWORK: _ClassVar[Purpose]
    INSTALL: _ClassVar[Purpose]
    LIBRARY: _ClassVar[Purpose]
    MACHINE_LEARNING_MODEL: _ClassVar[Purpose]
    MANIFEST: _ClassVar[Purpose]
    MODEL: _ClassVar[Purpose]
    MODULE: _ClassVar[Purpose]
    OPERATING_SYSTEM: _ClassVar[Purpose]
    OTHER: _ClassVar[Purpose]
    PATCH: _ClassVar[Purpose]
    PLATFORM: _ClassVar[Purpose]
    REQUIREMENT: _ClassVar[Purpose]
    SOURCE: _ClassVar[Purpose]
    SPECIFICATION: _ClassVar[Purpose]
    TEST: _ClassVar[Purpose]
UNKNOWN: HashAlgorithm
MD5: HashAlgorithm
SHA1: HashAlgorithm
SHA256: HashAlgorithm
SHA384: HashAlgorithm
SHA512: HashAlgorithm
SHA3_256: HashAlgorithm
SHA3_384: HashAlgorithm
SHA3_512: HashAlgorithm
BLAKE2B_256: HashAlgorithm
BLAKE2B_384: HashAlgorithm
BLAKE2B_512: HashAlgorithm
BLAKE3: HashAlgorithm
MD2: HashAlgorithm
ADLER32: HashAlgorithm
MD4: HashAlgorithm
MD6: HashAlgorithm
SHA224: HashAlgorithm
UNKNOWN_IDENTIFIER_TYPE: SoftwareIdentifierType
PURL: SoftwareIdentifierType
CPE22: SoftwareIdentifierType
CPE23: SoftwareIdentifierType
GITOID: SoftwareIdentifierType
UNKNOWN_PURPOSE: Purpose
APPLICATION: Purpose
ARCHIVE: Purpose
BOM: Purpose
CONFIGURATION: Purpose
CONTAINER: Purpose
DATA: Purpose
DEVICE: Purpose
DEVICE_DRIVER: Purpose
DOCUMENTATION: Purpose
EVIDENCE: Purpose
EXECUTABLE: Purpose
FILE: Purpose
FIRMWARE: Purpose
FRAMEWORK: Purpose
INSTALL: Purpose
LIBRARY: Purpose
MACHINE_LEARNING_MODEL: Purpose
MANIFEST: Purpose
MODEL: Purpose
MODULE: Purpose
OPERATING_SYSTEM: Purpose
OTHER: Purpose
PATCH: Purpose
PLATFORM: Purpose
REQUIREMENT: Purpose
SOURCE: Purpose
SPECIFICATION: Purpose
TEST: Purpose

class Document(_message.Message):
    __slots__ = ("metadata", "node_list")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    NODE_LIST_FIELD_NUMBER: _ClassVar[int]
    metadata: Metadata
    node_list: NodeList
    def __init__(self, metadata: _Optional[_Union[Metadata, _Mapping]] = ..., node_list: _Optional[_Union[NodeList, _Mapping]] = ...) -> None: ...

class Node(_message.Message):
    __slots__ = ("id", "type", "name", "version", "file_name", "url_home", "url_download", "licenses", "license_concluded", "license_comments", "copyright", "source_info", "comment", "summary", "description", "attribution", "suppliers", "originators", "release_date", "build_date", "valid_until_date", "external_references", "file_types", "identifiers", "hashes", "primary_purpose")
    class NodeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PACKAGE: _ClassVar[Node.NodeType]
        FILE: _ClassVar[Node.NodeType]
    PACKAGE: Node.NodeType
    FILE: Node.NodeType
    class IdentifiersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    class HashesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    URL_HOME_FIELD_NUMBER: _ClassVar[int]
    URL_DOWNLOAD_FIELD_NUMBER: _ClassVar[int]
    LICENSES_FIELD_NUMBER: _ClassVar[int]
    LICENSE_CONCLUDED_FIELD_NUMBER: _ClassVar[int]
    LICENSE_COMMENTS_FIELD_NUMBER: _ClassVar[int]
    COPYRIGHT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_INFO_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTION_FIELD_NUMBER: _ClassVar[int]
    SUPPLIERS_FIELD_NUMBER: _ClassVar[int]
    ORIGINATORS_FIELD_NUMBER: _ClassVar[int]
    RELEASE_DATE_FIELD_NUMBER: _ClassVar[int]
    BUILD_DATE_FIELD_NUMBER: _ClassVar[int]
    VALID_UNTIL_DATE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_REFERENCES_FIELD_NUMBER: _ClassVar[int]
    FILE_TYPES_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIERS_FIELD_NUMBER: _ClassVar[int]
    HASHES_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_PURPOSE_FIELD_NUMBER: _ClassVar[int]
    id: str
    type: Node.NodeType
    name: str
    version: str
    file_name: str
    url_home: str
    url_download: str
    licenses: _containers.RepeatedScalarFieldContainer[str]
    license_concluded: str
    license_comments: str
    copyright: str
    source_info: str
    comment: str
    summary: str
    description: str
    attribution: _containers.RepeatedScalarFieldContainer[str]
    suppliers: _containers.RepeatedCompositeFieldContainer[Person]
    originators: _containers.RepeatedCompositeFieldContainer[Person]
    release_date: _timestamp_pb2.Timestamp
    build_date: _timestamp_pb2.Timestamp
    valid_until_date: _timestamp_pb2.Timestamp
    external_references: _containers.RepeatedCompositeFieldContainer[ExternalReference]
    file_types: _containers.RepeatedScalarFieldContainer[str]
    identifiers: _containers.ScalarMap[int, str]
    hashes: _containers.ScalarMap[int, str]
    primary_purpose: _containers.RepeatedScalarFieldContainer[Purpose]
    def __init__(self, id: _Optional[str] = ..., type: _Optional[_Union[Node.NodeType, str]] = ..., name: _Optional[str] = ..., version: _Optional[str] = ..., file_name: _Optional[str] = ..., url_home: _Optional[str] = ..., url_download: _Optional[str] = ..., licenses: _Optional[_Iterable[str]] = ..., license_concluded: _Optional[str] = ..., license_comments: _Optional[str] = ..., copyright: _Optional[str] = ..., source_info: _Optional[str] = ..., comment: _Optional[str] = ..., summary: _Optional[str] = ..., description: _Optional[str] = ..., attribution: _Optional[_Iterable[str]] = ..., suppliers: _Optional[_Iterable[_Union[Person, _Mapping]]] = ..., originators: _Optional[_Iterable[_Union[Person, _Mapping]]] = ..., release_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., build_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., valid_until_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., external_references: _Optional[_Iterable[_Union[ExternalReference, _Mapping]]] = ..., file_types: _Optional[_Iterable[str]] = ..., identifiers: _Optional[_Mapping[int, str]] = ..., hashes: _Optional[_Mapping[int, str]] = ..., primary_purpose: _Optional[_Iterable[_Union[Purpose, str]]] = ...) -> None: ...

class Metadata(_message.Message):
    __slots__ = ("id", "version", "name", "date", "tools", "authors", "comment", "documentTypes")
    ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    TOOLS_FIELD_NUMBER: _ClassVar[int]
    AUTHORS_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    DOCUMENTTYPES_FIELD_NUMBER: _ClassVar[int]
    id: str
    version: str
    name: str
    date: _timestamp_pb2.Timestamp
    tools: _containers.RepeatedCompositeFieldContainer[Tool]
    authors: _containers.RepeatedCompositeFieldContainer[Person]
    comment: str
    documentTypes: _containers.RepeatedCompositeFieldContainer[DocumentType]
    def __init__(self, id: _Optional[str] = ..., version: _Optional[str] = ..., name: _Optional[str] = ..., date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., tools: _Optional[_Iterable[_Union[Tool, _Mapping]]] = ..., authors: _Optional[_Iterable[_Union[Person, _Mapping]]] = ..., comment: _Optional[str] = ..., documentTypes: _Optional[_Iterable[_Union[DocumentType, _Mapping]]] = ...) -> None: ...

class Edge(_message.Message):
    __slots__ = ("type", "to")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[Edge.Type]
        amends: _ClassVar[Edge.Type]
        ancestor: _ClassVar[Edge.Type]
        buildDependency: _ClassVar[Edge.Type]
        buildTool: _ClassVar[Edge.Type]
        contains: _ClassVar[Edge.Type]
        contained_by: _ClassVar[Edge.Type]
        copy: _ClassVar[Edge.Type]
        dataFile: _ClassVar[Edge.Type]
        dependencyManifest: _ClassVar[Edge.Type]
        dependsOn: _ClassVar[Edge.Type]
        dependencyOf: _ClassVar[Edge.Type]
        descendant: _ClassVar[Edge.Type]
        describes: _ClassVar[Edge.Type]
        describedBy: _ClassVar[Edge.Type]
        devDependency: _ClassVar[Edge.Type]
        devTool: _ClassVar[Edge.Type]
        distributionArtifact: _ClassVar[Edge.Type]
        documentation: _ClassVar[Edge.Type]
        dynamicLink: _ClassVar[Edge.Type]
        example: _ClassVar[Edge.Type]
        expandedFromArchive: _ClassVar[Edge.Type]
        fileAdded: _ClassVar[Edge.Type]
        fileDeleted: _ClassVar[Edge.Type]
        fileModified: _ClassVar[Edge.Type]
        generates: _ClassVar[Edge.Type]
        generatedFrom: _ClassVar[Edge.Type]
        metafile: _ClassVar[Edge.Type]
        optionalComponent: _ClassVar[Edge.Type]
        optionalDependency: _ClassVar[Edge.Type]
        other: _ClassVar[Edge.Type]
        packages: _ClassVar[Edge.Type]
        patch: _ClassVar[Edge.Type]
        prerequisite: _ClassVar[Edge.Type]
        prerequisiteFor: _ClassVar[Edge.Type]
        providedDependency: _ClassVar[Edge.Type]
        requirementFor: _ClassVar[Edge.Type]
        runtimeDependency: _ClassVar[Edge.Type]
        specificationFor: _ClassVar[Edge.Type]
        staticLink: _ClassVar[Edge.Type]
        test: _ClassVar[Edge.Type]
        testCase: _ClassVar[Edge.Type]
        testDependency: _ClassVar[Edge.Type]
        testTool: _ClassVar[Edge.Type]
        variant: _ClassVar[Edge.Type]
    UNKNOWN: Edge.Type
    amends: Edge.Type
    ancestor: Edge.Type
    buildDependency: Edge.Type
    buildTool: Edge.Type
    contains: Edge.Type
    contained_by: Edge.Type
    copy: Edge.Type
    dataFile: Edge.Type
    dependencyManifest: Edge.Type
    dependsOn: Edge.Type
    dependencyOf: Edge.Type
    descendant: Edge.Type
    describes: Edge.Type
    describedBy: Edge.Type
    devDependency: Edge.Type
    devTool: Edge.Type
    distributionArtifact: Edge.Type
    documentation: Edge.Type
    dynamicLink: Edge.Type
    example: Edge.Type
    expandedFromArchive: Edge.Type
    fileAdded: Edge.Type
    fileDeleted: Edge.Type
    fileModified: Edge.Type
    generates: Edge.Type
    generatedFrom: Edge.Type
    metafile: Edge.Type
    optionalComponent: Edge.Type
    optionalDependency: Edge.Type
    other: Edge.Type
    packages: Edge.Type
    patch: Edge.Type
    prerequisite: Edge.Type
    prerequisiteFor: Edge.Type
    providedDependency: Edge.Type
    requirementFor: Edge.Type
    runtimeDependency: Edge.Type
    specificationFor: Edge.Type
    staticLink: Edge.Type
    test: Edge.Type
    testCase: Edge.Type
    testDependency: Edge.Type
    testTool: Edge.Type
    variant: Edge.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    type: Edge.Type
    to: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, type: _Optional[_Union[Edge.Type, str]] = ..., to: _Optional[_Iterable[str]] = ..., **kwargs) -> None: ...

class ExternalReference(_message.Message):
    __slots__ = ("url", "type", "comment", "authority", "hashes")
    class HashesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    URL_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    AUTHORITY_FIELD_NUMBER: _ClassVar[int]
    HASHES_FIELD_NUMBER: _ClassVar[int]
    url: str
    type: str
    comment: str
    authority: str
    hashes: _containers.ScalarMap[int, str]
    def __init__(self, url: _Optional[str] = ..., type: _Optional[str] = ..., comment: _Optional[str] = ..., authority: _Optional[str] = ..., hashes: _Optional[_Mapping[int, str]] = ...) -> None: ...

class Person(_message.Message):
    __slots__ = ("name", "is_org", "email", "url", "phone", "contacts")
    NAME_FIELD_NUMBER: _ClassVar[int]
    IS_ORG_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    CONTACTS_FIELD_NUMBER: _ClassVar[int]
    name: str
    is_org: bool
    email: str
    url: str
    phone: str
    contacts: _containers.RepeatedCompositeFieldContainer[Person]
    def __init__(self, name: _Optional[str] = ..., is_org: bool = ..., email: _Optional[str] = ..., url: _Optional[str] = ..., phone: _Optional[str] = ..., contacts: _Optional[_Iterable[_Union[Person, _Mapping]]] = ...) -> None: ...

class Tool(_message.Message):
    __slots__ = ("name", "version", "vendor")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    VENDOR_FIELD_NUMBER: _ClassVar[int]
    name: str
    version: str
    vendor: str
    def __init__(self, name: _Optional[str] = ..., version: _Optional[str] = ..., vendor: _Optional[str] = ...) -> None: ...

class DocumentType(_message.Message):
    __slots__ = ("type", "name", "description")
    class SBOMType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OTHER: _ClassVar[DocumentType.SBOMType]
        DESIGN: _ClassVar[DocumentType.SBOMType]
        SOURCE: _ClassVar[DocumentType.SBOMType]
        BUILD: _ClassVar[DocumentType.SBOMType]
        ANALYZED: _ClassVar[DocumentType.SBOMType]
        DEPLOYED: _ClassVar[DocumentType.SBOMType]
        RUNTIME: _ClassVar[DocumentType.SBOMType]
        DISCOVERY: _ClassVar[DocumentType.SBOMType]
        DECOMISSION: _ClassVar[DocumentType.SBOMType]
    OTHER: DocumentType.SBOMType
    DESIGN: DocumentType.SBOMType
    SOURCE: DocumentType.SBOMType
    BUILD: DocumentType.SBOMType
    ANALYZED: DocumentType.SBOMType
    DEPLOYED: DocumentType.SBOMType
    RUNTIME: DocumentType.SBOMType
    DISCOVERY: DocumentType.SBOMType
    DECOMISSION: DocumentType.SBOMType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    type: DocumentType.SBOMType
    name: str
    description: str
    def __init__(self, type: _Optional[_Union[DocumentType.SBOMType, str]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class NodeList(_message.Message):
    __slots__ = ("nodes", "edges", "root_elements")
    NODES_FIELD_NUMBER: _ClassVar[int]
    EDGES_FIELD_NUMBER: _ClassVar[int]
    ROOT_ELEMENTS_FIELD_NUMBER: _ClassVar[int]
    nodes: _containers.RepeatedCompositeFieldContainer[Node]
    edges: _containers.RepeatedCompositeFieldContainer[Edge]
    root_elements: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, nodes: _Optional[_Iterable[_Union[Node, _Mapping]]] = ..., edges: _Optional[_Iterable[_Union[Edge, _Mapping]]] = ..., root_elements: _Optional[_Iterable[str]] = ...) -> None: ...
