import lvglui


class DemoScreen(lvglui.core.screen):
    def build(self):
        self["lv_obj_set_flex_flow"] = ["LV_FLEX_FLOW_COLUMN"]
        self["lv_obj_set_flex_align"] = [
            "LV_FLEX_ALIGN_CENTER",
            "LV_FLEX_ALIGN_START",
            "LV_FLEX_ALIGN_CENTER",
        ]

        self.extend(
            [
                lvglui.core.label(self, "Hello World"),
                lvglui.core.button(
                    self,
                    name="btn",
                    children=[
                        lvglui.core.label(self, "Click"),
                    ],
                ),
            ]
        )


def test_screen(caplog):
    scn = DemoScreen(name="demo_scn")
    with open("gen/demoscreen.c", "w") as f:
        f.write(
            """
lv_obj_t *lvui_screen_create(lv_obj_t *parent)
{
"""
        )
        f.write(scn.generate())
        f.write(
            """
	return %s;
}
"""
            % scn.name
        )
