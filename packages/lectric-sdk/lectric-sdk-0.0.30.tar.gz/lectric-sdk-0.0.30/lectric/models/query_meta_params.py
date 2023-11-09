from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.query_meta_params_object_type import QueryMetaParamsObjectType
from ..types import UNSET, Unset

T = TypeVar("T", bound="QueryMetaParams")


@_attrs_define
class QueryMetaParams:
    """
    Attributes:
        nprobe (int): Number of units to query. CPU: [1, nlist], GPU: [1, min(2048, nlist)
        object_type (Union[Unset, QueryMetaParamsObjectType]):  Default: QueryMetaParamsObjectType.QUERYMETAPARAMS.
        ef (Union[Unset, int]): Search Scope. Range [top_k, 32768]
        search_k (Union[Unset, int]): The number of nodes to search. -1 means 5% of the whole data. Range {-1} U [top_k,
            n x n_trees]
    """

    nprobe: int
    object_type: Union[Unset, QueryMetaParamsObjectType] = QueryMetaParamsObjectType.QUERYMETAPARAMS
    ef: Union[Unset, int] = UNSET
    search_k: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        nprobe = self.nprobe
        object_type: Union[Unset, str] = UNSET
        if not isinstance(self.object_type, Unset):
            object_type = self.object_type.value

        ef = self.ef
        search_k = self.search_k

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nprobe": nprobe,
            }
        )
        if object_type is not UNSET:
            field_dict["object_type"] = object_type
        if ef is not UNSET:
            field_dict["ef"] = ef
        if search_k is not UNSET:
            field_dict["search_k"] = search_k

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        nprobe = d.pop("nprobe")

        _object_type = d.pop("object_type", UNSET)
        object_type: Union[Unset, QueryMetaParamsObjectType]
        if isinstance(_object_type, Unset):
            object_type = UNSET
        else:
            object_type = QueryMetaParamsObjectType(_object_type)

        ef = d.pop("ef", UNSET)

        search_k = d.pop("search_k", UNSET)

        query_meta_params = cls(
            nprobe=nprobe,
            object_type=object_type,
            ef=ef,
            search_k=search_k,
        )

        query_meta_params.additional_properties = d
        return query_meta_params

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
