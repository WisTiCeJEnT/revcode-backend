import unittest
import requests
import json
from testing_lib import *
class Testmultiply(unittest.TestCase):

    def setUp(self):
        pass
    def test_register_and_createfile(self):
        username="Juitanya"
        uid="0k_this_is_for_test_only"
        email="Juitanya@hotmail.com"
        print('Registering ...')

        response = addUser(username,uid,email)
        self.assertEqual(response,'ok')

        filename = "Test.py"
        extension = "py"
        print('Creating file...')

        response = addFile(uid,filename,extension)
        self.assertEqual(response,'ok')

        removeUser("0k_this_is_for_test_only")
    
    def test_create_read_delete_read(self):
        print('Adding File ...')
        response = addFile('testerid01', 'testfile002.py', 'py')
        self.assertEqual(response,'ok')

        print('Getting Files ...')
        response = getFiles("testerid01")
        self.assertEqual(response, 'ok')

        print('Removing Files ...')
        response = removeFile('testerid01', '-LsprOfW6dQrFLdq-dEu')
        self.assertEqual(response,'ok')

        print('Getting Files ...')
        response = getFiles("testerid01")
        self.assertEqual(response, 'ok')

        print('Finished')
if __name__ == '__main__':
    unittest.main()
