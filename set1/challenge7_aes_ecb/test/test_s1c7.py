import unittest
from parameterized import parameterized
from set1.challenge7_aes_ecb.s1c7 import S1C7
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


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
        self.assertEqual(S1C7.s1c7(ciphertext), expected)
        key = bytes.fromhex('YELLOW SUBMARINE'.encode('utf-8').hex())
        cipher = Cipher(algorithms.AES(key), modes.ECB())
        encryptor = cipher.encryptor()
        ct = encryptor.update(ciphertext.encode("utf-8")) + encryptor.finalize()
        decryptor = cipher.decryptor()
        result = decryptor.update(ct) + decryptor.finalize()
        print(ciphertext)
        print(ct)
        print(result)
