from ..basic import stateless_widget


class button(stateless_widget):
    @property
    def create_func(self):
        return "lv_btn_create"
