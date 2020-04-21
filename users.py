from credentials import Credentials

class Users:
    users_list = []

    def __init__(self, username, password):
        """
        method to 
        """
        self.username = username
        self.password = password
    
    def save_user(self):
        
        """
        method to append the users to the users_list
        """

        Users.users_list.append(self)
    

    def del_user(self):
    
        """
        method to remove a user from the users_list
        """

        Users.users_list.remove(self)

    @classmethod
    def find_user(cls, username):

        """
        method to search a user from the users list based on the username
        """

        for user in cls.users_list:
            if user.username == username:
                return user
    
    @classmethod
    def check_user_exist(cls, username):

        """
        method to look up the existence of a user based on the username
        """

        for user in cls.users_list:
            if user.username == username:
                return True

    @classmethod
    def display_user(cls):
    
        """
        method to display all users in the users list
        """

        return cls.users_list
    
    def login(cls, username, password):
    
        """
        method to authenticate a user and log him or her into the system
        """
        for user in cls.users_list:
            if user.username == username and user.password == password:
                return Credentials.credentials_list