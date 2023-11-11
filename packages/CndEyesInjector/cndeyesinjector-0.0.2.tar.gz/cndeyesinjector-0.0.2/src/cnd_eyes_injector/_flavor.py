from ._base import Base


class Flavor(Base):
    @property
    def _base_path(self):
        return "flavors"
        
    def data(self, name, cpu, memory, active):
        return {
            "name": name,
            "cpu": name,
            "memory": memory,
            "active": active
        }
