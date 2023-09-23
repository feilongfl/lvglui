from ..basic import LvObject


class Button(LvObject):
    @property
    def createFunc(self):
        return "lv_btn_create"
