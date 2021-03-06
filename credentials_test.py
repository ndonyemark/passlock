import unittest
from credentials import Credentials

class Credentials_test(unittest.TestCase):
    
    def setUp(self):

        """
        instructions to run before any test is done
        """

        self.new_credentials = Credentials("ndonyemark", "instagram", "bossbaby")
    
    def test_init(self):
    
        """
        check if what is expected and what is passed in is as expected by the system
        """

        self.assertEqual(self.new_credentials.username, "ndonyemark")
        self.assertEqual(self.new_credentials.account_name, "instagram")
        self.assertEqual(self.new_credentials.account_password, "bossbaby")
    
    def tearDown(self):
    
        """
        method to resets the credentials list
        """

        Credentials.credentials_list = []
    
    def test_save_credential(self):
    
        """
        test if a credential is actually saved in the credentials list
        """

        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)
    
    def test_save_multiple_credentials(self):
    
        """
        test if the system can save multiple credentials
        """

        self.new_credentials.save_credentials()
        test_credentials = Credentials("toni", "twitter", "tweetme:)")
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 2)
    
    def test_delete_user(self):
    
        """
        test if the system actually deletes a credential
        """

        self.new_credentials.save_credentials()
        test_credentials = Credentials("toni", "twitter", "tweetme:)")
        test_credentials.save_credentials()
        self.new_credentials.del_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)
    
    def test_find_user_by_account_name(self):
    
        """
        method to test if you can lookup a credential based on the account_name
        """

        self.new_credentials.save_credentials()
        test_credentials = Credentials("toni", "twitter", "tweetme:)")
        test_credentials.save_credentials()
        found_credential = Credentials.find_by_account_name("twitter")
        self.assertEqual(found_credential.account_name, test_credentials.account_name)
    
    def test_check_credentials(self):
    
        """
        method to test if a credential really exists in the cerdentials list
        """

        self.new_credentials.save_credentials()
        test_credentials = Credentials("toni", "twitter", "tweetme:)")
        test_credentials.save_credentials()
        credential_exist = Credentials.check_credential_existence("twitter")
        self.assertTrue(credential_exist)
    
    def test_display_credentials(self):
    
        """
        method to test if theusers returned to the display credential equal the users list
        """

        self.assertEqual(Credentials.display_credentials(), Credentials.credentials_list)
    

if __name__ == '__main__':
    unittest.main()