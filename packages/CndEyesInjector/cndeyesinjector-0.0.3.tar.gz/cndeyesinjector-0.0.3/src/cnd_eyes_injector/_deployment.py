from ._base import Base


class Deployment(Base):
    @property
    def _base_path(self):
        return "deployments"
        
    def data(self, name, project_guid, app_name, owner_name, environment_name, requester_name, guid, last_seen, success, finished, item_created_at, item_updated_at, item_deleted_at, active):
        return {
            "name": name,
            "project_guid": project_guid,
            "app_name": app_name,
            "owner_name": owner_name,
            "environment_name": environment_name,
            "requester_name": requester_name,
            "guid": guid,
            "last_seen": last_seen,
            "success": success,
            "finished": finished,
            "item_created_at": item_created_at,
            "item_updated_at": item_updated_at,
            "item_deleted_at": item_deleted_at,
            "active": active
        }
