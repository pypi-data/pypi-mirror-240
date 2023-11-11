from ._base import Base


class Organization(Base):
    @property
    def _base_path(self):
        return "organizations"
        
    def data(self, name, guid, active):
        return {
            "name": name,
            "guid": guid,
            "active": active
        }
