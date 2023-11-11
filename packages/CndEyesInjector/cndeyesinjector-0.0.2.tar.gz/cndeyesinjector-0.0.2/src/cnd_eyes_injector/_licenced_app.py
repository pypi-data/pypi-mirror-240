from ._base import Base


class LicencedApp(Base):
    @property
    def _base_path(self):
        return "licenced_apps"
        
    def data(self, name, max, renew_date, renew_before, active):
        return {
            "name": name,
            "max": max,
            "renew_date": renew_date,
            "renew_before": renew_before,
            "active": active
        }

