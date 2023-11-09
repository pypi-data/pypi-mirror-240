"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import model.model.v1alpha.common_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class OcrObject(google.protobuf.message.Message):
    """OcrObject represents a predicted ocr object"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TEXT_FIELD_NUMBER: builtins.int
    SCORE_FIELD_NUMBER: builtins.int
    BOUNDING_BOX_FIELD_NUMBER: builtins.int
    text: builtins.str
    """OCR text"""
    score: builtins.float
    """OCR text score"""
    @property
    def bounding_box(self) -> model.model.v1alpha.common_pb2.BoundingBox:
        """OCR bounding box"""
    def __init__(
        self,
        *,
        text: builtins.str = ...,
        score: builtins.float = ...,
        bounding_box: model.model.v1alpha.common_pb2.BoundingBox | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["bounding_box", b"bounding_box"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["bounding_box", b"bounding_box", "score", b"score", "text", b"text"]) -> None: ...

global___OcrObject = OcrObject

@typing_extensions.final
class OcrInput(google.protobuf.message.Message):
    """OcrInput represents the input of ocr task"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    IMAGE_URL_FIELD_NUMBER: builtins.int
    IMAGE_BASE64_FIELD_NUMBER: builtins.int
    image_url: builtins.str
    """Image type URL"""
    image_base64: builtins.str
    """Image type base64"""
    def __init__(
        self,
        *,
        image_url: builtins.str = ...,
        image_base64: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["image_base64", b"image_base64", "image_url", b"image_url", "type", b"type"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["image_base64", b"image_base64", "image_url", b"image_url", "type", b"type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["type", b"type"]) -> typing_extensions.Literal["image_url", "image_base64"] | None: ...

global___OcrInput = OcrInput

@typing_extensions.final
class OcrInputStream(google.protobuf.message.Message):
    """OcrInputStream represents the input of ocr task when using stream method"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FILE_LENGTHS_FIELD_NUMBER: builtins.int
    CONTENT_FIELD_NUMBER: builtins.int
    @property
    def file_lengths(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """The list of file length for each uploaded binary file"""
    content: builtins.bytes
    """Content of images in bytes"""
    def __init__(
        self,
        *,
        file_lengths: collections.abc.Iterable[builtins.int] | None = ...,
        content: builtins.bytes = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["content", b"content", "file_lengths", b"file_lengths"]) -> None: ...

global___OcrInputStream = OcrInputStream

@typing_extensions.final
class OcrOutput(google.protobuf.message.Message):
    """OcrOutput represents the output of ocr task"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OBJECTS_FIELD_NUMBER: builtins.int
    @property
    def objects(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___OcrObject]:
        """A list of OCR objects"""
    def __init__(
        self,
        *,
        objects: collections.abc.Iterable[global___OcrObject] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["objects", b"objects"]) -> None: ...

global___OcrOutput = OcrOutput
