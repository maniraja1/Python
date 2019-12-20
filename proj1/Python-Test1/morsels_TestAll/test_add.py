import unittest
from add import add
class TestAdd(unittest.TestCase):
    def test_2_plus_2(self): self.assertEqual(add(2, 2), 4)
    def test_2_plus_3(self): self.assertEqual(add(2, 3), 5)
unittest.main(verbosity=2)