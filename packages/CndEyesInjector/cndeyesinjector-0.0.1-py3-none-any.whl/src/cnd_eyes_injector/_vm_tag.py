from ._base import Base


class VmTag(Base):
    @property
    def _base_path(self):
        return "vm_tags"
        
    def data(self, vm_id, tag_id):
        return {
            "vm_id": vm_id,
            "tag_id": tag_id
        }
