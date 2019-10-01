#!/bin/env python3
from ipaddress import ip_address
import sys
ip=int(ip_address(sys.argv[1]))
print('==>',ip)
