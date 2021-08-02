#!/usr/bin/env python3

proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
print(proto)
proto.append("dns")
protoa.append("dns")
proto2 = [22, 80, 443, 53]
proto.extend(proto2)
print(proto)
protoa.append(proto2)
print(protoa)


protoa.reverse()
print(protoa)

proto.pop(2)
print(proto)
