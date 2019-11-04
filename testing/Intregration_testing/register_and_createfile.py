import unittest
import requests
import json
import testing_lib
class Testmultiply(unittest.TestCase):

    def setUp(self):
        pass
    def test_register_and_createfile(self):
        username="Juitanya"
        uid="0k_this_is_for_test_only"
        email="Juitanya@hotmail.com"
        print('Registering ...')

        response = testing_lib.addUser(username,uid,email)
        self.assertEqual(response,'ok')

        filename = "Test.py"
        extension = "py"
        print('Creating file...')

        response = testing_lib.addFile(uid,filename,extension)
        self.assertEqual(response,'ok')

        testing_lib.removeUser("0k_this_is_for_test_only")
    


if __name__ == '__main__':
    unittest.main()