from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.collection_schema_object_type import CollectionSchemaObjectType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.field_schema import FieldSchema


T = TypeVar("T", bound="CollectionSchema")


@_attrs_define
class CollectionSchema:
    """
    Attributes:
        object_type (Union[Unset, CollectionSchemaObjectType]):  Default: CollectionSchemaObjectType.COLLECTIONSCHEMA.
        fields (Union[Unset, List['FieldSchema']]):
        description (Union[Unset, str]):  Default: ''.
    """

    object_type: Union[Unset, CollectionSchemaObjectType] = CollectionSchemaObjectType.COLLECTIONSCHEMA
    fields: Union[Unset, List["FieldSchema"]] = UNSET
    description: Union[Unset, str] = ""
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        object_type: Union[Unset, str] = UNSET
        if not isinstance(self.object_type, Unset):
            object_type = self.object_type.value

        fields: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for fields_item_data in self.fields:
                fields_item = fields_item_data.to_dict()

                fields.append(fields_item)

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_type is not UNSET:
            field_dict["object_type"] = object_type
        if fields is not UNSET:
            field_dict["fields"] = fields
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.field_schema import FieldSchema

        d = src_dict.copy()
        _object_type = d.pop("object_type", UNSET)
        object_type: Union[Unset, CollectionSchemaObjectType]
        if isinstance(_object_type, Unset):
            object_type = UNSET
        else:
            object_type = CollectionSchemaObjectType(_object_type)

        fields = []
        _fields = d.pop("fields", UNSET)
        for fields_item_data in _fields or []:
            fields_item = FieldSchema.from_dict(fields_item_data)

            fields.append(fields_item)

        description = d.pop("description", UNSET)

        collection_schema = cls(
            object_type=object_type,
            fields=fields,
            description=description,
        )

        collection_schema.additional_properties = d
        return collection_schema

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
