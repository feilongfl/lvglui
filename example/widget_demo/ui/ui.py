import lvglui


class DemoScreen(lvglui.core.screen):
    def build(self):
        self["lv_obj_set_flex_flow"] = ["LV_FLEX_FLOW_ROW"]
        self["lv_obj_set_flex_align"] = [
            "LV_FLEX_ALIGN_START",
            "LV_FLEX_ALIGN_CENTER",
            "LV_FLEX_ALIGN_CENTER",
        ]

        roller = lvglui.core.roller(
            self,
            [
                "Arc",
                "Bar",
                "Button",
                "Button Matrix",
                "Canvas",
                "CheckBox",
                "DropDown",
                "image",
                "Label",
                "Line",
                "Roller",
                "Slider",
                "Switch",
                "Table",
                "TextArea",
            ],
        )
        roller["lv_roller_set_visible_row_count"] = 6

        self.extend(
            [
                roller,
            ]
        )
