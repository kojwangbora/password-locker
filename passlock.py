#importing the relevant modules

import random
import string

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