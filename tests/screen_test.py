import lvglui
from loguru import logger


class DemoScreen(lvglui.core.Screen):
    def Build(self):
        self.extend(
            [
                lvglui.core.Label(self, "Hello"),
                lvglui.core.Label(self, "World"),
                lvglui.core.Button(
                    self,
                    name="btn",
                    children=[
                        lvglui.core.Label(self, "Click"),
                    ],
                ),
            ]
        )
        self.Artibute["lv_obj_set_flex_flow"] = ["LV_FLEX_FLOW_COLUMN"]


def test_screen(caplog):
    c = DemoScreen(name="demo_scn").Generate()
    # logger.debug("Code Generate:\n" + c)
    with open("gen/demoscreen.c", "w") as f:
        f.write(
            """
lv_obj_t *lvui_screen_create(lv_obj_t *parent)
{
"""
        )
        f.write(c)
        f.write(
            """
	return demo_scn;
}
"""
        )
