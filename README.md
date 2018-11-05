# Junos PyEZ Basics

[![Build Status](https://travis-ci.org/tplisson/pyez-basics.svg?branch=master)](https://travis-ci.org/tplisson/pyez-jinja2)

## Documentation Structure

[**1. Quick PyEZ Demo using the Python Interpreter**](README.md#1.-Quick-PyEZ-Demo-using-the-python-interpreter)

[**2. Simple Python script with PyEZ**](README.md#2.-Simple-Python-script-with-PyEZ)


# 1. Quick PyEZ Demo using the Python Interpreter
This is just a short demo to quickly show how Jinja2 templates work with Python

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

## 1.4 Open NETCONF connections
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

## 1.5 Close the NETCONF connection
Close the connection to the device.
```
dev.close()
```



# 2. Pull and Push Junos Configurations via NETCONF
text

```
cli
```

## 2.1 Baseline script
text

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
## 2. subtitle
text

```
cli
```
