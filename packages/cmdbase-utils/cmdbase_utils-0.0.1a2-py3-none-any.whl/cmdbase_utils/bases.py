from __future__ import annotations
from importlib import import_module

import inspect
import json
import logging
import logging.config
import os
import re
from argparse import ArgumentParser
from configparser import NoOptionError, NoSectionError
from contextlib import nullcontext
from pprint import pprint
from typing import Generic, Iterable, TypeVar, get_args

from tabulate import tabulate
from zut import _UNSET, ExtendedJSONEncoder, CommandManager

from .apiclient import CMDBaseApiClient
from .settings import CONFIG, OUT_BASE_DIR

logger = logging.getLogger(__name__)


class BaseContext:
    prog = 'cmdbase-utils'
    
    def __init__(self, arg: str = None):
        self.arg = arg
        self._cmdbase_apiclient: CMDBaseApiClient = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type=None, exc_val=None, exc_tb=None):
        pass


    @classmethod
    def get_available_args(cls):
        try:
            return cls._available_args
        except AttributeError:
            cls._available_args = []

            for section in CONFIG.sections():
                if section.startswith(f'{cls.prog}:'):
                    arg = section[len(f'{cls.prog}:'):]
                    cls._available_args.append(arg)

            return cls._available_args


    @classmethod
    def has_args(cls):
        return len(cls.get_available_args()) > 0
        

    @classmethod
    def add_argument(cls, parser: ArgumentParser):
        if args := cls.get_available_args():
            parser.add_argument('--context', '-c', choices=args, default=args[0], help=f"Context to use for {cls.prog}.")


    @classmethod
    def get_out_dir(cls):
        try:
            return cls._out_dir
        except:       
            pass

        subdir = cls.prog[len('cmdbase-'):] if cls.prog.startswith('cmdbase-') else cls.prog
        cls._out_dir = OUT_BASE_DIR.joinpath(subdir, "{context}" if cls.has_args() else "")
        return cls._out_dir
    

    @property
    def refprefix(self):
        return f"{self.arg.lower()}-" if self.arg else ""


    def report_items(self, itemname: str, data: list[dict], out: os.PathLike = None):
        if out == 'pprint':
            pprint(data, sort_dicts=False)
            
        elif m := re.match(r'^tab(?:\:(?P<format>.+))?$', out):
            dict_headers = {}
            for obj in data:
                for key in obj:
                    if isinstance(obj[key], dict):
                        dict_header = dict_headers.get(key)
                        if key in dict_headers:
                            dict_header = dict_headers[key]
                            if dict_header is None:
                                continue
                        else:
                            dict_header = []
                            dict_headers[key] = dict_header

                        for sub_key in obj[key]:
                            if not sub_key in dict_header:
                                dict_header.append(sub_key)


            headers = []
            for obj in data:
                for key in obj:
                    if not key in headers:
                        if key in dict_headers:
                            for sub_key in dict_headers[key]:
                                full_key = f"{key}.{sub_key}"
                                if not full_key in headers:
                                    headers.append(full_key)
                        else:
                            headers.append(key)
            
            rows = []
            for obj in data:
                row = []
                for header in headers:
                    value = obj
                    for part in header.split('.'):
                        value = value.get(part)
                        if value is None:
                            break
                    row.append(value)
                rows.append(row)
            
            print(tabulate(rows, headers=headers, tablefmt=m['format'] or 'simple'))
        
        elif out:
            if out == 'json':
                out = str(self.get_out_dir().joinpath(f"{itemname.lower()}.json")).format(context=self.arg)
            
            logger.info(f"export {itemname} data to {out}")

            os.makedirs(os.path.dirname(out), exist_ok=True)
            with open(out, 'w', encoding='utf-8') as fp:
                json.dump(data, fp=fp, indent=4, cls=ExtendedJSONEncoder, ensure_ascii=False)

        else:            
            logger.info(f"export {itemname} data to CMDBase")
            self.cmdbase_apiclient.report(data)


    @property
    def cmdbase_apiclient(self):
        if self._cmdbase_apiclient is None:
            base_url = self._get_option('api_base_url', fallback="http://localhost:8000/api")
            api_token = self._getsecret_option('api_token', fallback=None)
            self._cmdbase_apiclient = CMDBaseApiClient(base_url, api_token)
        
        return self._cmdbase_apiclient
    
    
    def _get_option(self, option: str, *, fallback = _UNSET) -> str:
        return self._func_option('get', option, fallback=fallback)
    
    def _getsecret_option(self, option: str, *, fallback = _UNSET) -> str:
        return self._func_option('get', option, fallback=fallback)
    
    def _getboolean_option(self, option: str, *, fallback = _UNSET) -> str:
        return self._func_option('getboolean', option, fallback=fallback)
    
    def _func_option(self, func_name: str, option: str, *, fallback = _UNSET):
        sections = ''

        if self.arg:
            sections = f"{self.prog}:{self.arg}"
            try:
                return getattr(CONFIG, func_name)(f"{self.prog}:{self.arg}", option)
            except (NoSectionError,NoOptionError):
                pass
    
        try:
            sections += (', ' if sections else '') + self.prog
            return getattr(CONFIG, func_name)(self.prog, option)
        except (NoSectionError,NoOptionError):
            pass
    
        try:
            sections += (', ' if sections else '') + 'cmdbase'
            return getattr(CONFIG, func_name)('cmdbase', option)
        except (NoSectionError,NoOptionError):
            pass
    
        if fallback is _UNSET:
            raise NoOptionError(option, sections)
        else:
            return fallback


