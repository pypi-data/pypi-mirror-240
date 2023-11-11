from mockito import when, mock, unstub
from expects import *
from mamba import description, context, it
from requests_mock import Mocker
import tests.vars as vars
import src.cnd_eyes_injector as cnd_eyes_injector


with description('App') as self:
    with before.each:
        unstub()
        self.instance_parent = cnd_eyes_injector.eyes_injector.EyesInjector(vars.host, vars.port, vars.scheme, vars._print, vars.verify)
        setattr(self.instance_parent, 'base', cnd_eyes_injector._base.Base(self.instance_parent._adapter))
        self.instance = self.instance_parent.base
#        self.instance_parent.get_bearer(vars.user, vars.password)

    with context("__init__"):
        with it("shoud get an instance"):
            expect(isinstance(self.instance, cnd_eyes_injector._base.Base)).to(equal(True))

    with context("get", "get"):
        with it("shoud get"):
            with Mocker(real_http=True) as m:
                json_data = vars.read_yaml_file("tests/data/apps/get.json")
                m.get(f'{vars.base_url}/api/v2/{self.instance._base_path}', status_code=200, json=json_data)
                result = self.instance.get()
                expect(result).to(equal([{'id': 530, 'name': 'Jedha', 'active': False}]))
                
    with context("create", "create"):
        with it("shoud create"):
            with Mocker(real_http=True) as m:
                json_data = vars.read_yaml_file("tests/data/apps/post.json")
                m.post(f'{vars.base_url}/api/v2/{self.instance._base_path}', status_code=201, json=json_data)
                result = self.instance.create(self.instance.data())
                expect(result).to(equal(533))
                
    with context("patch", "patch"):
        with it("shoud update"):
            with Mocker(real_http=True) as m:
                id = 456
                json_data = vars.read_yaml_file("tests/data/apps/patch.json")
                m.patch(f'{vars.base_url}/api/v2/{self.instance._base_path}/{id}', status_code=200, json=json_data)
                result = self.instance.update(id, self.instance.data())
                expect(result).to(equal(True))
                
    with context("delete", "delete"):
        with it("shoud delete"):
            with Mocker(real_http=True) as m:
                id = 3
                m.delete(f'{vars.base_url}/api/v2/{self.instance._base_path}/{id}', status_code=204, json={})
                result = self.instance.delete(id)
                expect(result).to(equal(True))


