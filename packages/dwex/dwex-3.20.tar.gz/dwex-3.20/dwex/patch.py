import os
import elftools.dwarf.enums
import elftools.dwarf.dwarf_expr
import elftools.dwarf.locationlists
from elftools.common.utils import struct_parse
from elftools.common.exceptions import DWARFError
from elftools.dwarf.descriptions import _DESCR_DW_CC
from types import MethodType

def monkeypatch():
    #https://docs.hdoc.io/hdoc/llvm-project/e051F173385B23DEF.html
    elftools.dwarf.enums.ENUM_DW_AT["DW_AT_LLVM_apinotes"] = 0x3e07
    elftools.dwarf.enums.ENUM_DW_AT["DW_AT_APPLE_objc_direct"] = 0x3fee
    elftools.dwarf.enums.ENUM_DW_AT["DW_AT_APPLE_sdk"] = 0x3fef

    # Wasmloc: monkeypatch for #1589
    elftools.dwarf.dwarf_expr.DW_OP_name2opcode["DW_OP_WASM_location"] = 0xed
    elftools.dwarf.dwarf_expr.DW_OP_opcode2name[0xed] = "DW_OP_WASM_location"
    elftools.dwarf.dwarf_expr.DW_OP_name2opcode['DW_OP_GNU_uninit'] = 0xf0
    elftools.dwarf.dwarf_expr.DW_OP_opcode2name[0xf0] = 'DW_OP_GNU_uninit'
    old_init_dispatch_table = elftools.dwarf.dwarf_expr._init_dispatch_table
    def _init_dispatch_table_patch(structs):
        def parse_wasmloc():
            def parse(stream):
                op = struct_parse(structs.Dwarf_uint8(''), stream)
                if 0 <= op <= 2:
                    return [op, struct_parse(structs.Dwarf_uleb128(''), stream)]
                elif op == 3:
                    return [op, struct_parse(structs.Dwarf_uint32(''), stream)]
                else:
                    raise DWARFError("Unknown operation code in DW_OP_WASM_location: %d" % (op,))
            return parse
        #wasmloc patch
        table = old_init_dispatch_table(structs)
        table[0xed] = parse_wasmloc()
        # GNU_uninit
        table[0xf0] = lambda s: []
        return table
    
    elftools.dwarf.dwarf_expr._init_dispatch_table = _init_dispatch_table_patch

    # Fix for 1613 and other bogus loclist/bogus expr bugs
    def _attribute_is_constant(attr, dwarf_version):
        return (((dwarf_version >= 3 and attr.name == 'DW_AT_data_member_location') or
                (attr.name in ('DW_AT_upper_bound', 'DW_AT_count'))) and
            attr.form in ('DW_FORM_data1', 'DW_FORM_data2', 'DW_FORM_data4', 'DW_FORM_data8', 'DW_FORM_sdata', 'DW_FORM_udata', 'DW_FORM_implicit_const'))
    
    def _attribute_has_loc_list(cls, attr, dwarf_version):
        return (((dwarf_version < 4 and
                 attr.form in ('DW_FORM_data1', 'DW_FORM_data2', 'DW_FORM_data4', 'DW_FORM_data8') and
                 not attr.name == 'DW_AT_const_value') or
                attr.form in ('DW_FORM_sec_offset', 'DW_FORM_loclistx')) and
                not _attribute_is_constant(attr, dwarf_version))
    
    def _attribute_is_loclistptr_class(cls, attr):
        return (attr.name in ( 'DW_AT_location', 'DW_AT_string_length',
                               'DW_AT_const_value', 'DW_AT_return_addr',
                               'DW_AT_data_member_location',
                               'DW_AT_frame_base', 'DW_AT_segment',
                               'DW_AT_static_link', 'DW_AT_use_location',
                               'DW_AT_vtable_elem_location',
                               'DW_AT_call_value',
                               'DW_AT_GNU_call_site_value',
                               'DW_AT_GNU_call_site_target',
                               'DW_AT_GNU_call_site_data_value',
                               'DW_AT_call_target',
                               'DW_AT_call_target_clobbered',
                               'DW_AT_call_data_location',
                               'DW_AT_call_data_value',
                               'DW_AT_upper_bound',
                               'DW_AT_count'))
    elftools.dwarf.locationlists.LocationParser._attribute_has_loc_list = MethodType(_attribute_has_loc_list, elftools.dwarf.locationlists.LocationParser)
    elftools.dwarf.locationlists.LocationParser._attribute_is_loclistptr_class = MethodType(_attribute_is_loclistptr_class, elftools.dwarf.locationlists.LocationParser)
    elftools.dwarf.locationlists.LocationParser._attribute_is_loclistptr_class = MethodType(_attribute_is_loclistptr_class, elftools.dwarf.locationlists.LocationParser)

    # Raw location lists
    def get_location_list_at_offset_ex(self, offset):
        self.stream.seek(offset, os.SEEK_SET)
        return [entry
            for entry
            in struct_parse(self.structs.Dwarf_loclists_entries, self.stream)]
    
    elftools.dwarf.locationlists.LocationLists.get_location_lists_at_offset_ex = get_location_list_at_offset_ex

    # Rangelist entry translate with mixed V4/V5
    def translate_v5_entry(self, entry, cu):
        return self._rnglists.translate_v5_entry(entry, cu)
    elftools.dwarf.ranges.RangeListsPair.translate_v5_entry = translate_v5_entry

    # DWARF5 calling convention codes
    _DESCR_DW_CC[4] = '(pass by ref)'
    _DESCR_DW_CC[5] = '(pass by value)'





