from ..basic import LvObject


class bar(LvObject):
    def __init__(self, parent=None, value=0, **kwargs) -> None:
        super().__init__(parent, **kwargs)

        self["lv_bar_create"] = [value]

    @property
    def create_func(self):
        return "lv_bar_create"
