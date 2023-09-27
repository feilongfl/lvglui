from ..basic import stateless_widget


class button_mutrix(stateless_widget):
    def __init__(self, parent=None, button_map=[], **kwargs) -> None:
        super().__init__(parent, **kwargs)

        self["__button_map"] = button_map
        self["lv_btnmatrix_set_map"] = [self.btnmap_name]

    @property
    def btnmap_name(self):
        return f"{self.name}_btnmap"

    @property
    def create_func(self):
        return "lv_btnmatrix_create"

    @property
    def raw_attribute(self):
        return """static const char * %s[] = {%s, ""};""" % (
            self.btnmap_name,
            ",".join([f'"{x}"' for x in self["__button_map"]]),
        )
