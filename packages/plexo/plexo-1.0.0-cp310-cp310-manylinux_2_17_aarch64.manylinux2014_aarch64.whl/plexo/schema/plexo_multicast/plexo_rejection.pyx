# THIS FILE HAS BEEN GENERATED AUTOMATICALLY BY capnpy
# do not edit by hand
# generated on 2023-11-09 06:06
# cython: language_level=2

from capnpy cimport ptr as _ptr
from capnpy.struct_ cimport Struct as _Struct
from capnpy.struct_ cimport check_tag as _check_tag
from capnpy.struct_ import undefined as _undefined
from capnpy.enum import enum as _enum, fill_enum as _fill_enum
from capnpy.enum cimport BaseEnum as _BaseEnum
from capnpy.type import Types as _Types
from capnpy.segment.segment cimport Segment as _Segment
from capnpy.segment.segment cimport MultiSegment as _MultiSegment
from capnpy.segment.builder cimport SegmentBuilder as _SegmentBuilder
from capnpy.list cimport List as _List
from capnpy.list cimport PrimitiveItemType as _PrimitiveItemType
from capnpy.list cimport BoolItemType as _BoolItemType
from capnpy.list cimport TextItemType as _TextItemType
from capnpy.list cimport TextUnicodeItemType as _TextUnicodeItemType
from capnpy.list cimport StructItemType as _StructItemType
from capnpy.list cimport EnumItemType as _EnumItemType
from capnpy.list cimport VoidItemType as _VoidItemType
from capnpy.list cimport ListItemType as _ListItemType
from capnpy.anypointer import AnyPointer as _AnyPointer
from capnpy.util import text_bytes_repr as _text_bytes_repr
from capnpy.util import text_unicode_repr as _text_unicode_repr
from capnpy.util import data_repr as _data_repr
from capnpy.util import float32_repr as _float32_repr
from capnpy.util import float64_repr as _float64_repr
from capnpy.util import extend_module_maybe as _extend_module_maybe
from capnpy.util import check_version as _check_version
from capnpy.util import encode_maybe as _encode_maybe
from capnpy cimport _hash
from capnpy.list cimport void_list_item_type as _void_list_item_type
from capnpy.list cimport bool_list_item_type as _bool_list_item_type
from capnpy.list cimport int8_list_item_type as _int8_list_item_type
from capnpy.list cimport uint8_list_item_type as _uint8_list_item_type
from capnpy.list cimport int16_list_item_type as _int16_list_item_type
from capnpy.list cimport uint16_list_item_type as _uint16_list_item_type
from capnpy.list cimport int32_list_item_type as _int32_list_item_type
from capnpy.list cimport uint32_list_item_type as _uint32_list_item_type
from capnpy.list cimport int64_list_item_type as _int64_list_item_type
from capnpy.list cimport uint64_list_item_type as _uint64_list_item_type
from capnpy.list cimport float32_list_item_type as _float32_list_item_type
from capnpy.list cimport float64_list_item_type as _float64_list_item_type
from capnpy.list cimport data_list_item_type as _data_list_item_type
from capnpy.list cimport text_bytes_list_item_type as _text_bytes_list_item_type
from capnpy.list cimport text_unicode_list_item_type as _text_unicode_list_item_type
__capnpy_id__ = 0xa2849a07964d7b1b
__capnpy_version__ = '0.10.1'
__capnproto_version__ = '0.5.3.1'
# schema compiled with --no-version-check, skipping the call to _check_version
from capnpy.schema import CodeGeneratorRequest as _CodeGeneratorRequest
from capnpy.annotate import Options as _Options
from capnpy.reflection import ReflectionData as _ReflectionData
class _plexo_rejection_ReflectionData(_ReflectionData):
    request = _CodeGeneratorRequest.from_buffer(_Segment(b'\x00\x00\x00\x00\x00\x00\x02\x00\x05\x00\x00\x00\xb7\x00\x00\x00\x81\x01\x00\x00\x1f\x00\x00\x00\x08\x00\x00\x00\x05\x00\x06\x00\x90\x99^@g\xb5\x9c\xf6;\x00\x00\x00\x01\x00\x02\x00\x1b{M\x96\x07\x9a\x84\xa2\x01\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00A\x00\x00\x00R\x02\x00\x00e\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00a\x00\x00\x00\xaf\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1b{M\x96\x07\x9a\x84\xa25\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x01\x00\x00\xda\x01\x00\x00!\x01\x00\x00\x17\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00/io/src/plexo/schema/plexo_multicast/plexo_rejection.capnp:PlexoRejection\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00\x0c\x00\x00\x00\x03\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00E\x00\x00\x00Z\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00D\x00\x00\x00\x03\x00\x01\x00P\x00\x00\x00\x02\x00\x01\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00M\x00\x00\x00Z\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00L\x00\x00\x00\x03\x00\x01\x00X\x00\x00\x00\x02\x00\x01\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00U\x00\x00\x00J\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00T\x00\x00\x00\x03\x00\x01\x00`\x00\x00\x00\x02\x00\x01\x00instanceId\x00\x00\x00\x00\x00\x00\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00proposalId\x00\x00\x00\x00\x00\x00\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00typeName\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00/io/src/plexo/schema/plexo_multicast/plexo_rejection.capnp\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x01\x00\x01\x00\x90\x99^@g\xb5\x9c\xf6\x01\x00\x00\x00z\x00\x00\x00PlexoRejection\x00\x00\x04\x00\x00\x00\x01\x00\x02\x00\x1b{M\x96\x07\x9a\x84\xa2\x05\x00\x00\x00\xda\x01\x00\x00!\x00\x00\x00\x07\x00\x00\x00/io/src/plexo/schema/plexo_multicast/plexo_rejection.capnp\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00'), 8, 0, 2)
    default_options = _Options.from_buffer(_Segment(b'\x02\x00\x03\x00\x01\x00\x03\x00'), 0, 1, 0)
    pyx = True
