__author__="Marco Antonio Carcano"
__version__=  '1.0.0'

import logging 
  
from .host import Host
from .group import Group

log = logging.getLogger(__name__) 
log.addHandler(logging.NullHandler()) 

class Inventory():
  """
  Ansible Inventory object
  """
  _children = list()
  _variables = dict()

  def __init__(self):
    """
    initialize the ansible inventory
    """
    log.debug('Package: '+__name__+', Method: '+self.__init__.__qualname__)
    self.addGroup(Group('ungrouped'))

  def setVar(self,name,value):
    """
    add a variable to the list of globa variables (the variables defined
    for every host and group
    """
    log.debug('Package: '+__name__+', Method: '+self.setVar.__qualname__)
    if name == "" or name == None:
      raise ValueError("The name of the variable to set cannot be empty")
    if value == "" or value == None:
      raise ValueError("The value of the variable to set cannot be empty")
    self._variables[name] = value

  def getVar(self,name):
    """
    get the value of a global variable seeking it by name
    """
    log.debug('Package: '+__name__+', Method: '+self.getVar.__qualname__)
    if name == "" or name == None:
      raise ValueError("The name of the variable to get cannot be empty")
    return self._variables[name]

  def addGroup(self,group):
    """
    add a group to the inventory
    """
    log.debug('Package: '+__name__+', Method: '+self.addGroup.__qualname__)
    self._children.append(group)

  def addHost(self,host,groupname='ungrouped'):
    """
    add a host to the specified group, or to the "ungrouped" group is nothing
    is specified
    """
    log.debug('Package: '+__name__+', Method: '+self.addHost.__qualname__)
    if groupname == 'ungrouped':
      self._children[0].addHost(host)
    else:
      self._children[self.getGroupIndexByName(groupname)].addHost(host)

  def getGroupIndexByName(self,name):
    """
    get the index of the given group in the list of groups of the inventory
    """
    log.debug('Package: '+__name__+', Method: '+self.getGroupIndexByName.__qualname__)
    for i, child in enumerate(self._children):
      if child.name == name:
        return i
    return -1

  def getGroupByName(self,name):
    """
    get a reference to the given group
    """
    log.debug('Package: '+__name__+', Method: '+self.getGroupByName.__qualname__)
    for child in self._children:
      if child.name == name:
        return child
    return None

  def getHostByName(self,name):
    """
    get a reference to the given host
    """
    log.debug('Package: '+__name__+', Method: '+self.getHostByName.__qualname__)
    for group in self._children:
      host=group.getHostByName(name)
      if host != None:
        return host
    return None

  def raw(self):
    """
    return a raw representation of the Inventory object.
    This can be used for example for yaml serialization
    """
    log.debug('Package: '+__name__+', Method: '+self.raw.__qualname__)
    yml=dict()
    dict_all=dict()
    dict_children=dict()
    if len(self._children) > 0:
      for child in self._children:
        dict_children.update(child.raw())
      dict_all['children']=dict_children
    if len(self._variables) > 0:
      dict_all['vars']=self._variables
    yml['all']=dict_all
    return yml
