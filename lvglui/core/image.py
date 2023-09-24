from ..basic import stateless_widget


class image(stateless_widget):
    def __init__(self, parent=None, src="", **kwargs) -> None:
        super().__init__(parent, **kwargs)

        self["!LV_IMG_DECLARE"] = [f"{src}"]
        self["lv_img_set_src"] = [f"&{src}"]

        # todo: auto generate imgsrc from asserts

    @property
    def create_func(self):
        return "lv_img_create"
