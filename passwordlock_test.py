#import relevant modules

from password_lock import User
from password_lock import Credentials
import unittest


class TestClass(unittest.TestCase):
    """ Test class defining the test cases for class User."""

    def setUp(self):
        """A method that runs  before the test methods run"""
        

        self.new_user = User('KojwangBora', 'Babu254@')
    
    def test_init(self):
        """Test case to check proper object initialization"""
        self.assertEqual(self.new_user.username, 'KojwangBora')
        self.assertEqual(self.new_user.password, 'Babu254@')
    
    def test_save_user(self):
        """Test case to check if the new user instance in saved into the User list"""

        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

class TestCredentials(unittest, unittest.TestCase):
    """method runs before individual credential tests runs"""

    def setUp(self):
        """method runs before the credential test method"""

        self.new_credential= Credentials('Gmail','Kjwang_Bora', 'qwe12rTy')

    def test_init(self):
        """Testing case to check new Credentials have been initialized properly"""

        self.assertEqual(self.new_credential.account, 'Gmail')
        self.assertEqual(self.new_credential.userName, 'Kojwang_Bora')
        self.assertEqual(self.new_credential.password, 'qwe12rTy')
    
    
         
    