import unittest
from parameterized import parameterized
from set1.challenge7_aes_ecb.s1c7 import S1C7
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import base64


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
        ct = encryptor.update(bytes(ciphertext.encode("utf-8"))) + encryptor.finalize()
        decryptor = cipher.decryptor()
        result = decryptor.update(ct) + decryptor.finalize()
        # print(ciphertext)
        # print(ct)
        # print(result)
        key2 = bytes.fromhex('YELLOW SUBMARINE'.encode('utf-8').hex())
        # print(key2)
        cipher2 = Cipher(algorithms.AES(key), modes.ECB())
        encryptor2 = cipher.encryptor()
        message2 = expected
        # print(message2)
        message_bytes2 = bytes(message2.encode("utf-8"))
        # print(message_bytes2)
        padder2 = padding.PKCS7(128).padder()
        padded_message_bytes2_except_last_byte = padder2.update(message_bytes2)
        padded_message_bytes2 = padded_message_bytes2_except_last_byte + padder2.finalize()
        # print(padded_message_bytes2)
        ct2 = encryptor2.update(padded_message_bytes2) + encryptor2.finalize()
        # print(ct2)
        ct2b64 = base64.b64encode(ct2)
        # print(ct2b64)

    @parameterized.expand([
        ('set1/challenge7_aes_ecb/test/7.txt',
         'set1/challenge7_aes_ecb/test/7.decrypted.txt'),
         ('set1/challenge7_aes_ecb/test/7b.txt',
         'set1/challenge7_aes_ecb/test/7b.decrypted.txt')
    ])
    def test_decrypting_files2(self, infile_name, exfile_name):
        with open(infile_name, 'r') as infile:
            encrypted_text = infile.read()
        with open(exfile_name, 'r') as exfile:
            expected_decrypted_text = exfile.read()
        self.assertEqual(S1C7.s1c7(encrypted_text), expected_decrypted_text)