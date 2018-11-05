# Junos PyEZ Basics

[![Build Status](https://travis-ci.org/tplisson/pyez-basics.svg?branch=master)](https://travis-ci.org/tplisson/pyez-jinja2)

## Documentation Structure

[**1. Quick PyEZ Demo using the Python Interpreter**](README.md#1.-Quick-PyEZ-Demo-using-the-Python-Interpreter)

[**2. Handling Junos Configurations with PyEZ**](README.md#2.-Handling-Junos-Configurations-with-PyEZ)


# 1. Quick PyEZ Demo using the Python Interpreter
This is just a short demo to quickly show how the Python PyEZ library can help us 

More on PyEZ here:
https://junos-pyez.readthedocs.io/en/stable/
https://www.juniper.net/documentation/en_US/junos-pyez/information-products/pathway-pages/junos-pyez-developer-guide.html

---
## 1.1 Start a Docker container for the PyEZ environment
Using a Docker container greatly simplifies the environment setup for Python, PyEz and Ansible... It also keeps things clean and contained

```
docker run -it --rm -v $(pwd):/project --name pyez-ansible juniper/pyez-ansible ash
```
See Docker Hub for more info
https://hub.docker.com/r/juniper/pyez-ansible/

## 1.2 Start the Python interpreter
```
python
```

## 1.3 Getting the PyEZ module
Import the "Device" class from the PyEZ module (jnpr.junps)
```
from jnpr.junos import Device
```

Check out the documentation for the Device class
```
help(Device)
```

## 1.4 Open PyEZ/NETCONF connections
Create an instance of Device with the following variables:
- host = hostname or IP address (mandatory)
- user = username  (mandatory)
- passwd = password (can be empty when using SSH key)
- port = 830 (by default but can be changed if needed)

```
dev1 = Device(host='mx1',user='lab', passwd='lab123')
dev2 = Device(host='mx2',user='lab', passwd='lab123')
dev1.open()
dev2.open()
```

It's always a good idea to catch exceptions like this:
```
import sys
from jnpr.junos.exception import ConnectError

try:
    dev1.open()
except ConnectError as err:
    print ("Cannot connect to device: {0}".format(err))
    sys.exit(1)
```

## 1.5 Gather facts from devices

Print all facts from the Devices instance objects
```
print(dev1.facts)
print(dev2.facts)
```

Print only some specific facts
```
print(dev1.facts['hostname'])
print(dev1.facts['model'])
print(dev1.facts['version'])
```

Use Pretty Print instead
```
from pprint import pprint
pprint(dev1.facts)
pprint(dev2.facts)
```

Display facts in JSON format
```
import json
print (json.dumps(dev1.facts))
```

Display facts in YAML format
```
import yaml
print (yaml.dump(dev1.facts))
```

## 1.6 Close the PyEZ/NETCONF connection
Close the connection to the device.
```
dev.close()
```

## 1.7 Complete PyEZ Script
Create a script called 'get_facts.py'

```
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
```

Setting file permissions
```
chmod +x get_facts.py
```

Running the Python script
```
./get_facts.py
```
or
```
python get_facts.py
```

# 2. Handling Junos Configurations with PyEZ
Now exploring how to retrieve and modify the configuration of some Junos devices using PyEZ

## 2.1 Baseline script
Let's start with a simple script to open a NETCONF session to a single Junos device

```
from jnpr.junos import Device
from jnpr.junos.exception import ConnectError
import pprint
import sys

dev1 = Device(host='mx1',user='lab', passwd='lab123')

try:
    dev1.open()
except ConnectError as err:
    print ("Cannot connect to device: {0}".format(err))
    sys.exit(1)

print(dev1.facts['hostname'])
print(dev1.facts['model'])
print(dev1.facts['version'])


dev1.close()
```

## 2.2 Retrieving Junos configuration data
text

```
data = dev1.rpc.get_config()
print(etree.tostring(data, encoding='unicode'))
```
## 2. subtitle
text

```
cli
```
## 2. subtitle
text

```
cli
```
## 2. subtitle
text

```
cli
```
## 2. subtitle
text

```
cli
```
## 2. subtitle
text

```
cli
```
## 2. subtitle
text

```
cli
```
## 2. subtitle
text

```
cli
```
## 2. subtitle
text

```
cli
```
## 2. subtitle
text

```
cli
```
## 2. subtitle
text

```
cli
```
## 2. subtitle
text

```
cli
```
## 2. subtitle
text

```
cli
```
## 2. subtitle
text

```
cli
```
