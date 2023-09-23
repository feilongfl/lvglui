from ..basic import Obj


class Label(Obj):
    def __init__(self, parent=None, text="", **kwargs) -> None:
        super().__init__(parent, **kwargs)

        self.createFunc = "lv_label_create"
        self.text = text

    def _setText(self) -> str:
        return f"""	lv_label_set_text({self.name}, "{self.text}");"""

    def Define(self):
        return "\n".join(
            [
                super().Define(),
                self._setText(),
            ]
        )
