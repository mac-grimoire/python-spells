#!/usr/bin/env python3
from carcano.foolist import *

d = Foolist()
d.append('RedHat',True)
d.append('Suse',True)
d.append('CentOS',False)
print("Print the list:")
for l in d:
  print(l)
print("Print the list in ascending order:")
for l in sorted(d):
  print(l)
d.remove('CentOS')
d.append('Rocky Linux',False)
print("Print the list - after the removal of CentOS:")
for l in d:
  print(l)


print("Print the list in descending order:")
for l in sorted(d,reverse=True):
  print(l)
