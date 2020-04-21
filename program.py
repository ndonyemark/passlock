from credentials import Credentials
from users import Users
import time
import secrets
import string

def create_user(username, password):
    new_user = Users(username, password)
    return new_user

def save_users(user):
    user.save_user()

def del_user(user):
    user.delete_user()

def find_user(username):
    return Users.find_user(username)

def check_user(username):
    return Users.check_user_exist(username)

def display_user():
    return Users.display_user()

def login(username, password):
    login = Users.login(username, password)
    if login != False:
        return Users.login(username, password)

def main():
    name = input("Enter your name: ")

    print(f"Welcome {name}. What would you like to do?")