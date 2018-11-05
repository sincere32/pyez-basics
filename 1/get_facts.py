#!/usr/bin/env python

from jnpr.junos import Device
from jnpr.junos.exception import ConnectError
import pprint
import sys

dev1 = Device(host='mx1',user='lab', passwd='lab123')
dev2 = Device(host='mx2',user='lab', passwd='lab123')

try:
    dev1.open()
    dev2.open()
except ConnectError as err:
    print ("Cannot connect to device: {0}".format(err))
    sys.exit(1)

print(dev1.facts['hostname'])
print(dev1.facts['model'])
print(dev1.facts['version'])

print(dev2.facts['hostname'])
print(dev2.facts['model'])
print(dev2.facts['version'])

dev1.close()
dev2.close()
