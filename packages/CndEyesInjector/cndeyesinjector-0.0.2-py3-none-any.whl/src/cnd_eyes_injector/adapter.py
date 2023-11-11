import requests
import json
import yaml
import os
import urllib3
urllib3.disable_warnings()


class Adapter:
    def __init__(self, host, port, scheme, _print, verify=False):
        self._host = host
        self._port = port
        self._scheme = scheme
        self._base_host = f"{self._scheme}://{self._host}:{self._port}"
        self._verify = verify
        self._print = _print
        self._prefix = "/api/v2/"
        self.default_headers = {"Content-Type": "application/json", "Authorization": None}
        
    def _build_url(self, path):
        return f"{self._base_host}{self._prefix}{path}"
        
    def connect(self, user, password):
        if self.default_headers["Authorization"] is None:
            self._get_bearer(user, password)
        return True
        
    def _get_bearer(self, user, password):
        result = self._query(f"login/sign_in?email={user}&password={password}", method="post")
        if result["status_code"] != 200:
            return False
        self.default_headers["Authorization"] = result["headers"]["Authorization"]
        return True

    def _display_log(self, url, method, response):
        self._print.log_v(f'Url: {url}')
        self._print.trace_v(f'Method: {method}')
        self._print.trace_v(f'Status Code: {response.status_code}')
        self._print.trace_v(f'Response Content: {response.content}')
        
    def _query(self, url, method="get", json_data=None, retry=False, retry_count=3):
        if method not in ['get', 'post', 'delete', 'patch', 'put']:
            raise AttributeError("(CND) Method not allowed")
        full_url = self._build_url(url)
        self.kwargs = {}
        if json_data is not None:
            self.kwargs["json"] = json_data
        response = getattr(requests, method)(
            full_url,
            headers=self.default_headers,
            verify=False,
            **self.kwargs
        )
        self._display_log(full_url, method, response)
        if response.status_code == 204:
            return {
                "content": {},
                "status_code": response.status_code
            }
        if response.status_code in [200, 201, 202, 404]:
            return {
                "content": json.loads(response.content),
                "status_code": response.status_code,
                "headers": response.headers
            }
        self._print.log_e(f'Error with status code: {response.status_code}')
        return False
