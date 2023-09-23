from typing import Any
import uuid
from loguru import logger

OBJ_NAME_PREFIX = "lvglobj_"


class LvObject(list):
    def __init__(self, parent=None, **kwargs):
        self._name = kwargs.get("name", f"{OBJ_NAME_PREFIX}{uuid.uuid4()}").replace(
            "-", "_"
        )
        self.parent = parent
        self._attribute = {}

        self.children(**kwargs)
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
        self._attribute[__name] = __value

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

    def define(self):
        define_map = [
            "",
            f"/* lvglui: {self.__class__.__name__}: {self.full_name} */",
            f"{self.typedef} {self.name} = {self.create_func}({self.parent});",
        ]
        define_map.append(self.raw_attribute) if self.raw_attribute is not None else ""
        define_map.extend(
            [
                f"{k[1:]}({','.join([*(str(x) for x in v)])});"
                for k, v in self.attributes.items()
                if k.startswith("@")
            ]
        )
        define_map.extend(
            [
                f"{k}({','.join([self.name, *(str(x) for x in v)])});"
                for k, v in self.attributes.items()
                if not k.startswith(("__", "@"))
            ]
        )
        logger.debug(f"define: {self}: {define_map}")

        return "\n    ".join(define_map)

    def build(self):
        pass

    def children(self, **kwargs):
        if "children" in kwargs:
            print(f"{self.__class__.__name__}: {self}: {kwargs}")
            for child in kwargs["children"]:
                child.parent = self
                self.append(child)

    def __str__(self):
        return self.name

    def generate(self):
        logger.debug(f"generate call: {self}: children->{[obj.name for obj in self]}")
        return self.define() + "\n" + "\n".join([obj.generate() for obj in self])
