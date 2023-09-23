# LVGL UI

> this is a lvgl c code generator.

> warning: this project is not stable, and in developing
> 
> **DO NOT** USE in product.

## usage

### simple demo

#### python descript

``` python
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
```

#### c generate

``` c
/* DemoScreen: demo_scn */
lv_obj_t* demo_scn = lv_obj_create(parent);
lv_obj_set_flex_flow(demo_scn,LV_FLEX_FLOW_COLUMN);

/* Label: lvglobj_5a0d5797_f4fa_44da_b37b_bedaa9ca26c3 */
lv_obj_t* lvglobj_5a0d5797_f4fa_44da_b37b_bedaa9ca26c3 = lv_label_create(demo_scn);
lv_label_set_text(lvglobj_5a0d5797_f4fa_44da_b37b_bedaa9ca26c3, "Hello");


/* Label: lvglobj_0bc4318a_05cd_4fa5_8e7b_a397795ffccd */
lv_obj_t* lvglobj_0bc4318a_05cd_4fa5_8e7b_a397795ffccd = lv_label_create(demo_scn);
lv_label_set_text(lvglobj_0bc4318a_05cd_4fa5_8e7b_a397795ffccd, "World");


/* Button: btn */
lv_obj_t* btn = lv_btn_create(demo_scn);

/* Label: lvglobj_dbefc428_a860_4b0b_bd77_d3565d3824c3 */
lv_obj_t* lvglobj_dbefc428_a860_4b0b_bd77_d3565d3824c3 = lv_label_create(btn);
lv_label_set_text(lvglobj_dbefc428_a860_4b0b_bd77_d3565d3824c3, "Click");
```

