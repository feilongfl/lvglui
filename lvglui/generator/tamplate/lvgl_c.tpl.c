#include <lvgl.h>

#include "${lvobj.name}.h"
#include "${lvobj.name}_data.inc"

/* event cb start */
% for obj in lvobj.get_children():
% if len(obj['@event'])>0:
static void ${obj.name}_event_handler(lv_event_t * e)
{
    lv_event_code_t code = lv_event_get_code(e);
    ARG_UNUSED(e);
}

% endif
% endfor
/* event cb end */

lv_obj_t *lvglui_create_${lvobj.name}(lv_obj_t *parent) {
% for obj in lvobj.get_children():
    /* lvglui: ${obj.__class__.__name__}: ${obj.full_name} */
    ${obj.typedef} ${obj.name} = ${obj.create_func}(${obj.parent});
% if obj.raw_attribute != None:
    /* lvglui: ${obj.__class__.__name__}: ${obj.full_name}: RAW ATTRIBUTE */
    ${obj.raw_attribute}
% endif
    /* lvglui: ${obj.__class__.__name__}: ${obj.full_name}: ATTRIBUTE */
% for attr, val in obj.attributes.items():
% if attr.startswith("!"):
    ${attr}(${','.join([str(v) for v in val])});
% elif attr.startswith("@event"):
% elif attr.startswith("__"):
% else:
    ${attr}(${', '.join([obj.name, *[str(v) for v in val]])});
% endif
% endfor

% endfor
    return ${lvobj.name};
}
