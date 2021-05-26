__author__="Marco Antonio Carcano"
__version__=  '1.0.0'

import logging 

from .target import Target
  
log = logging.getLogger(__name__) 
log.addHandler(logging.NullHandler()) 

class Host(Target):
  """
  object representing an Ansible target host
  """
  def __init__(self,name):
    """
    initialize the host object
    """
    log.debug('Package: '+__name__+', Method: '+self.__init__.__qualname__)
    Target.__init__(self,name)

  def raw(self):
    """
    return a raw representation of the Host object.
    This can be used for example for yaml serialization
    """
    log.debug('Package: '+__name__+', Method: '+self.raw.__qualname__)
    yml=dict()
    yml[self._name]=self._variables
    return yml
