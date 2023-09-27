from ..basic import stateless_widget


class arc(stateless_widget):
    def __init__(self, parent=None, value=0, **kwargs) -> None:
        super().__init__(parent, **kwargs)

        self["lv_arc_set_value"] = [value]

    @property
    def create_func(self):
        return "lv_arc_create"
