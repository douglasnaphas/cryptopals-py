import unittest
from parameterized import parameterized
from set1.challenge3_1_byte_XOR_cipher.s1c3 import S1C3

class TestS1C3(unittest.TestCase):
    def test_s1c3(self):
        self.assertEqual(S1C3.s1c3()[3], 'Cooking MC\'s like a pound of bacon')
