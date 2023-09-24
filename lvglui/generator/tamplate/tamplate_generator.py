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
    def generator(self):
        return {
            f"{self.lvobj.name}_data.inc": "lvgl_c_data.tpl.inc",
            f"{self.lvobj.name}.h": "lvgl_c.tpl.h",
            f"{self.lvobj.name}.c": "lvgl_c.tpl.c",
        }

    def generate(self, outdir="gen"):
        if not os.path.exists(outdir):
            os.makedirs(outdir)

        for gen_file, gen_tpl in self.generator.items():
            with open(os.path.join(outdir, gen_file), "w") as f:
                f.write(self._file_descript_headers)
                f.write(str(self.lut.get_template(gen_tpl).render(lvobj=self.lvobj)))
