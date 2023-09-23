from ..basic import LvObject


class Label(LvObject):
    def __init__(self, parent=None, text="", **kwargs) -> None:
        super().__init__(parent, **kwargs)

        self.text = text

    @property
    def create_func(self):
        return "lv_label_create"

    def _setText(self) -> str:
        return f"""	lv_label_set_text({self.name}, "{self.text}");"""

    def define(self):
        return "\n".join(
            [
                super().define(),
                self._setText(),
            ]
        )
