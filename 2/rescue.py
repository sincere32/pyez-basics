#!/usr/bin/env python

from jnpr.junos import Device
from jnpr.junos.utils.config import Config

dev = Device(host='mx1',user='lab', passwd='lab123')

try:
    dev.open()
except ConnectError as err:
    print("Cannot connect to device: {0}".format(err))
    sys.exit(1)

# Loading the rescue config
print("### Loading the rescue config")
cu = Config(dev, mode='private')
cu.rescue(action="reload")
cu.pdiff()

cu.commit(comment="Loading the rescue config")

dev.close()
