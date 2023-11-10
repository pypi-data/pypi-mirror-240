from importlib import reload
from types import ModuleType
from importlib.util import module_from_spec, spec_from_loader
from importlib.machinery import SourceFileLoader
from logging import getLogger
import mlbull_dummies


from .print_logger import PrintLogger

logger = getLogger(__name__)


def reload_mlbull_dummies():
    reload(mlbull_dummies)


def get_module_from_filename(filename: str, fullpath: str):
    logger.info(f"Loading module from {filename}")
    reload_mlbull_dummies()

    loader = SourceFileLoader(filename, filename)
    spec = spec_from_loader(filename, loader)

    if spec is None:
        raise Exception(f"Failed to import {filename})")

    module = module_from_spec(spec)
    # Add prefix to every print
    print_logger = PrintLogger(fullpath)
    module.__dict__["print"] = print_logger
    loader.exec_module(module)

    return module, print_logger


def get_decorators(module: ModuleType):
    try:
        return module.__dict__["predict_function"].gathered_functions
    except KeyError:
        logger.error(f"No predict_function defined in {module.__name__}")
        return []


def sanitize_module_name(name: str):
    name = name.removeprefix("./")
    if name.endswith(".py"):
        name = name[:-3]
    return name
