import unittest
from set1.challenge2_fixed_XOR.s1c2 import S1C2
from parameterized import parameterized

class TestS1C2(unittest.TestCase):
    @parameterized.expand([
        ( "1c0111001f010100061a024b53535009181c",
          "686974207468652062756c6c277320657965",
          "746865206b696420646f6e277420706c6179" ),
    ])
    def test_fixed_XOR(self, a, b, expected):
        self.assertEqual(S1C2.fixed_XOR(a, b), expected)
