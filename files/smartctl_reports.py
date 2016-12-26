from pySMART import Device
import yaml
import re
import sys
sda = Device(sys.argv[1])
yaml_str = yaml.dump(sda, canonical = False, default_flow_style = False )
print re.sub(r"!!python/object.*\n *",r"",yaml_str)
