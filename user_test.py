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
    
    def test_delete_users(self):
        
        """
        test if the system actually deletes the users
        """

        self.new_user.save_user()
        test_user = Users("Mark", "justmark")
        test_user.save_user()
        self.new_user.del_user()
        self.assertEqual(len(Users.users_list), 1)
    
    def test_find_user_by_username(self):
        
        """
        method to test if you can lookup a user based on the username
        """

        self.new_user.save_user()
        test_user = Users("Mark", "justmark")
        test_user.save_user()
        found_user =Users.find_user("Mark")
        self.assertEqual(found_user.username, test_user.username)