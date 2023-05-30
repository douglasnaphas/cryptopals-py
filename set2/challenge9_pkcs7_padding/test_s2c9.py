import unittest
from parameterized import parameterized
from utils.utils import Utils


class TestS2C9(unittest.TestCase):
    @parameterized.expand(
        [
            ("YELLOW SUBMARINE", 20, "YELLOW SUBMARINE\x04\x04\x04\x04"),
            ("YELLOW SUBMARINE", 17, "YELLOW SUBMARINE\x04")
        ]
    )
    def test_pad2(self, s, l, expected):
        self.assertEqual(Utils.pad(s, l), expected)
