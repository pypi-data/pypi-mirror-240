from ._base import Base


class Tier(Base):
    @property
    def _base_path(self):
        return "tiers"
        
    def data(self, name, active):
        return {
            "name": name,
            "active": active
        }
