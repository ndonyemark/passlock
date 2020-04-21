import unittest
from users import Users

class Users_test(unittest.TestCase):
    
    def setUp(self):
        
        """
        instructions to run before any test is done
        """
        
        self.new_user = Users("Toni", "Bossbaby")