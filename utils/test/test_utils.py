import unittest
from parameterized import parameterized
from utils.utils import Utils
import numpy

class TestNby(unittest.TestCase):
    @parameterized.expand([
        (0, 1), (1, 1), (255, 1), (256, 2), (1 << 15, 2), (1 << 16, 3),
        (123456, 3)
    ])
    def test_nby(self, n, expected):
        self.assertEqual(Utils.nby(n), expected)

class TestStr2Ltrv(unittest.TestCase):
    @parameterized.expand([
        ('a', numpy.array([1 / 1] + [0] * 25)),
        ('ab', numpy.array([1 / 2] * 2 + [0] * 24)),
        ('zbaacccccb', numpy.array([2 / 10] * 2 +
                                   [5 / 10] +
                                   [0] * 22 +
                                   [1 / 10])),
        ('', numpy.array([0] * 26))
    ])
    def test_str2ltrv(self, s, expected):
        self.assertTrue(numpy.array_equal(Utils.str2ltrv(s), expected))

class TestScoreEnglish(unittest.TestCase):
    @parameterized.expand([('a', 0)])
    def test_score_english(self, s, expected):

        common_f = [
            ('a', 0.08167),
            ('b', 0.01492),
            ('c', 0.02202),
            ('d', 0.04253),
            ('e', 0.12702),
            ('f', 0.02228),
            ('g', 0.02015),
            ('h', 0.06094),
            ('i', 0.06966),
            ('j', 0.00153),
            ('k', 0.01292),
            ('l', 0.04025),
            ('m', 0.02406),
            ('n', 0.06749),
            ('o', 0.07507),
            ('p', 0.01929),
            ('q', 0.00095),
            ('r', 0.05987),
            ('s', 0.06327),
            ('t', 0.09356),
            ('u', 0.02758),
            ('v', 0.00978),
            ('w', 0.0256),
            ('x', 0.0015),
            ('y', 0.01994),
            ('z', 0.00077)
        ]
        self.assertEqual(Utils.score_english(s), expected)
