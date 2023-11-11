from ._base import Base


class Domain(Base):
    @property
    def _base_path(self):
        return "domains"
        
    def data(self, name, active):
        return {
            "name": name,
            "active": active,
        }
