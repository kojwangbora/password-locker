#import relevant modules

from cgi import test
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

class TestCredentials(unittest.TestCase):
    """method runs before individual credential tests runs"""

    def setUp(self):
        """method runs before the credential test method"""

        self.new_credential= Credentials('Gmail','Kjwang_Bora', 'qwe12rTy')

    def test_init(self):
        """Testing case to check new Credentials have been initialized properly"""

        self.assertEqual(self.new_credential.account, 'Gmail')
        self.assertEqual(self.new_credential.userName, 'Kojwang_Bora')
        self.assertEqual(self.new_credential.password, 'qwe12rTy')
    
    def save_credential_test(self):
        """test to check if credential object is saved in the credential list"""

        self.new_credential.save_details()
        self.assertEqual(len(Credentials.credentials_list),1)
    
    def tearDown(self):
        '''A method that cleans up after the test case have run'''

        Credentials.credentials_list =[]
    
    def test_save_many_accounts(self):
        '''Tests to check if  it can save multiple credentials in our credential list'''

        self.new_credential.save_details()
        test_credential= Credentials("Instagram", "ochiengbora", "TiktakT5u")
        test_credential.save_details()
        self.assertEqual(len(Credentials.credentials_list),2)

    def test_delete_credential(self):
        """Test method for removing an account's credentials from the credential_list"""
        self.new_credential.save_details()
        test_credential = Credentials("Instagram", "ochiengbora", "TiktakT5u")
        test_credential.save_details()

        self.new_credential.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
    
    def test_find_credentials(self):
        """Test  to find a credential entry by account name and displays details of the credentials"""

        self.new_credential.save_details()
        test_credential = Credentials("Instagram", "ochiengbora", "TiktakT5u")
        test_credential.save_details()

        the_credential = Credentials.find_credentials("Instagram")

        self.assertEqual(the_credential.account,test_credential.account)
    
    def test_credential_exist(self):
        """Test to return a boolean based on whether we and or can't find the credential"""
        self.new_credential.save_details()
        the_credential = Credentials("Instagram", "ochiengbora", "TiktakT5u")
        the_credential.save_details()
        credential_is_found = Credentials.if_credential_exist("Instagram")
        self.assertTrue(credential_is_found)

