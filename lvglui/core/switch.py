from ..basic import LvObject


class switch(LvObject):
    @property
    def create_func(self):
        return "lv_switch_create"
