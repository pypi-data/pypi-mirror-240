import requests
import json
import yaml
import os
import urllib3
urllib3.disable_warnings()
from .adapter import Adapter
from ._app import App
from ._flavor import Flavor
from ._domain import Domain
from ._environment import Environment
from ._organization import Organization
from ._tier import Tier
from ._source import Source
from ._software import Software
from ._service import Service
from ._project import Project
from ._os_type import OsType
from ._licenced_app import LicencedApp
from ._cloud_account import CloudAccount
from ._customer import Customer
from ._datacenter import Datacenter
from ._deployment import Deployment
from ._environment_app import EnvironmentApp
from ._environment_infra import EnvironmentInfra
from ._hostname import Hostname
from ._vm_tag import VmTag
from ._vm import Vm
import re
import pathlib


class EyesInjector:
    def __init__(self, host, port, scheme, _print, verify=False):
        self._adapter = Adapter(host, port, scheme, _print, verify=verify)
        for sub_class_name in EyesInjector._get_all_subclass():
            sub_class = eval(sub_class_name)
            setattr(self, self.camel_to_snake(sub_class.__name__), sub_class(self._adapter))
        
    def camel_to_snake(self, name):
        name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()
        
    def connect(self, user, password):
        self._adapter.connect(user, password)
        
    @staticmethod
    def _filename_to_camel_case(filename):
        str = filename.split('.')[0][0:]
        temp = str.split('_')
        res = ''.join(ele.title() for ele in temp[0:])
        return res

    @staticmethod
    def _get_all_subclass():
        current_file_path = pathlib.Path(__file__).parent.resolve()
        files = filter(lambda my_file: (my_file[0] == '_' and my_file[1] != '_' and my_file != '_base.py'), os.listdir(current_file_path))
        my_list = list(files)
        return [EyesInjector._filename_to_camel_case(my_file) for my_file in my_list]
