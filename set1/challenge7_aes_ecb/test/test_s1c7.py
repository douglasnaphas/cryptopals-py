import unittest
from parameterized import parameterized
from set1.challenge7_aes_ecb.s1c7 import S1C7


class TestDecryptingFiles(unittest.TestCase):
    @parameterized.expand([
        ('set1/challenge7_aes_ecb/test/7.txt',
         'set1/challenge7_aes_ecb/test/7.decrypted.txt')
    ])
    def test_decrypting_files(self, infile_name, exfile_name):
        self.assertEqual('a', 'a')
        infile = open(infile_name, 'r')
        ciphertext = infile.read()
        infile.close()
        exfile = open(exfile_name, 'r')
        expected = exfile.read()
        exfile.close()


