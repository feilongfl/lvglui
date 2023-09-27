from ..basic import stateless_widget


class switch(stateless_widget):
    @property
    def create_func(self):
        return "lv_switch_create"
