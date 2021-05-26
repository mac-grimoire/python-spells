__author__="Marco Antonio Carcano"
__version__=  '1.0.0'

import logging 

from .target import Target
  
log = logging.getLogger(__name__) 
log.addHandler(logging.NullHandler()) 

class Group(Target):
  """
  object representing a group of ansible hosts
  """
  _hosts = list()
  _groups = list()

  def __init__(self,name):
    """
    initialize the object
    """
    log.debug('Package: '+__name__+', Method: '+self.__init__.__qualname__)
    Target.__init__(self,name)
    self._hosts = list()
    self._groups = list()

  def raw(self):
    """
    return a raw representation of the Group object.
    This can be used for example for yaml serialization
    """
    log.debug('Package: '+__name__+', Method: '+self.raw.__qualname__)
    yml=dict()
    d=dict()
    g=dict()
    h=dict()
    dict_children=dict()
    if len(self._variables) > 0:
      d['vars']=self._variables
    if len(self._hosts) > 0:
      for host in self._hosts:
        h.update(host.raw())
      d['hosts']=h
    elif len(self._groups) > 0:
      for group in self._groups:
        p=dict()
        p[group.name]=dict()
        g.update(p)
      d['children']=g
    yml[self._name]=d
    return yml

  def addGroup(self,group):
    """
    add a nested group to the group
    """
    log.debug('Package: '+__name__+', Method: '+self.addGroup.__qualname__)
    if len(self._hosts) > 0:
      raise ValueError("You cannot add a group to a group that already contains hosts")
    self._groups.append(group)

  def addHost(self,host):
    """
    add an host to the group
    """
    log.debug('Package: '+__name__+', Method: '+self.addHost.__qualname__)
    if len(self._groups) > 0:
      raise ValueError("You cannot add a hosts to a group that already contains groups")
    self._hosts.append(host)

  def getHostByName(self,name):
    """
    get a reference to a given Host object belonging to the group
    seeking it by its name
    """
    log.debug('Package: '+__name__+', Method: '+self.getHostByName.__qualname__)
    for host in self._hosts:
      if host.name == name:
        return host
    return None
