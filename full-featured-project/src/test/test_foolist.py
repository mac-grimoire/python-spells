#!/usr/bin/env python3
import unittest
from collections.abc import Iterable

from carcano.foolist import *

class Foolist(unittest.TestCase):
    l=Foolist()
    def testFoolistIsIterable(self):
        self.assertIsInstance(self.l,Iterable)
    def testFoolistAppend(self):
        self.l.append('RedHat',True)
        self.l.append('CentOS',False)
        self.l.append('Suse',True)
        self.assertIn(FoolistItem('CentOS',False), self.l)
    def testFoolistRemove(self):
        self.l.remove('CentOS')
        self.assertNotIn(FoolistItem('CentOS',False), self.l)

if __name__ == '__main__':
    unittest.main()
