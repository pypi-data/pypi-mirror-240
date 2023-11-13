from ._base import Base


class Software(Base):
    @property
    def _base_path(self):
        return "softwares"
        
    def data(self, name):
        return {
            "name": name
        }
