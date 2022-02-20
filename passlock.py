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

         