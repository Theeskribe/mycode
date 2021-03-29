#!/usr/bin/env python3
proto = ["ssh", "http", "https"]
ports = [22, 80, 443, 53]
print(proto)
proto.append("dns")
print(proto)
stuff = proto + ports
print(stuff)
proto.append(ports)
print(proto)
