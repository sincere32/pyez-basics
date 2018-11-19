# Junos PyEZ Basics

[![Build Status](https://travis-ci.org/tplisson/pyez-basics.svg?branch=master)](https://travis-ci.org/tplisson/pyez-jinja2)

## Documentation Structure

[**1. Quick PyEZ Demo using the Python Interpreter**](README.md#1.-Quick-PyEZ-Demo-using-the-Python-Interpreter)

[**2. Handling Junos Configurations with PyEZ**](README.md#2.-Handling-Junos-Configurations-with-PyEZ)


# 1. Quick PyEZ Demo using the Python Interpreter
This is just a short demo to quickly show how the Python PyEZ library can help us 

More on PyEZ here:
 - https://junos-pyez.readthedocs.io/en/stable/
 - https://www.juniper.net/documentation/en_US/junos-pyez/information-products/pathway-pages/junos-pyez-developer-guide.html


---
## 1.1 Start a Docker container for the PyEZ environment
Using a Docker container greatly simplifies the environment setup for Python, PyEz and Ansible... It also keeps things clean and contained

```
docker pull juniper/pyez

docker run -it --rm -v $(pwd):/project juniper/pyez
```
See Docker Hub for more info: 
https://hub.docker.com/r/juniper/pyez-ansible/

## 1.2 Start the Python interpreter
```
python
```

## 1.3 Getting the PyEZ module
Import the "Device" class from the PyEZ module (jnpr.junps)
```python
from jnpr.junos import Device
```

Check out the documentation for the Device class
```python
help(Device)
```

## 1.4 Open PyEZ/NETCONF connections
Create an instance of Device with the following variables:
- host = hostname or IP address (mandatory)
- user = username  (mandatory)
- passwd = password (can be empty when using SSH key)
- port = 830 (by default but can be changed if needed)

```python
dev1 = Device(host='mx1',user='lab', passwd='lab123')
dev2 = Device(host='mx2',user='lab', passwd='lab123')
dev1.open()
dev2.open()
```

It's always a good idea to catch exceptions like this:
```python
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
```python
print(dev1.facts)
print(dev2.facts)
```

Print only some specific facts
```python
print(dev1.facts['hostname'])
print(dev1.facts['model'])
print(dev1.facts['version'])
```

Use Pretty Print instead
```python
from pprint import pprint
pprint(dev1.facts)
pprint(dev2.facts)
```

Display facts in JSON format
```python
import json
print (json.dumps(dev1.facts))
```

Display facts in YAML format
```python
import yaml
print (yaml.dump(dev1.facts))
```

## 1.6 Close the PyEZ/NETCONF connection
Close the connection to the device.
```python
dev.close()
```

## 1.7 Complete PyEZ Script
Create a script called 'get_facts.py'

```python
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


Running the Python script
```
python get_facts.py
```
or

Setting file permissions before running the Python script
```
chmod +x get_facts.py

./get_facts.py
```




# 2. Handling Junos Configurations with PyEZ
Now exploring how to retrieve and modify the configuration of some Junos devices using PyEZ

## 2.1 Baseline script
Let's start with a simple script to open a NETCONF session to a single Junos device

```python
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
Retrieve the full config in XML format
```python
from lxml import etree

data = dev1.rpc.get_config()
print(etree.tostring(data, encoding='unicode'))
```

In Text format (classic curly braces style)
```python
data = dev1.rpc.get_config(options={'format':'text'})
print(etree.tostring(data))
```

In Text format (set commands)
data = dev1.rpc.get_config(options={'format':'set'})
print (etree.tostring(data))


In JSON format
```python
data = dev1.rpc.get_config(options={'format':'json'})
pprint (data)
```

Retrieving only specific parts of the configuration. This is achieved with the 'filter_xml' argument with the correct XML XPath. Here we look at the XPath: 'system/services'
```python
data = dev1.rpc.get_config(filter_xml='<system><services/></system>', options={'format':'text'})
print(etree.tostring(data))
```

## 2.3 Complete PyEZ Script

```python
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
print "# Full Config in XML format"
data = dev1.rpc.get_config()
print(etree.tostring(data, encoding='unicode'))

# Full Config in Text format (classic curly braces style)
print "# Full Config in TEXT format (curly braces)"
data = dev1.rpc.get_config(options={'format':'text'})
print(etree.tostring(data))

# Full Config in Text format (set commands)
print "# Full Config in TEXT format (set)"
data = dev1.rpc.get_config(options={'format':'set'})
print (etree.tostring(data))

# Full Config in JSON format
print "# Full Config in JSON format"
data = dev1.rpc.get_config(options={'format':'json'})
pprint (data)

# Specific Config in Text format
data = dev1.rpc.get_config(filter_xml='<system><services/></system>', options={'format':'text'})
print(etree.tostring(data))

dev1.close()
```


## 2.4 Loading a Junos configuration
Loading (merge) and committing some Junos config in text format (curly braces style)

```
from jnpr.junos.utils.config import Config


```

... TBC


## 2. subtitle
text

```
cli
```
