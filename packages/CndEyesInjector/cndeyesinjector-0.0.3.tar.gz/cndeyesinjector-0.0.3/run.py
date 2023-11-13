#!/usr/bin/env python
import tests.vars as vars
import src.cnd_eyes_injector as cnd_eyes_injector

files = [
  'sources',
  'apps',
  'cloud_accounts',
  'customers',
  'datacenters',
  'domains',
  'environment_apps',
  'environment_infras',
  'environments',
  'flavors',
  'organizations',
  'projects',
  'services',
  'deployments',
  'tiers',
  'os_types',
  'softwares',
  'vms'
]
instance = cnd_eyes_injector.eyes_injector.EyesInjector(vars.host, vars.port, vars.scheme, vars._print, vars.verify)
instance.connect(vars.user, vars.password)

for file in files:
    print(f"loading file: {file}.yml")
    items = vars.read_yaml_file(f"sample/{file}.yml")
    for item in items:
        item_obj = getattr(instance, file[:-1])
        print(item)
        result = item_obj.create(item)
#        print(result)
#    print(content)
