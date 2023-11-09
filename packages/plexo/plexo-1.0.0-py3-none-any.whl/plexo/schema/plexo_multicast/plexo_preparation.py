# THIS FILE HAS BEEN GENERATED AUTOMATICALLY BY capnpy
# do not edit by hand
# generated on 2023-11-09 05:25
# cython: language_level=2

from capnpy import ptr as _ptr
from capnpy.struct_ import Struct as _Struct
from capnpy.struct_ import check_tag as _check_tag
from capnpy.struct_ import undefined as _undefined
from capnpy.enum import enum as _enum, fill_enum as _fill_enum
from capnpy.enum import BaseEnum as _BaseEnum
from capnpy.type import Types as _Types
from capnpy.segment.segment import Segment as _Segment
from capnpy.segment.segment import MultiSegment as _MultiSegment
from capnpy.segment.builder import SegmentBuilder as _SegmentBuilder
from capnpy.list import List as _List
from capnpy.list import PrimitiveItemType as _PrimitiveItemType
from capnpy.list import BoolItemType as _BoolItemType
from capnpy.list import TextItemType as _TextItemType
from capnpy.list import TextUnicodeItemType as _TextUnicodeItemType
from capnpy.list import StructItemType as _StructItemType
from capnpy.list import EnumItemType as _EnumItemType
from capnpy.list import VoidItemType as _VoidItemType
from capnpy.list import ListItemType as _ListItemType
from capnpy.anypointer import AnyPointer as _AnyPointer
from capnpy.util import text_bytes_repr as _text_bytes_repr
from capnpy.util import text_unicode_repr as _text_unicode_repr
from capnpy.util import data_repr as _data_repr
from capnpy.util import float32_repr as _float32_repr
from capnpy.util import float64_repr as _float64_repr
from capnpy.util import extend_module_maybe as _extend_module_maybe
from capnpy.util import check_version as _check_version
from capnpy.util import encode_maybe as _encode_maybe
__capnpy_id__ = 0x8627c77e3987131a
__capnpy_version__ = '0.10.1'
__capnproto_version__ = '0.5.3.1'
# schema compiled with --no-version-check, skipping the call to _check_version
from capnpy.schema import CodeGeneratorRequest as _CodeGeneratorRequest
from capnpy.annotate import Options as _Options
from capnpy.reflection import ReflectionData as _ReflectionData
class _plexo_preparation_ReflectionData(_ReflectionData):
    request = _CodeGeneratorRequest.from_buffer(_Segment(b"\x00\x00\x00\x00\x00\x00\x02\x00\x05\x00\x00\x00\xb7\x00\x00\x00\x95\x01\x00\x00\x1f\x00\x00\x00\x08\x00\x00\x00\x05\x00\x06\x00\xffP\xd7\x16\x80\xbb\xbb\xa1O\x00\x00\x00\x01\x00\x02\x00\x1a\x13\x879~\xc7'\x86\x01\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00A\x00\x00\x00\x02\x03\x00\x00m\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00i\x00\x00\x00\xaf\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1a\x13\x879~\xc7'\x86I\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\r\x01\x00\x00z\x02\x00\x001\x01\x00\x00\x17\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00/builds/plexo/pyplexo/src/plexo/schema/plexo_multicast/plexo_preparation.capnp:PlexoPreparation\x00\x00\x00\x00\x00\x01\x00\x01\x00\x0c\x00\x00\x00\x03\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00E\x00\x00\x00Z\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00D\x00\x00\x00\x03\x00\x01\x00P\x00\x00\x00\x02\x00\x01\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00M\x00\x00\x00Z\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00L\x00\x00\x00\x03\x00\x01\x00X\x00\x00\x00\x02\x00\x01\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00U\x00\x00\x00J\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00T\x00\x00\x00\x03\x00\x01\x00`\x00\x00\x00\x02\x00\x01\x00instanceId\x00\x00\x00\x00\x00\x00\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00proposalId\x00\x00\x00\x00\x00\x00\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00typeName\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00/builds/plexo/pyplexo/src/plexo/schema/plexo_multicast/plexo_preparation.capnp\x00\x00\x04\x00\x00\x00\x01\x00\x01\x00\xffP\xd7\x16\x80\xbb\xbb\xa1\x01\x00\x00\x00\x8a\x00\x00\x00PlexoPreparation\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x01\x00\x02\x00\x1a\x13\x879~\xc7'\x86\x05\x00\x00\x00z\x02\x00\x00)\x00\x00\x00\x07\x00\x00\x00/builds/plexo/pyplexo/src/plexo/schema/plexo_multicast/plexo_preparation.capnp\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00"), 8, 0, 2)
    default_options = _Options.from_buffer(_Segment(b'\x02\x00\x03\x00\x01\x00\x03\x00'), 0, 1, 0)
    pyx = False
_reflection_data = _plexo_preparation_ReflectionData()

#### FORWARD DECLARATIONS ####

class PlexoPreparation(_Struct): pass
PlexoPreparation.__name__ = 'PlexoPreparation'


#### DEFINITIONS ####

@PlexoPreparation.__extend__
class PlexoPreparation(_Struct):
    __capnpy_id__ = 0xa1bbbb8016d750ff
    __static_data_size__ = 2
    __static_ptrs_size__ = 1
    
    
    @property
    def instance_id(self):
        # no union check
        value = self._read_primitive(0, ord(b'Q'))
        if 0 != 0:
            value = value ^ 0
        return value
    
    @property
    def proposal_id(self):
        # no union check
        value = self._read_primitive(8, ord(b'Q'))
        if 0 != 0:
            value = value ^ 0
        return value
    
    @property
    def type_name(self):
        # no union check
        return self._read_text_bytes(0)
    
    def get_type_name(self):
        return self._read_text_bytes(0, default_=b"")
    
    def has_type_name(self):
        ptr = self._read_fast_ptr(0)
        return ptr != 0
    
    @staticmethod
    def __new(instance_id=0, proposal_id=0, type_name=None):
        builder = _SegmentBuilder()
        pos = builder.allocate(24)
        builder.write_uint64(pos + 0, instance_id)
        builder.write_uint64(pos + 8, proposal_id)
        builder.alloc_text(pos + 16, type_name)
        return builder.as_string()
    
    def __init__(self, instance_id=0, proposal_id=0, type_name=None):
        _buf = PlexoPreparation.__new(instance_id, proposal_id, type_name)
        self._init_from_buffer(_buf, 0, 2, 1)
    
    def shortrepr(self):
        parts = []
        parts.append("instanceId = %s" % self.instance_id)
        parts.append("proposalId = %s" % self.proposal_id)
        if self.has_type_name(): parts.append("typeName = %s" % _text_bytes_repr(self.get_type_name()))
        return "(%s)" % ", ".join(parts)

_PlexoPreparation_list_item_type = _StructItemType(PlexoPreparation)


_extend_module_maybe(globals(), modname=__name__)