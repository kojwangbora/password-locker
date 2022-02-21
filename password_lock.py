#importing the relevant modules

import random
import string

import pyperclip

class User:
    """
    Creates user class that generates new user instances
    """
    user_list =[]

    def __init__(self, username, password):
        """
        method defines the user properties.
        """
        self.username = username
        self.password = password
    
    def save_user(self):
        """
        A method that saves a new user  into the user list
        """
        User.user_list.append(self)
    

    @classmethod
    
    def display_user(cls):
        return  cls.user_list
    
    def delete_user(self):
        '''
        delete_account method deletes a saved account from the list
        '''
        User.user_list.remove(self)

class Credentials():
    """

    Create credential class to help increating new credential objects
    """
    credentials_list= []
    @classmethod

    def verify_user(cls, username, password):
        """
        method to verify th euser in in the user_list
        """
        a_user =""
        for user in User.user_list:
            if(user.username == username and user.password == password):
                a_user == user.username
        return a_user
    
    def __init__(self, account, userName, password):
        """
        method defines user credentials that are to be stored
        """
        self.account = account
        self.userName = userName
        self.password = password
        
    def save_details(self):
        """
        method to store new credential 
        """
        Credentials.credentials_list.append(self)
    
    def delete_credentials(self):
        """

        delete_credentials, a method that deletes account's credentials from the credentials_listt
        """
        Credentials.credentials_list.remove(self)
    
    @classmethod
    def find_credentials(cls, account):
        """
         A method taking in account_name and returns credentials matching the account_name
         """
        for credential in cls.credentials_list:
            if credential.account == account:
                return credential
    @classmethod
    def copy_password(cls, account):
        found_credentials = Credentials.find_credentials(account)
        pyperclip.copy(found_credentials.password)
    
    @classmethod
    def if_credential_exist(cls, account):
        """
        Method checking credentials exist in the credential list and returns true or false  depending if the credential exists.
        """
        for credential in cls.credentials_list:
            if credential.account == account:
                return True
        return False
    @classmethod
    def display_credentials(cls):
        """

        Method returning all the items in credential list
        """
        return cls.credentials_list
    
    def generatePassword(stringLength=8):
        """
        Generate random password string of letters and integers and special characters
        """
        password = string.ascii_uppercase +string.ascii_lowercase + string.digits + "~!@#$%^&*"
        return ''.join(random.choice(password) for i in range(stringLength))
