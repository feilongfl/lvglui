#include <lvgl.h>

#include "${lvobj.name}.h"
#include "${lvobj.name}_data.inc"

lv_obj_t *lvglui_create_${lvobj.name}(lv_obj_t *parent) {
    ${lvobj.generate()}

    return ${lvobj.name};
}
