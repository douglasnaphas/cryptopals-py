import unittest
from set1.challenge1_convert_hex_to_base64.s1c1 import S1C1
from parameterized import parameterized

class TestCanary(unittest.TestCase):
    def test_succeed(self):
        self.assertTrue(True)

    def test_import(self):
        self.assertTrue(S1C1.ret_true())

    @parameterized.expand([
        (2, 2, 4),
        (1, 1, 2),
    ])
    def test_p(self, a, b, expected):
        self.assertEqual(a + b, expected)
