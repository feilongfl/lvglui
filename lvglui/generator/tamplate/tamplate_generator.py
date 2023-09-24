import os
from mako.template import Template
from mako.lookup import TemplateLookup

from ...basic.obj import LvObject
from ..base import generator


class tamplate_generator(generator):
    def __init__(self, lvobj: LvObject) -> None:
        super().__init__()

        self.lut = TemplateLookup(directories=[os.path.dirname(__file__)])
        self.lvobj = lvobj

    @property
    def _file_descript_headers(self) -> str:
        return """/* Auto Generate File
 * DO NOT EDIT
 */
"""

    @property
    def _generate_c_include(self):
        return f"""
#include <lvgl.h>

#include "{self.lvobj.name}.h"
#include "{self.lvobj.name}_data.inc"
"""

    @property
    def _generate_c_create_func(self):
        return f"""
lv_obj_t *lvglui_create_{self.lvobj.name}(lv_obj_t *parent) {{
    {self.lvobj.generate()}

    return {self.lvobj.name};
}}
"""

    @property
    def _generate_h_create_func_dec(self):
        return f"""
lv_obj_t *lvglui_create_{self.lvobj.name}(lv_obj_t *parent);
"""

    def _generate_c(self) -> str:
        return "".join([self._generate_c_include, self._generate_c_create_func])

    def _generate_data(self) -> str:
        return ""

    def _generate_h(self) -> str:
        return "".join([self._generate_h_create_func_dec])

    @property
    def generator(self):
        return {
            f"{self.lvobj.name}_data.inc": self._generate_data,
            f"{self.lvobj.name}.h": self._generate_h,
            f"{self.lvobj.name}.c": self._generate_c,
        }

    def generate(self, outdir="gen"):
        if not os.path.exists(outdir):
            os.makedirs(outdir)

        for gen_file, gen_func in self.generator.items():
            with open(os.path.join(outdir, gen_file), "w") as f:
                f.write(self._file_descript_headers)
                f.write(gen_func())
