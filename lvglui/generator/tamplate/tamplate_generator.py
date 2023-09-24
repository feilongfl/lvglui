from mako.template import Template

from ...basic.obj import LvObject
from ..base import generator


class tamplate_generator(generator):
    def __init__(self, lvobj: LvObject) -> None:
        super().__init__()