_reflection_data = _plexo_rejection_ReflectionData()

#### FORWARD DECLARATIONS ####

cdef class PlexoRejection(_Struct)


#### DEFINITIONS ####

cdef class PlexoRejection(_Struct):
    __capnpy_id__ = 0xf69cb567405e9990
    __static_data_size__ = 2
    __static_ptrs_size__ = 1
    
    
    property instance_id:
        def __get__(self):
            # no union check
            value = self._read_primitive(0, ord(b'Q'))
            if 0 != 0:
                value = value ^ 0
            return value
    
    property proposal_id:
        def __get__(self):
            # no union check
            value = self._read_primitive(8, ord(b'Q'))
            if 0 != 0:
                value = value ^ 0
            return value
    
    property type_name:
        def __get__(self):
            # no union check
            return self._read_text_bytes(0)
    
    cpdef get_type_name(self):
        return self._read_text_bytes(0, default_=b"")
    
    cpdef has_type_name(self):
        ptr = self._read_fast_ptr(0)
        return ptr != 0
    
    @staticmethod
    cdef __new(object instance_id=0, object proposal_id=0, object type_name=None):
        cdef _SegmentBuilder builder
        cdef long pos
        builder = _SegmentBuilder()
        pos = builder.allocate(24)
        builder.write_uint64(pos + 0, instance_id)
        builder.write_uint64(pos + 8, proposal_id)
        builder.alloc_text(pos + 16, type_name)
        return builder.as_string()
    
    def __init__(object self, object instance_id=0, object proposal_id=0, object type_name=None):
        _buf = PlexoRejection.__new(instance_id, proposal_id, type_name)
        self._init_from_buffer(_buf, 0, 2, 1)
    
    cpdef shortrepr(self):
        parts = []
        parts.append("instanceId = %s" % self.instance_id)
        parts.append("proposalId = %s" % self.proposal_id)
        if self.has_type_name(): parts.append("typeName = %s" % _text_bytes_repr(self.get_type_name()))
        return "(%s)" % ", ".join(parts)

cdef _StructItemType _PlexoRejection_list_item_type = _StructItemType(PlexoRejection)


_extend_module_maybe(globals(), modname=__name__)