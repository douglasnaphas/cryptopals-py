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

    @parameterized.expand([
        ( "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d",
          "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t" ),
        ( "446561646c792c207768656e20492068656172206120646f7065206d656c6f6479",
          "RGVhZGx5LCB3aGVuIEkgaGVhciBhIGRvcGUgbWVsb2R5" ),
        ( "416e797468696e67206c657373207468616e20746865206265737420697320612066656c6f6e79",
          "QW55dGhpbmcgbGVzcyB0aGFuIHRoZSBiZXN0IGlzIGEgZmVsb255" ),
    ])
    def test_p(self, hx, expected):
        self.assertEqual(S1C1.hex_to_base64(hx), expected)
