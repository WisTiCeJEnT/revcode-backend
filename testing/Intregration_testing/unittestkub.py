import unittest
import requests
import json
import testing_lib
class Testmultiply(unittest.TestCase):
   
    def setUp(self):
        pass
    def test_register(self):
        username=input("Username : ")
        uid=input("UID : ")
        email=input("Email : ")
    
        response = testing_lib.addUser(username,uid,email)
        self.assertEqual(response,'ok')
    '''
    def test_addfile(self):
        response = testing_lib.addFile("f0rtest_0nly","Testfile.py","py")
        self.assertEqual(response,'ok')
    def test_getallfiles(self):
        response = testing_lib.getFiles("f0rtest_0nly")
        print("All files : "+str(response))
      #  self.assertEqual(response,'ok')
    def test_save_file(self):
        response = testing_lib.saveFile()
    '''


if __name__ == '__main__':
    unittest.main()