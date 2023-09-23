from ..basic import LvObject


class button(LvObject):
    @property
    def create_func(self):
        return "lv_btn_create"
