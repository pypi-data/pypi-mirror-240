class Base:
    @property
    def _base_path(self):
        return "stupid-path"
        
    def __init__(self, adapter):
        self._adapter = adapter
        
    def data(self):
        return {}
        
    def get(self):
        result = self._adapter._query(self._base_path)
        return result["content"]["items"]
        
    def create(self, data):
        result = self._adapter._query(f'{self._base_path}', method="post", json_data={self._base_path[:-1]: data})
        if result is False:
            return False
        return result["content"]["id"]
        
    def update(self, id, data):
        result = self._adapter._query(f'{self._base_path}/{id}', method="patch", json_data={self._base_path[:-1]: data})
        if result is False:
            return False
        return True
        
    def delete(self, id):
        result = self._adapter._query(f'{self._base_path}/{id}', method="delete")
        if result is False:
            return False
        return True
