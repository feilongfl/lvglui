#include <lvgl.h>

#include "${lvobj.name}.h"
#include "${lvobj.name}_data.inc"

/* event cb start */
% for obj in lvobj.get_children():
% if len(obj['__event'])>0:
static void ${obj.name}_event_handler(lv_event_t * e)
{
    lv_event_code_t code = lv_event_get_code(e);
    ARG_UNUSED(e);
}

% endif
% endfor
/* event cb end */

/* create functions start */
% for obj in reversed(lvobj.get_children()):
% if obj.parent != 'parent':
static inline \
% endif
lv_obj_t *lvglui_create_${obj.full_name}(lv_obj_t *parent) {
    lv_obj_t *${obj.name} = ${obj.create_func}(parent);
    /* set raw attribute */
% if obj.raw_attribute != None:
    ${obj.raw_attribute}
% endif

    /* set attribute */
% for attr, val in obj.attributes.items():
% if attr.startswith("!"):
    ${attr}(${','.join([str(v) for v in val])});
% elif attr.startswith("__"):
% else:
    ${attr}(${', '.join([obj.name, *[str(v) for v in val]])});
% endif
% endfor

    /* set event handler */
% for evt in obj['__event']:
    lv_obj_add_event_cb(${obj.name}, ${obj.name}_event_handler, evt, NULL);
% endfor

    /* create children */
% for child in obj:
    lvglui_create_${child.full_name}(${obj.name})
% endfor

    return ${obj.name};
}

% endfor
/* create functions end */
