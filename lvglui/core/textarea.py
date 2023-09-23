from ..basic import LvObject


class textarea(LvObject):
    @property
    def create_func(self):
        return "lv_textarea_create"
