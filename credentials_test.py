import unittest
from credential import Credentials

class Credentials_test(unittest.TestCase):
    
    def setUp(self):

        """
        instructions to run before any test is done
        """

        self.new_credentials = Credentials("ndonyemark", "instagram", "bossbaby")