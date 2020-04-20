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
    
    def del_credentials(self):
    
        """
        method to remove a credential from the credentials_list
        """

        Credentials.credentials_list.remove(self)
    
    @classmethod
    def find_by_account_name(cls, account_name):

        """
        method to search a credential from the credentials list based on the account name
        """

        for account in cls.credentials_list:
            if account.account_name == account_name:
                return account
    
     @classmethod
    def check_credential_existence(cls, account_name):

        """
        method to look up the existence of a credential based on the account name
        """

        for account in cls.credentials_list:
            if account.account_name == account_name:
                return True