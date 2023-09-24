from typing import Any
import uuid

OBJ_NAME_PREFIX = "lvglobj_"


class LvObject(list):
    def __init__(self, parent=None, **kwargs):
        self._name = kwargs.get("name", f"{OBJ_NAME_PREFIX}{uuid.uuid4()}").replace(
            "-", "_"
        )
        self.parent = parent
        self._attribute = {}

        self._parse_init_kwargs(**kwargs)
        self.build()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value == "parent":
            raise ValueError("Object name can't be 'parent'")
        self._name = value

    @property
    def parent(self):
        return "parent" if self._parent is None else self._parent

    @parent.setter
    def parent(self, value):
        self._parent = value

    @property
    def typedef(self):
        return "lv_obj_t*"

    @property
    def create_func(self):
        return "lv_obj_create"

    @property
    def attributes(self):
        return self._attribute

    def __setitem__(self, __name: str, __value: Any) -> None:
        if isinstance(__value, list):
            self._attribute[__name] = __value
        else:
            self._attribute[__name] = [__value]

    def __getitem__(self, __name: str) -> None:
        return self._attribute[__name]

    @property
    def full_name(self):
        if self.parent == "parent":
            return self.name

        return f"{self.parent.full_name}/{self.name}"

    @property
    def raw_attribute(self):
        return None

    def build(self):
        pass

    def _parse_children(self, **kwargs):
        if "children" in kwargs:
            for child in kwargs["children"]:
                child.parent = self
                self.append(child)

    def _parse_attr(self, **kwargs):
        if "attr" in kwargs:
            for attr, val in kwargs["attr"].items():
                self[attr] = val

    def _parse_event(self, **kwargs):
        if "event" in kwargs.keys():
            self['@event'] = kwargs["event"]
        else:
            self['@event'] = []

    def _parse_init_kwargs(self, **kwargs):
        self._parse_children(**kwargs)
        self._parse_attr(**kwargs)
        self._parse_event(**kwargs)

    def get_children(self, _include_self=True):
        ret = []

        if _include_self:
            ret.append(self)

        for child in self:
            ret.append(child)
            ret.extend(child.get_children(_include_self=False))

        return ret

    def __str__(self):
        return self.name
