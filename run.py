#import relevant module
from password_lock import User
from password_lock import Credentials

def function():
    print(" Welcome to Password Locker!😄 ")
function()

def create_new_user(username,password):
    '''Function creates a new user with password and username'''
    new_user = User(username,password)
    return new_user

def save_user(user):
    '''This fn saves a new user'''
    user.save_user()
def display_user():
    """fn displays existing user"""
    return User.display_user()
def login_user(username,password):
    """ fn checks existing user then logs user in"""

    check_user = Credentials.verify_user(username, password)
    return check_user

def create_new_credential(account, userName, password):
    """function creates new credentials for  user account"""
    new_credential = Credentials(account,userName,password)
    return new_credential
def save_credentials(credentials):
    """Function saves Credentials in the credential list"""
    credentials.save_details()
def display_accounts_details():
    """Function returns all saved credentials"""
    return Credentials.display_credentials()
def delete_credential(credentials):
    """Function deletes a Credentials from credentials list"""
    credentials.delete_credentials()

def find_credential(account):
    """Function finds Credentials  using account name and returns Credentials belonging to the relevant account"""
    return Credentials.find_credentials(account)
def check_credentials(account):
    """Function check Credentials with a specific account name to return either true or false"""
    return Credentials.if_credential_exist(account)

def generate_Password():
    '''generates random user password'''
    auto_password=Credentials.generatePassword()
    return auto_password

 

    