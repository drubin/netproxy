#!/usr/bin/env python

import json
import re

json_config = open("config.json").read()

config = json.loads(json_config)

# Create the hosts file lines.
lines = ["%s %s\n" % (config["haproxy_bind_ip"], proxy["dest_addr"]) for proxy in config["proxies"]]

hosts = open("hosts", "w")
hosts.write("\n\n# netproxy IP section\n")
hosts.writelines(lines)
hosts.close()
