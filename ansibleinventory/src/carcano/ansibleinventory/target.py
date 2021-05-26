__author__="Marco Antonio Carcano"
__version__=  '1.0.0'


import logging 
 
"""
initialize logger to NullHandler
"""
log = logging.getLogger(__name__) 
log.addHandler(logging.NullHandler()) 

class Target():
  """
  Target class used to derive Host and Group classes
  """
  _variables = dict()
  _name = None
 
  def __init__(self,name):
    """
    Initalize a target with the supplied name
    """
    log.debug('Package: '+__name__+', Method: '+self.__init__.__qualname__)
    self.name=name
    self._variables = dict()
 
  @property
  def name(self):
    """
    get the name of the target
    """
    log.debug('Package: '+__name__+', Method: Target.name(self)')
    return self._name

  @name.setter
  def name(self,name):
    """
    Set the name of the target
    """
    log.debug('Package: '+__name__+', Method: Target.name(self,name)')
    if name == "" or name == None:
      raise ValueError("Target name cannot be empty")
    else:
      self._name = name
 
  def setVar(self,name,value):
    """
    add a varible to the list of variable that belogns to the target
    variables can either be of string, number, list or dictinary type
    """
    log.debug('Package: '+__name__+', Method: '+self.setVar.__qualname__)
    if name == "" or name == None:
      raise ValueError("The name of the variable to set cannot be empty")
    if value == "" or value == None:
      raise ValueError("The value of the variable to set cannot be empty")
    self._variables[name] = value
 
  def getVar(self,name):
    """
    retrieve the value of the given variable name from the list of variables
    that belongs to the target
    """
    log.debug('Package: '+__name__+', Method: '+self.getVar.__qualname__)
    if name == "" or name == None:
      raise ValueError("The name of the variable to get cannot be empty")
    return self._variables[name]
