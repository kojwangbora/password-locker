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

def copy_password(account):
    """Copies password useing pypreclip, import the framework then declare the function that copies emails"""
    return Credentials.copy_password(account)


def passlocker():
    print("Welcome to Password Locker..\n Please follow the instructions below to proceed.\n CR --- Create New Account \n HA --- Have An Account \n")
    short_code = input("").lower().strip()
    if short_code == "cr":
        print("sign Up")
        print('*'*50)
        username = input("User_name: ")
        while True:
            print("T - To type your passcode: \n GP - Generate random Password")
            password_Choice = input().lower().strip()
            if password_Choice =='tp':
                password = input("Please Enter your password\n")
                break
            elif password_Choice =='gp':
                password = generate_Password()
                break
            else:
                print("you have entered an invalid password, please try again")
        save_user(create_new_user(username,password))
        print("*"*85)
        print(f"hello {username}, Success! Your account has been created. Your passsword is: {password}")
        print("*"*85)
    elif short_code == "li":
        print("*"*50)
        print("Please enter your username and password to login: ")
        print('*' * 50)
        username = input("User name: ")
        password = input(" password: ")
        login = login_user(username, password)
        if login_user == login:
            print(f"hello {username}.Welcome To Password Locker!")
            print('\n')
    while True:
        print( "Use the following short codes:\n cc - Create new credentals \n dc - Display Credentials \n fc- FIind credentials \n GP - Generate a random password \n d- Delete credential \n ex - Exi application \n")
        
