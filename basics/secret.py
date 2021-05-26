#!/usr/bin/env python3

import json

class JsonSerializable(object):
  def toJson(self):
    return json.dumps(self.__dict__)

  def __repr__(self):
    return self.toJson()

  def __init__(self, data):
    self.__dict__ = json.loads(data)

class Secret(JsonSerializable):
  _name=None
  _username=None
  _password=None
  
  @property
  def name():
    return self._name

  @name.setter
  def name(self,name):
    if name == "" or name == None:
      raise ValueError("The name of the Secret cannot be empty")
    else:
      self._name = name

  @property
  def username():
    return self._username

  @username.setter
  def username(self,username):
    if username == "" or username == None:
      raise ValueError("The username of the Secret cannot be empty")
    else:
      self._username = username

  @property
  def password():
    return self._password

  @password.setter
  def password(self,password):
    if password == "" or password == None:
      raise ValueError("The password of the Secret cannot be empty")
    else:
      self._password = password

  @property
  def url():
    return self._url

  @url.setter
  def url(self,url):
    if url == "" or url == None:
      raise ValueError("The url of the Secret cannot be empty")
    else:
      self._url = url

jsonstr= '{"_name": "a web server", "_username": "carma", "_password": "poorsecret", "_url": "http://www.carcano.local"}'

secret=Secret(jsonstr)
print("secret initialized from the json string")
print(secret)
secret.name="localE web server"
secret.password="itisnotasecret"
secret.url="http://www.carcano.local/login/"
print("secret after modifying some attributesd")
print(secret)
