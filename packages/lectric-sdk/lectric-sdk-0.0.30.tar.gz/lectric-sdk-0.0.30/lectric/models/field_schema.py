from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.field_schema_object_type import FieldSchemaObjectType
from ..types import UNSET, Unset

T = TypeVar("T", bound="FieldSchema")


@_attrs_define
class FieldSchema:
    """
    Attributes:
        name (str):
        dtype (int):
        object_type (Union[Unset, FieldSchemaObjectType]):  Default: FieldSchemaObjectType.FIELDSCHEMA.
        is_primary (Union[Unset, bool]):
        auto_id (Union[Unset, bool]):
        description (Union[Unset, str]):  Default: ''.
        dim (Union[Unset, int]):
        max_length (Union[Unset, int]):
    """

    name: str
    dtype: int
    object_type: Union[Unset, FieldSchemaObjectType] = FieldSchemaObjectType.FIELDSCHEMA
    is_primary: Union[Unset, bool] = False
    auto_id: Union[Unset, bool] = False
    description: Union[Unset, str] = ""
    dim: Union[Unset, int] = UNSET
    max_length: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        dtype = self.dtype
        object_type: Union[Unset, str] = UNSET
        if not isinstance(self.object_type, Unset):
            object_type = self.object_type.value

        is_primary = self.is_primary
        auto_id = self.auto_id
        description = self.description
        dim = self.dim
        max_length = self.max_length

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "dtype": dtype,
            }
        )
        if object_type is not UNSET:
            field_dict["object_type"] = object_type
        if is_primary is not UNSET:
            field_dict["is_primary"] = is_primary
        if auto_id is not UNSET:
            field_dict["auto_id"] = auto_id
        if description is not UNSET:
            field_dict["description"] = description
        if dim is not UNSET:
            field_dict["dim"] = dim
        if max_length is not UNSET:
            field_dict["max_length"] = max_length

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        dtype = d.pop("dtype")

        _object_type = d.pop("object_type", UNSET)
        object_type: Union[Unset, FieldSchemaObjectType]
        if isinstance(_object_type, Unset):
            object_type = UNSET
        else:
            object_type = FieldSchemaObjectType(_object_type)

        is_primary = d.pop("is_primary", UNSET)

        auto_id = d.pop("auto_id", UNSET)

        description = d.pop("description", UNSET)

        dim = d.pop("dim", UNSET)

        max_length = d.pop("max_length", UNSET)

        field_schema = cls(
            name=name,
            dtype=dtype,
            object_type=object_type,
            is_primary=is_primary,
            auto_id=auto_id,
            description=description,
            dim=dim,
            max_length=max_length,
        )

        field_schema.additional_properties = d
        return field_schema

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
