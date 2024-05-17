from jinja2 import Environment, FileSystemLoader
import yaml

ENV = Environment(loader=FileSystemLoader('.'),trim_blocks=True, lstrip_blocks=True)
template = ENV.get_template("configtemplate.j2")

router_files = ["configR1.yml", "configR2.yml", "configR3.yml", "configR4.yml"]
# Iterate over each YAML file
for router_file in router_files:
    with open(router_file) as f:
      interfaces = yaml.load(f, Loader=yaml.SafeLoader)
      print(template.render(interface_list=interfaces))
