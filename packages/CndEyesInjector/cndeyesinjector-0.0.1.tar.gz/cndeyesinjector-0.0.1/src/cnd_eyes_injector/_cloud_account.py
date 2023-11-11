from ._base import Base


class CloudAccount(Base):
    @property
    def _base_path(self):
        return "cloud_accounts"
        
    def data(self, name, source_name, active):
        return {
            "name": name,
            "source_name": source_name,
            "active": active,
        }
