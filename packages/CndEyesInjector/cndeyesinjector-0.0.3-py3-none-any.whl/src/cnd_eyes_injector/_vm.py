from ._base import Base


class Vm(Base):
    @property
    def _base_path(self):
        return "vms"
        
    def data(self, name, guid, domain_name, hostname_name, datacenter_name, source_name, deployment_guid, cloud_account_name, tier_name, os_type_name, software_name, cpu, memory, power_state, success, finished, item_created_at, item_updated_at, item_deleted_at, tags, ips, active):
        return {
            "name": name,
            "guid": guid,
            "domain_name": domain_name,
            "hostname_name": hostname_name,
            "datacenter_name": datacenter_name,
            "source_name": source_name,
            "deployment_guid": deployment_guid,
            "cloud_account_name": cloud_account_name,
            "tier_name": tier_name,
            "os_type_name": os_type_name,
            "software_name": software_name,
            "cpu": cpu,
            "memory": memory,
            "power_state": power_state,
            "success": success,
            "finished": finished,
            "item_created_at": item_created_at,
            "item_updated_at": item_updated_at,
            "item_deleted_at": item_deleted_at,
            "tags": tags,
            "ips": ips,
            "finished": finished,
            "active": active
        }
