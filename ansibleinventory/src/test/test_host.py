#!/usr/bin/env python3
import unittest

from carcano.ansibleinventory import *
#from ansibleinventory import Host
#from ansibleinventory import Target

class TestHost(unittest.TestCase):
    h=Host("ahost")
    def testHostInstance(self):
        self.assertIsInstance(self.h, Host)
    def testHostSetAndGetName(self):
        self.h.name="myhost.domain.local"
        self.assertEqual(self.h.name,"myhost.domain.local")
    def testHostSetNameWithEmptyVal(self):
        with self.assertRaisesRegex(ValueError, 'Target name cannot be empty'):
            self.h.name=""
    def testHostSetAndGetVar(self):
        self.h.setVar("description","Host I want to test")
        self.assertEqual(self.h.getVar("description"),"Host I want to test")
    def testHostSetVarWithEmptyName(self):
        with self.assertRaisesRegex(ValueError, 'The name of the variable to set cannot be empty'):
            self.h.setVar("","Host I want to test")
    def testHostSetVarWithEmptyValue(self):
        with self.assertRaisesRegex(ValueError, 'The value of the variable to set cannot be empty'):
            self.h.setVar("description","")

if __name__ == '__main__':
    unittest.main()
