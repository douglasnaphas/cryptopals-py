import unittest
from parameterized import parameterized
from utils.aes import AES
from utils.utils import Utils

class TestAesEcb(unittest.TestCase):
    def test_decrypt_first_block_7txt(self):
        first_144_bits_b64 = 'CRIwqt4+szDbqkNY+I0qb' + 'D' + 'e3'
        # convert to a number, then 0-out the last 144 - 128 bits
        first_144_bits_number = Utils.b64toInt(first_144_bits_b64)
        
        
