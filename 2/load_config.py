#!/usr/bin/env python

from jnpr.junos import Device
from jnpr.junos.utils.config import Config


dev = Device(host='mx1',user='lab', passwd='lab123')

try:
    dev.open()
except ConnectError as err:
    print ("Cannot connect to device: {0}".format(err))
    sys.exit(1)

# Loading Config from the file: 'configs/vpn1.conf'
print "### Loading Config from the file: 'configs/vpn1.conf'"
conf_file = "configs/vpn1.conf"
cu = Config(dev, mode='private')
cu.load(path=conf_file, merge=True)
cu.pdiff()

# Loading Config from the file: 'configs/op-script.conf'
print "### Loading Config from the file: 'configs/op-script.conf'"
conf_file = "configs/op-script.conf"
cu = Config(dev, mode='private')
cu.load(path=conf_file, merge=True)
cu.pdiff()

cu.commit(comment="Loading config from the 'configs' folder")

dev.close()
