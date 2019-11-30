import unittest
from parameterized import parameterized
from set1.challenge3_1_byte_XOR_cipher.s1c3 import S1C3

class TestS1C3(unittest.TestCase):
    @parameterized.expand([
        ("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
    ])
    def test_decipher_1_byte_XOR(self, a):
        pass
