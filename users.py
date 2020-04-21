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
    
    