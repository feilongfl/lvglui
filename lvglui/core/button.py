from ..basic import Obj


class Button(Obj):
    def __init__(self, parent=None, **kwargs) -> None:
        super().__init__(parent, **kwargs)

        self.createFunc = "lv_btn_create"
