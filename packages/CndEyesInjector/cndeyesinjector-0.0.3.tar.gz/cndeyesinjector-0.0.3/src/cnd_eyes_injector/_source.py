from ._base import Base


class Source(Base):
    @property
    def _base_path(self):
        return "sources"
        
    def data(self, name, active):
        return {
            "name": name,
            "active": active
        }
