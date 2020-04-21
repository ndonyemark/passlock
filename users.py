from credential import Credentials

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