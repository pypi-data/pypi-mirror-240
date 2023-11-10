from __future__ import annotations
import ast
from typing import Tuple, TypeVar, Iterable
from func_adl import ObjectStream, func_adl_callback, func_adl_parameterized_call
import func_adl_servicex_xaodr24

_method_map = {
    'eta': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'eta',
        'return_type': 'float',
    },
    'globalEta': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'globalEta',
        'return_type': 'int',
    },
    'phi': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'phi',
        'return_type': 'float',
    },
    'globalPhi': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'globalPhi',
        'return_type': 'unsigned int',
    },
    'jFEXtowerID': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'jFEXtowerID',
        'return_type': 'unsigned int',
    },
    'isCore': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'isCore',
        'return_type': 'bool',
    },
    'SCellEt': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'SCellEt',
        'return_type_element': 'float',
        'return_type_collection': 'const vector<float>',
    },
    'SCellEta': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'SCellEta',
        'return_type_element': 'float',
        'return_type_collection': 'const vector<float>',
    },
    'SCellPhi': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'SCellPhi',
        'return_type_element': 'float',
        'return_type_collection': 'const vector<float>',
    },
    'SCellID': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'SCellID',
        'return_type_element': 'short',
        'return_type_collection': 'const vector<int>',
    },
    'SCellMask': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'SCellMask',
        'return_type_element': 'bool',
        'return_type_collection': 'const vector<bool>',
    },
    'TileEt': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'TileEt',
        'return_type': 'int',
    },
    'TileEta': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'TileEta',
        'return_type': 'float',
    },
    'TilePhi': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'TilePhi',
        'return_type': 'float',
    },
    'jtowerEtMeV': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'jtowerEtMeV',
        'return_type': 'int',
    },
    'SCellEtMeV': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'SCellEtMeV',
        'return_type': 'float',
    },
    'TileEtMeV': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'TileEtMeV',
        'return_type': 'float',
    },
    'emulated_jtowerEt': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'emulated_jtowerEt',
        'return_type': 'int',
    },
    'index': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'index',
        'return_type': 'int',
    },
    'usingPrivateStore': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'usingPrivateStore',
        'return_type': 'bool',
    },
    'usingStandaloneStore': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'usingStandaloneStore',
        'return_type': 'bool',
    },
    'hasStore': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'hasStore',
        'return_type': 'bool',
    },
    'hasNonConstStore': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'hasNonConstStore',
        'return_type': 'bool',
    },
    'clearDecorations': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'clearDecorations',
        'return_type': 'bool',
    },
    'trackIndices': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'trackIndices',
        'return_type': 'bool',
    },
    'auxdataConst': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'auxdataConst',
        'return_type': 'U',
    },
    'isAvailable': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'isAvailable',
        'return_type': 'bool',
    },
}


T = TypeVar('T')


def _add_method_metadata(s: ObjectStream[T], a: ast.Call) -> Tuple[ObjectStream[T], ast.Call]:
    '''Add metadata for a collection to the func_adl stream if we know about it
    '''
    assert isinstance(a.func, ast.Attribute)
    if a.func.attr in _method_map:
        s_update = s.MetaData(_method_map[a.func.attr])
        s_update = s_update.MetaData({
            'metadata_type': 'inject_code',
            'name': 'xAODTrigL1Calo/versions/jFexTower_v1.h',
            'body_includes': ["xAODTrigL1Calo/versions/jFexTower_v1.h"],
        })
        return s_update, a
    else:
        return s, a


@func_adl_callback(_add_method_metadata)
class jFexTower_v1:
    "A class"

    def eta(self) -> float:
        "A method"
        ...

    def globalEta(self) -> int:
        "A method"
        ...

    def phi(self) -> float:
        "A method"
        ...

    def globalPhi(self) -> int:
        "A method"
        ...

    def jFEXtowerID(self) -> int:
        "A method"
        ...

    def isCore(self) -> bool:
        "A method"
        ...

    def SCellEt(self) -> func_adl_servicex_xaodr24.vector_float_.vector_float_:
        "A method"
        ...

    def SCellEta(self) -> func_adl_servicex_xaodr24.vector_float_.vector_float_:
        "A method"
        ...

    def SCellPhi(self) -> func_adl_servicex_xaodr24.vector_float_.vector_float_:
        "A method"
        ...

    def SCellID(self) -> func_adl_servicex_xaodr24.vector_int_.vector_int_:
        "A method"
        ...

    def SCellMask(self) -> func_adl_servicex_xaodr24.vector_bool_.vector_bool_:
        "A method"
        ...

    def TileEt(self) -> int:
        "A method"
        ...

    def TileEta(self) -> float:
        "A method"
        ...

    def TilePhi(self) -> float:
        "A method"
        ...

    def jtowerEtMeV(self) -> int:
        "A method"
        ...

    def SCellEtMeV(self) -> float:
        "A method"
        ...

    def TileEtMeV(self) -> float:
        "A method"
        ...

    def emulated_jtowerEt(self) -> int:
        "A method"
        ...

    def index(self) -> int:
        "A method"
        ...

    def usingPrivateStore(self) -> bool:
        "A method"
        ...

    def usingStandaloneStore(self) -> bool:
        "A method"
        ...

    def hasStore(self) -> bool:
        "A method"
        ...

    def hasNonConstStore(self) -> bool:
        "A method"
        ...

    def clearDecorations(self) -> bool:
        "A method"
        ...

    def trackIndices(self) -> bool:
        "A method"
        ...

    @func_adl_parameterized_call(lambda s, a, param_1: func_adl_servicex_xaodr24.type_support.cpp_generic_1arg_callback('auxdataConst', s, a, param_1))
    @property
    def auxdataConst(self) -> func_adl_servicex_xaodr24.type_support.index_type_forwarder[str]:
        "A method"
        ...

    @func_adl_parameterized_call(lambda s, a, param_1: func_adl_servicex_xaodr24.type_support.cpp_generic_1arg_callback('isAvailable', s, a, param_1))
    @property
    def isAvailable(self) -> func_adl_servicex_xaodr24.type_support.index_type_forwarder[str]:
        "A method"
        ...
