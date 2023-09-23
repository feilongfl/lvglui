from ..basic import LvObject


class label(LvObject):
    def __init__(self, parent=None, text="", **kwargs) -> None:
        super().__init__(parent, **kwargs)

        self["lv_label_set_text"] = [f'"{text}"']

    @property
    def create_func(self):
        return "lv_label_create"
