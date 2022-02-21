#import relevant modules

from password_lock import User
from password_lock import Credentials
import unittest


class TestClass(unittest.TestCase):
    """ Test class defining the test cases for class User."""

    def setUp(self):
        """A method that runs  before the test methods run"""
        

        self.new_user = User('KojwangBora', 'Babu254@')

    