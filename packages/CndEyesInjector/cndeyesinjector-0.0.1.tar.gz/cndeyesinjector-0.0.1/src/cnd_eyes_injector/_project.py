from ._base import Base


class Project(Base):
    @property
    def _base_path(self):
        return "projects"
        
    def data(self, name, guid, organization_name, source_name, active):
        return {
            "name": name,
            "guid": guid,
            "organization_name": organization_name,
            "source_name": source_name,
            "active": active
        }
