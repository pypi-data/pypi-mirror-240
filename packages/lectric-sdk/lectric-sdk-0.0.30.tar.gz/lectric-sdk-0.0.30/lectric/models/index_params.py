from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.index_params_object_type import IndexParamsObjectType
from ..types import UNSET, Unset

T = TypeVar("T", bound="IndexParams")


@_attrs_define
class IndexParams:
    """
    Attributes:
        object_type (Union[Unset, IndexParamsObjectType]):  Default: IndexParamsObjectType.INDEXPARAMS.
        nlist (Union[Unset, int]): Number of cluster units Default: 128.
        quant (Union[Unset, int]): Number of factors of product quantization
        nbits (Union[Unset, int]): Number of bits in which each low-dimensional vector is stored
        m (Union[Unset, int]): Maximum degree of the node
        ef_construction (Union[Unset, int]): Search scope
        pqm (Union[Unset, int]): Number of factors of product quantization
        ntrees (Union[Unset, int]): The number of methods of space division
    """

    object_type: Union[Unset, IndexParamsObjectType] = IndexParamsObjectType.INDEXPARAMS
    nlist: Union[Unset, int] = 128
    quant: Union[Unset, int] = UNSET
    nbits: Union[Unset, int] = UNSET
    m: Union[Unset, int] = UNSET
    ef_construction: Union[Unset, int] = UNSET
    pqm: Union[Unset, int] = UNSET
    ntrees: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        object_type: Union[Unset, str] = UNSET
        if not isinstance(self.object_type, Unset):
            object_type = self.object_type.value

        nlist = self.nlist
        quant = self.quant
        nbits = self.nbits
        m = self.m
        ef_construction = self.ef_construction
        pqm = self.pqm
        ntrees = self.ntrees

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_type is not UNSET:
            field_dict["object_type"] = object_type
        if nlist is not UNSET:
            field_dict["nlist"] = nlist
        if quant is not UNSET:
            field_dict["quant"] = quant
        if nbits is not UNSET:
            field_dict["nbits"] = nbits
        if m is not UNSET:
            field_dict["M"] = m
        if ef_construction is not UNSET:
            field_dict["efConstruction"] = ef_construction
        if pqm is not UNSET:
            field_dict["PQM"] = pqm
        if ntrees is not UNSET:
            field_dict["ntrees"] = ntrees

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _object_type = d.pop("object_type", UNSET)
        object_type: Union[Unset, IndexParamsObjectType]
        if isinstance(_object_type, Unset):
            object_type = UNSET
        else:
            object_type = IndexParamsObjectType(_object_type)

        nlist = d.pop("nlist", UNSET)

        quant = d.pop("quant", UNSET)

        nbits = d.pop("nbits", UNSET)

        m = d.pop("M", UNSET)

        ef_construction = d.pop("efConstruction", UNSET)

        pqm = d.pop("PQM", UNSET)

        ntrees = d.pop("ntrees", UNSET)

        index_params = cls(
            object_type=object_type,
            nlist=nlist,
            quant=quant,
            nbits=nbits,
            m=m,
            ef_construction=ef_construction,
            pqm=pqm,
            ntrees=ntrees,
        )

        index_params.additional_properties = d
        return index_params

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
