from mockito import when, mock, unstub
from expects import *
from mamba import description, context, it
from requests_mock import Mocker
import tests.vars as vars
import src.cnd_eyes_injector as cnd_eyes_injector


file_path_base = "deployments"
with description('Deployment') as self:
    with before.each:
        unstub()
        self.instance_parent = cnd_eyes_injector.eyes_injector.EyesInjector(vars.host, vars.port, vars.scheme, vars._print, vars.verify)
        self.instance = self.instance_parent.deployment

    with context("__init__"):
        with it("shoud get an instance"):
            expect(isinstance(self.instance, cnd_eyes_injector._deployment.Deployment)).to(equal(True))

    with context("get", "get"):
        with it("shoud get"):
            with Mocker(real_http=True) as m:
                json_data = vars.read_yaml_file(f"tests/data/{file_path_base}/get.json")
                m.get(f'{vars.base_url}/api/{vars._api_version}/{file_path_base}', status_code=200, json=json_data)
                result = self.instance.get()
                expect(result).to(equal([{'id': 530, 'name': 'Jedha', "project_guid": "project_guid", "service_name": "service_name", "owner_name": "owner_name", "environment_name": "environment_name", "requester_name": "requester_name", "guid": "guid", "last_seen": "2023-01-01", "success": "2023-01-01", "finished": "2023-01-01", "item_created_at": "2023-01-01", "item_updated_at": "2023-01-01", "item_deleted_at": "2023-01-01", 'active': False}]))
                
    with context("create", "create"):
        with it("shoud create"):
            with Mocker(real_http=True) as m:
                json_data = vars.read_yaml_file(f"tests/data/{file_path_base}/post.json")
                m.post(f'{vars.base_url}/api/{vars._api_version}/{file_path_base}', status_code=201, json=json_data)
                result = self.instance.create(self.instance.data("Abcd", "project_guid", "service_name", "owner_name", "environment_name", "requester_name", "guid", "2023-01-01", "2023-01-01", "2023-01-01", "2023-01-01", "2023-01-01", "2023-01-01", True))
                expect(result).to(equal(533))
                
    with context("patch", "patch"):
        with it("shoud update"):
            with Mocker(real_http=True) as m:
                id = 456
                json_data = vars.read_yaml_file(f"tests/data/{file_path_base}/patch.json")
                m.patch(f'{vars.base_url}/api/{vars._api_version}/{file_path_base}/{id}', status_code=200, json=json_data)
                result = self.instance.update(id, self.instance.data("----", "project_guid", "service_name", "owner_name", "environment_name", "requester_name", "guid", "2023-01-01", "2023-01-01", "2023-01-01", "2023-01-01", "2023-01-01", "2023-01-01", True))
                expect(result).to(equal(True))
                
    with context("delete", "delete"):
        with it("shoud delete"):
            with Mocker(real_http=True) as m:
                id = 3
                m.delete(f'{vars.base_url}/api/{vars._api_version}/{file_path_base}/{id}', status_code=204, json={})
                result = self.instance.delete(id)
                expect(result).to(equal(True))
