from ._base import Base


class Service(Base):
    @property
    def _base_path(self):
        return "services"
        
    def data(self, name, app_id, description, organizations_id, active):
        return {
            "name": name,
            "app_id": app_id,
            "description": description,
            "organizations_id": organizations_id,
            "active": active
        }

