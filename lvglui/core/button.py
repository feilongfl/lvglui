from ..basic import LvObject


class Button(LvObject):
    @property
    def create_func(self):
        return "lv_btn_create"
