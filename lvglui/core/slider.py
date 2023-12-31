from ..basic import LvObject


class slider(LvObject):
    def __init__(self, parent=None, value=0, **kwargs) -> None:
        super().__init__(parent, **kwargs)

        self["lv_slider_set_value"] = [value, "LV_ANIM_OFF"]

    @property
    def create_func(self):
        return "lv_slider_create"
