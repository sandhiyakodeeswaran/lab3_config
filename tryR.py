from jinja2 import Environment, FileSystemLoader
import yaml
import os

# Set up the Jinja2 environment
ENV = Environment(loader=FileSystemLoader('.'), trim_blocks=True, lstrip_blocks=True)
template = ENV.get_template("tryR.j2")

# Load the YAML file
with open("tryR.yml") as f:
    routers_data = yaml.load(f, Loader=yaml.SafeLoader)

# Iterate over each router configuration
for router in routers_data['routers']:
    output = template.render(routers=[router])
    # Print the output
    print(output)
