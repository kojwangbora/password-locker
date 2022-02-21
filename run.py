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
        short_code = input().lower().strip()
        if short_code == "cc":
            print("Create new Credential")
            print("."*20)
            print("Account name ...")
            account = input().lower()
            print("Your username")
            userName = input()
            while True:
                print("TP - To type your own pasword if you already have an account:\n GP - To generate random Password")
                password_Choice = input().lower().strip()
                if password_Choice == 'tp':
                    password = input("enter Your Own password\n")
                    break
                elif password_Choice == 'gp':
                    password = generate_Password()
                    break
                else:
                    print("You have entered an invalid password, please try again")
            save_credentials(create_new_credential(account,userName,password))
            print('\n')
            print(f"Account credential for: {account} - UserName: {userName} - Password: {password} created succedfully")
            print('\n')
        elif short_code == "dc":
            if display_accounts_details():
                print("Here is your list of accounts: ")

                print('*'*30)
                print('_'*30)
                for account in display_accounts_details():
                    print(f"Account: {account.account} \n User Name: {username}\n Password: {password}")
                    print('_'*30)
                print('*'*30)
            else:
                    print("You do not have any save credentials!")
        elif short_code == "fc":
            print ("Enter the name of account")
            search_name= input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print(f"Account Name: {search_credential.account}")
                print('_'*50)
                print(f"User Name: {search_credential.userName} Password : {search_credential.password}")
                print ('_'* 50)
            else:
                print("The Credential entered do not exist, please enter the correct ones")
                print('\n')
        elif short_code =="d":
            print("Enter the name of accont of the credentials to be deleted")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print("_"*50)
                search_credential.delete_credentials()
                print('\n')
                print(f"Your stored credentials from : {search_credential.account} you have successfully deleted the credential!")
                print('\n')
            else:
                print("The credential to be deleted does not exists!")
        elif short_code =='gp':


            password = generate_Password()
            print(f" {password} hass been successflly generated")






