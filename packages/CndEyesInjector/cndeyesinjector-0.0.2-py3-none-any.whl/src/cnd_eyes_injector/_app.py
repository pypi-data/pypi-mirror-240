from ._base import Base


class App(Base):
    @property
    def _base_path(self):
        return "apps"
        
    def data(self, name, active):
        return {
            "name": name,
            "active": active
        }
