from ._base import Base


class EnvironmentApp(Base):
    @property
    def _base_path(self):
        return "environment_apps"
        
    def data(self, name, active):
        return {
            "name": name,
            "active": active
        }
