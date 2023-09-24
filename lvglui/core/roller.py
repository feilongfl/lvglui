from ..basic import stateless_widget


class roller(stateless_widget):
    def __init__(self, parent=None, drop_opt=[], roller_mode="LV_ROLLER_MODE_NORMAL", **kwargs) -> None:
        super().__init__(parent, **kwargs)

        self["__roller_opt"] = drop_opt
        self["lv_roller_set_options"] = [self.roller_opt_name, roller_mode]

    @property
    def roller_opt_name(self):
        return f"{self.name}_options"

    @property
    def create_func(self):
        return "lv_roller_create"

    @property
    def raw_attribute(self):
        return """static const char * %s = "%s";""" % (
            self.roller_opt_name,
            "\\n".join([f"{x}" for x in self["__roller_opt"]]),
        )
