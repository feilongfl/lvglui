from ..basic import stateless_widget


class textarea(stateless_widget):
    @property
    def create_func(self):
        return "lv_textarea_create"
