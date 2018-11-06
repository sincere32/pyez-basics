#!/usr/bin/env python

from jnpr.junos import Device
from jnpr.junos.exception import ConnectError
from lxml import etree
from pprint import pprint
import sys

dev1 = Device(host='mx1',user='lab', passwd='lab123')

try:
    dev1.open()
except ConnectError as err:
    print ("Cannot connect to device: {0}".format(err))
    sys.exit(1)

# Full Config in XML format
print "### Full Config in XML format"
data = dev1.rpc.get_config()
print(etree.tostring(data, encoding='unicode'))

# Full Config in Text format (classic curly braces style)
print "### Full Config in TEXT format (curly braces)"
data = dev1.rpc.get_config(options={'format':'text'})
print(etree.tostring(data))

# Full Config in Text format (set commands)
print "### Full Config in TEXT format (set)"
data = dev1.rpc.get_config(options={'format':'set'})
print (etree.tostring(data))

# Full Config in JSON format
print "### Full Config in JSON format"
data = dev1.rpc.get_config(options={'format':'json'})
pprint (data)

# Specific Config in Text format
print "### Specific Config for system services"
data = dev1.rpc.get_config(filter_xml='<system><services/></system>', options={'format':'text'})
print(etree.tostring(data))


dev1.close()