T_Context = TypeVar('T_Context', bound=BaseContext)
T_Obj = TypeVar('T_Obj')

class BaseEntity(Generic[T_Context, T_Obj]):
    def __init__(self, context: T_Context, obj: T_Obj):
        self.context = context
        self.obj = obj
    

    @classmethod
    def get_itemname(cls) -> str:
        try:
            return cls.itemname
        except AttributeError:
            pass

        cls.itemname = cls.__name__.lower()
        if cls.itemname.endswith('entity') and len(cls.itemname) > len('entity'):
            cls.itemname = cls.itemname[:-len('entity')]
        return cls.itemname
    

    @classmethod
    def get_contexttype(cls) -> type[T_Context]:
        try:
            return cls.contexttype
        except AttributeError:
            pass

        cls.contexttype = _get_class_generic_definition(cls, BaseContext)
        return cls.contexttype


    @classmethod
    def get_objtype(cls) -> type[T_Obj]:
        try:
            return cls.objtype
        except AttributeError:
            pass

        if not hasattr(cls, 'objtype_parent'):
            raise ValueError(f"cannot determine objtype for {cls}, please provide objtype or objtype_parent")

        cls.objtype = _get_class_generic_definition(cls, cls.objtype_parent)
        return cls.objtype


    @classmethod
    def extract_doc(cls):
        return f"Collect and export {cls.get_itemname()} data."


    @classmethod
    def extract_add_arguments(cls, parser: ArgumentParser):
        parser.add_argument('--out', '-o', help="Output json file (default: send to CMDBase API).")
        cls.get_contexttype().add_argument(parser)


    @classmethod
    def extract_handle(cls, context: T_Context, out: os.PathLike = None, **kwargs):
        # Collect data
        logger.info(f"collect {cls.get_itemname()} data")
        
        data_headers = cls.collect_headers(context)

        data_list = []
        for obj in cls.extract_objs(context, **kwargs):
            entity = cls(context, obj)

            logger.info("collecting %s %s", cls.get_itemname(), entity.name)
            data = entity.collect()

            if data is not None:
                if isinstance(data, list):
                    for d in data:
                        data_list.append(d)
                else:
                    data_list.append(data)

        if not data_list:
            logger.warning(f"no {cls.get_itemname()} data collected")
            return
            
        # Export data
        if data_headers:
            if not isinstance(data_headers, list):
                data_headers = [data_headers]
            data_list = [*data_headers, *data_list]
            
        context.report_items(cls.get_itemname(), data_list, out)


    @classmethod
    def extract_objs(cls, context: T_Context, **kwargs) -> Iterable[T_Obj]:
        return NotImplementedError()
    
    @property
    def name(self) -> str:
        return NotImplementedError()
    
    @classmethod
    def collect_headers(cls, context: T_Context) -> dict|list[dict]|None:
        return None

    def collect(self) -> dict|list[dict]|None:
        return NotImplementedError()
    

def _get_class_generic_definition(leaf_cls: type, generic_base_cls: type) -> type:
    cls = leaf_cls
    while True:
        if not hasattr(cls, '__orig_bases__'):
            raise ValueError(f"{generic_base_cls.__name__} generic not found in {leaf_cls.__name__} hierarchy")
                
        for base in cls.__orig_bases__:
            for arg in get_args(base):
                if isinstance(arg, type) and issubclass(arg, generic_base_cls):
                    return arg

        if not cls.__base__:
            raise ValueError(f"{generic_base_cls.__name__} generic not found in {leaf_cls.__name__} hierarchy")
        cls = cls.__base__


def main_base(context_cls: type[BaseContext], add_arguments=None, default_handle=None, doc=None):
    """
    Reusable main function.
    """
    main_module = inspect.getmodule(inspect.stack()[1][0])
    root_module_name = main_module.__name__
    if root_module_name.endswith('.__main__'):
        root_module_name = root_module_name[:-len('.__main__')]
    prog = root_module_name.replace('_', '-').replace('.', '-')

    manager = CommandManager(main_module, prog=prog, add_arguments=add_arguments, default_handle=default_handle)
    manager.register_resource('context', context_cls)
    manager.main()
