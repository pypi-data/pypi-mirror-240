from typing import Any, cast, Dict, List, Optional, Type, TypeVar, Union

import attr

from ..extensions import NotPresentError
from ..types import UNSET, Unset

T = TypeVar("T", bound="Collaborator")


@attr.s(auto_attribs=True, repr=False)
class Collaborator:
    """  """

    _name: Union[Unset, str] = UNSET
    _type: Union[Unset, str] = UNSET
    _admin_schema_policy_id: Union[Unset, str] = UNSET
    _id: Union[Unset, str] = UNSET
    _member_schema_policy_id: Union[Unset, str] = UNSET
    _schema_policy_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def __repr__(self):
        fields = []
        fields.append("name={}".format(repr(self._name)))
        fields.append("type={}".format(repr(self._type)))
        fields.append("admin_schema_policy_id={}".format(repr(self._admin_schema_policy_id)))
        fields.append("id={}".format(repr(self._id)))
        fields.append("member_schema_policy_id={}".format(repr(self._member_schema_policy_id)))
        fields.append("schema_policy_id={}".format(repr(self._schema_policy_id)))
        fields.append("additional_properties={}".format(repr(self.additional_properties)))
        return "Collaborator({})".format(", ".join(fields))

    def to_dict(self) -> Dict[str, Any]:
        name = self._name
        type = self._type
        admin_schema_policy_id = self._admin_schema_policy_id
        id = self._id
        member_schema_policy_id = self._member_schema_policy_id
        schema_policy_id = self._schema_policy_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        # Allow the model to serialize even if it was created outside of the constructor, circumventing validation
        if name is not UNSET:
            field_dict["name"] = name
        if type is not UNSET:
            field_dict["type"] = type
        if admin_schema_policy_id is not UNSET:
            field_dict["adminSchemaPolicyId"] = admin_schema_policy_id
        if id is not UNSET:
            field_dict["id"] = id
        if member_schema_policy_id is not UNSET:
            field_dict["memberSchemaPolicyId"] = member_schema_policy_id
        if schema_policy_id is not UNSET:
            field_dict["schemaPolicyId"] = schema_policy_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any], strict: bool = False) -> T:
        d = src_dict.copy()

        def get_name() -> Union[Unset, str]:
            name = d.pop("name")
            return name

        try:
            name = get_name()
        except KeyError:
            if strict:
                raise
            name = cast(Union[Unset, str], UNSET)

        def get_type() -> Union[Unset, str]:
            type = d.pop("type")
            return type

        try:
            type = get_type()
        except KeyError:
            if strict:
                raise
            type = cast(Union[Unset, str], UNSET)

        def get_admin_schema_policy_id() -> Union[Unset, str]:
            admin_schema_policy_id = d.pop("adminSchemaPolicyId")
            return admin_schema_policy_id

        try:
            admin_schema_policy_id = get_admin_schema_policy_id()
        except KeyError:
            if strict:
                raise
            admin_schema_policy_id = cast(Union[Unset, str], UNSET)

        def get_id() -> Union[Unset, str]:
            id = d.pop("id")
            return id

        try:
            id = get_id()
        except KeyError:
            if strict:
                raise
            id = cast(Union[Unset, str], UNSET)

        def get_member_schema_policy_id() -> Union[Unset, str]:
            member_schema_policy_id = d.pop("memberSchemaPolicyId")
            return member_schema_policy_id

        try:
            member_schema_policy_id = get_member_schema_policy_id()
        except KeyError:
            if strict:
                raise
            member_schema_policy_id = cast(Union[Unset, str], UNSET)

        def get_schema_policy_id() -> Union[Unset, str]:
            schema_policy_id = d.pop("schemaPolicyId")
            return schema_policy_id

        try:
            schema_policy_id = get_schema_policy_id()
        except KeyError:
            if strict:
                raise
            schema_policy_id = cast(Union[Unset, str], UNSET)

        collaborator = cls(
            name=name,
            type=type,
            admin_schema_policy_id=admin_schema_policy_id,
            id=id,
            member_schema_policy_id=member_schema_policy_id,
            schema_policy_id=schema_policy_id,
        )

        collaborator.additional_properties = d
        return collaborator

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

    def get(self, key, default=None) -> Optional[Any]:
        return self.additional_properties.get(key, default)

    @property
    def name(self) -> str:
        if isinstance(self._name, Unset):
            raise NotPresentError(self, "name")
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @name.deleter
    def name(self) -> None:
        self._name = UNSET

    @property
    def type(self) -> str:
        if isinstance(self._type, Unset):
            raise NotPresentError(self, "type")
        return self._type

    @type.setter
    def type(self, value: str) -> None:
        self._type = value

    @type.deleter
    def type(self) -> None:
        self._type = UNSET

    @property
    def admin_schema_policy_id(self) -> str:
        if isinstance(self._admin_schema_policy_id, Unset):
            raise NotPresentError(self, "admin_schema_policy_id")
        return self._admin_schema_policy_id

    @admin_schema_policy_id.setter
    def admin_schema_policy_id(self, value: str) -> None:
        self._admin_schema_policy_id = value

    @admin_schema_policy_id.deleter
    def admin_schema_policy_id(self) -> None:
        self._admin_schema_policy_id = UNSET

    @property
    def id(self) -> str:
        if isinstance(self._id, Unset):
            raise NotPresentError(self, "id")
        return self._id

    @id.setter
    def id(self, value: str) -> None:
        self._id = value

    @id.deleter
    def id(self) -> None:
        self._id = UNSET

    @property
    def member_schema_policy_id(self) -> str:
        if isinstance(self._member_schema_policy_id, Unset):
            raise NotPresentError(self, "member_schema_policy_id")
        return self._member_schema_policy_id

    @member_schema_policy_id.setter
    def member_schema_policy_id(self, value: str) -> None:
        self._member_schema_policy_id = value

    @member_schema_policy_id.deleter
    def member_schema_policy_id(self) -> None:
        self._member_schema_policy_id = UNSET

    @property
    def schema_policy_id(self) -> str:
        if isinstance(self._schema_policy_id, Unset):
            raise NotPresentError(self, "schema_policy_id")
        return self._schema_policy_id

    @schema_policy_id.setter
    def schema_policy_id(self, value: str) -> None:
        self._schema_policy_id = value

    @schema_policy_id.deleter
    def schema_policy_id(self) -> None:
        self._schema_policy_id = UNSET
