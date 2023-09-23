import uuid

ObjNamePrefix = "lvglobj_"


class Obj(list):
    def __init__(self, parent=None, **kwargs) -> None:
        self.name = (
            str(kwargs.get("name"))
            if "name" in kwargs
            else f"{ObjNamePrefix}{uuid.uuid4()}".replace("-", "_")
        )
        
        if self.name == 'parent':
            raise ValueError("obj name can't be parent")

        self.typedef = "lv_obj_t*"
        self.createFunc = "lv_obj_create"
        self.parent = parent

        self.Artibute = {}

        self.Children(**kwargs)
        self.Build()

    def getParent(self):
        return "parent" if self.parent == None else self.parent

    def Define(self):
        defineMap = [
            "",
            f"/* {self.__class__.__name__}: {self.name} */",
            f"{self.typedef} {self.name} = {self.createFunc}({self.getParent()});",
        ]

        defineMap.extend([f"{k}({','.join([self.name, *v])});" for k, v in self.Artibute.items()])

        return "\n	".join(defineMap)

    def Build(self):
        pass

    def Children(self, **kwargs):
        if "children" not in kwargs:
            return

        for child in kwargs.get("children"):
            child.parent = self
            self.append(child)

    def __str__(self) -> str:
        return self.name

    def Generate(self):
        return self.Define() + "\n" + "\n".join([object.Generate() for object in self])
