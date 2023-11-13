from ._base import Base


class OsType(Base):
    @property
    def _base_path(self):
        return "os_types"
        
    def data(self, name):
        return {
            "name": name
        }
