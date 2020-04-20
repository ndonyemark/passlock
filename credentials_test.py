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