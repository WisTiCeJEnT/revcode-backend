import unittest
from mult import multiply
class Testmultiply(unittest.TestCase):
  #  def setUp(self):
   #     pass
    def test_numbers_3_4(self):
        self.assertEqual(multiply(3,4),4)
    def test_strings_a_3(self):
        self.assertEqual( multiply(4,3), 4)

if __name__ == '__main__':
    unittest.main()