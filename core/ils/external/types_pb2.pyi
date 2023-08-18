from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

CARRIER_ACTION_PICK: CarrierActionType
CARRIER_ACTION_PUT: CarrierActionType
CARRIER_ACTION_UNKNOWN: CarrierActionType
DESCRIPTOR: _descriptor.FileDescriptor
LOCATION_PRIMARY: LocationType
LOCATION_SECONDARY: LocationType
LOCATION_UNKNOWN: LocationType

class CarrierActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class LocationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
