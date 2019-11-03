import unittest
import requests
from mult import multiply
class Testmultiply(unittest.TestCase):
    def setUp(self):
        pass
    def test_GET_user_data(self):
        res = requests.get("https://revcode.herokuapp.com/userdata?uid=cidCuqVCQ5OKf26IAGjKRr8mLA82")
        txt = res.json()
        for i in txt:
            print(i)
        self.assertEqual(res.text,'Woring')
 #   def test_numbers_3_4(self):
  #      self.assertEqual(multiply(3,4),4)
   # def test_strings_a_3(self):
    #    self.assertEqual( multiply(4,3), 4)

if __name__ == '__main__':
    unittest.main()