'''Object Data Mapper for pulsar asynchronous framework'''
import os
from .version import get_version


VERSION = (0, 5, 0, 'alpha', 0)
__version__ = get_version(VERSION, __file__)


if os.environ.get('package_info') != 'odm':

    from .mapper import (Model, Mapper, OdmSession, logger, model_base,
                         BaseModel, table_args, declared_attr, copy_models,
                         move_models, get_models, ImproperlyConfigured)
    from .strategy import create_engine
    from . import dialects

    __all__ = ['BaseModel', 'Model', 'Mapper', 'OdmSession', 'logger',
               'model_base', 'table_args', 'create_engine', 'dialects',
               'declared_attr', 'copy_models', 'move_models', 'get_models',
               'ImproperlyConfigured']
