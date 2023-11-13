from ._base import Base


class EnvironmentInfra(Base):
    @property
    def _base_path(self):
        return "environment_infras"
        
    def data(self, name, active):
        return {
            "name": name,
            "active": active
        }
