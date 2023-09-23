from ..basic import LvObject


class dropdown(LvObject):
    def __init__(self, parent=None, drop_opt=[], **kwargs) -> None:
        super().__init__(parent, **kwargs)

        self["__dropdown_opt"] = drop_opt
        self["lv_dropdown_set_options"] = [self.dropdown_opt_name]

    @property
    def dropdown_opt_name(self):
        return f"{self.name}_options"

    @property
    def create_func(self):
        return "lv_dropdown_create"

    @property
    def raw_attribute(self):
        return """static const char * %s = "%s";""" % (
            self.dropdown_opt_name,
            '\\n'.join([f'{x}' for x in self["__dropdown_opt"]]),
        )
