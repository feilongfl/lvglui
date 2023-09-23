import os
import importlib

contents = os.listdir(os.path.dirname(__file__))
module_files = [
    f
    for f in contents
    if f.endswith(".py") and not f.startswith(("__init__", "__main__"))
]


for module_file in module_files:
    module_name = os.path.splitext(module_file)[0]
    module = importlib.import_module(f".{module_name}", package=__package__)
    globals()[module_name] = getattr(module, module_name)
