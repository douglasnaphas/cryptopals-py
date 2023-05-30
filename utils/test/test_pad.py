import unittest
from parameterized import parameterized
from utils.utils import Utils


class TestPad(unittest.TestCase):
    @parameterized.expand(
        [
            ("ABCD", 9, "ABCD\x04\x04\x04\x04\x04"),
            ("\x04\x04", 3, "\x04\x04\x04")
        ]
    )
    def test_pad(self, s, l, expected):
        self.assertEqual(Utils.pad(s, l), expected)