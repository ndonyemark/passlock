import unittest
from users import Users

class Users_test(unittest.TestCase):
    
    def setUp(self):
        
        """
        instructions to run before any test is done
        """
        
        self.new_user = Users("Toni", "Bossbaby")
    
    def test_init(self):
        
        """
        check if what is expected and what is passed in is as expected by the system
        """

        self.assertEqual(self.new_user.username, "Toni")
        self.assertEqual(self.new_user.password, "Bossbaby")
    
    def tearDown(self):
    
        """
        method to resets the users list
        """

        Users.users_list = []
    
    def test_save(self):
        
        """
        test if a user is actually saved in the users list
        """

        self.new_user.save_user()
        self.assertEqual(len(Users.users_list), 1)