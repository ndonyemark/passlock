class Credentials:

    credentials_list = []

    def __init__(self, username, account_name, account_password):
        self.username = username
        self.account_name = account_name
        self.account_password = account_password
    
    def save_credentials(self):
    
        """
        method to append the credntials to the credentials_list
        """

        Credentials.credentials_list.append(self)