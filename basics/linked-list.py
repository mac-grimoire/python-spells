#!/usr/bin/env python3
class DistroItem:
  _name = ""
  _commercial = False
  _next=None

  def __init__(self,name,commercial=False):
    self._name=name
    self._commercial=commercial
    self._next=None

  def __repr__(self):
    return f"OS: {self._name}, Commercial: {self._commercial}"

  @property
  def next(self):
    return self._next

  @next.setter
  def next(self, node):
    self._next = node

  @property
  def name(self):
    return self._name

  @name.setter
  def name(self,name):
    self._name=name

  @property
  def commercial(self):
    return self._commercial

  @commercial.setter
  def commercial(self,commercial):
    self._commercial=commercial

class Distro:
  def __init__(self):
    self.head = None

  def __iter__(self):
    node = self.head
    while node is not None:
      yield node
      node = node._next

  def append(self, name, commercial=False):
    if self.head == None:
       self.head = DistroItem(name,commercial)
       return
    for current_node in self:
        pass
    current_node.next=DistroItem(name,commercial)
 
  def remove(self,name):
    for f in self:
      if f.name==name:
        if f==self.head:
          self.head=f._next
        else:    
          hold._next=f._next
        del f
      else:
        hold=f

  def __repr__(self):
    nodes = []
    for node in self:
        nodes.append(node._name)
    return " -> ".join(nodes)

d = Distro()
d.append('RedHat',True)
d.append('CentOS',False)
#d.remove('RedHat')
#d.remove('CentOS')
d.append('Foo',True)

for l in d:
  print(l)
