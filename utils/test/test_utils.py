import unittest
from parameterized import parameterized
from utils.utils import Utils

class TestNby(unittest.TestCase):
    @parameterized.expand([
        (0, 1), (1, 1), (255, 1), (256, 2), (1 << 15, 2), (1 << 16, 3),
        (123456, 3)
    ])
    def test_nby(self, n, expected):
        self.assertEqual(Utils.nby(n), expected)
