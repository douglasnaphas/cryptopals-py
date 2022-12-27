import unittest
from parameterized import parameterized
from set1.challenge7_aes_ecb.s1c7 import S1C7

class TestDecryptingFiles(unittest.TestCase):
    @parameterized.expand([
        ('set1/challenge7_aes_ecb/test/7.txt', '7.decrypted.txt')
    ])
    def test_decrypting_files(self, infile, outfile):
        self.assertEqual('a', 'a')
        f = open(infile, 'r')
        ciphertext = f.read()
        f.close()


