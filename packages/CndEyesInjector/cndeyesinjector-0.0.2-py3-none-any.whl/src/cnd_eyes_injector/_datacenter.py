from ._base import Base


class Datacenter(Base):
    @property
    def _base_path(self):
        return "datacenters"
        
    def data(self, name):
        return {
            "name": name
        }
