import unittest
from parameterized import parameterized
from utils.utils import Utils


class TestDetectDuplicateBlocks(unittest.TestCase):
    @parameterized.expand([
        (['aa'], 1, ['aa']),
        (['aa', 'ab'], 1, ['aa'])
    ])
    def test_detect_duplicate_blocks(self, strs, block_size, expected):
        self.assertEqual(Utils.detect_duplicate_blocks(strs, block_size), expected)
