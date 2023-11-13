from ._base import Base


class Hostname(Base):
    @property
    def _base_path(self):
        return "hostnames"
        
    def data(self, name, domain_name):
        return {
            "name": name,
            "domain_name": domain_name
        }
