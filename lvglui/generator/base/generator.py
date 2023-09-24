import os
from ...basic.obj import LvObject

class generator:
    def __init__(self, lvobj: LvObject) -> None:
        self.lvobj = lvobj

    def generate(self, outdir="gen"):
        if not os.path.exists(outdir):
            os.makedirs(outdir)
