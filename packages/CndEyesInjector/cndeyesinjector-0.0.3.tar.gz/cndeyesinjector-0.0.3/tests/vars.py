import cndprint
import yaml


host = "cndeyesrails.test"
port = "443"
scheme = "https"
verify = False
user = "denis.fabien.ca@gmail.com"
password = "abcdef"
base_url = f"{scheme}://{host}:{port}"
# base_url = f"{scheme}://{host}"
_print = cndprint.CndPrint(level="trace", uuid=">> ", silent_mode=False)
_api_version = "v2"

def read_file(filename):
    return open(filename).read()
    
def read_yaml_file(filename):
    content = read_file(filename)
    return yaml.safe_load(content)
