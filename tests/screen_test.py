import lvglui
from lvglui.generator.tamplate import tamplate_generator


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
                    event=[
                        'LV_EVENT_ALL',
                    ]
                ),
            ]
        )


def test_screen(caplog):
    scn = DemoScreen(name="demo_scn")
    print(scn.parent)
    tamplate_generator(scn).generate(outdir='gen/test_screen')
