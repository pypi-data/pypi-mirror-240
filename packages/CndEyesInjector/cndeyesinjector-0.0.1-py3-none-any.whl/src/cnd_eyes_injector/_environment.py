from ._base import Base


class Environment(Base):
    @property
    def _base_path(self):
        return "environments"
        
    def data(self, name, environment_app, environment_infra, domain, active):
        return {
            "name": name,
            "environment_app_name": environment_app,
            "environment_infra_name": environment_infra,
            "domain_name": domain,
            "active": active
        }
