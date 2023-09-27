from .ui import DemoScreen
from lvglui.generator.tamplate import tamplate_generator

if __name__ == "__main__":
    scn = DemoScreen(name="demo_scn")
    tamplate_generator(scn).generate(outdir="src/ui")
