#thanks gpt 

import importlib.util
import os

_loaded_modules = {}

def loadModule(path):

    if path in _loaded_modules:
        return _loaded_modules[path]

    module_name = os.path.splitext(os.path.basename(path))[0]

    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    cls = getattr(module, module_name)

    _loaded_modules[path] = cls
    return cls
