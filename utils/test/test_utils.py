import unittest
from parameterized import parameterized
from utils.utils import Utils
import numpy
import functools

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
    def test_str2ltrv_spaces_false(self, s, expected):
        self.assertTrue(numpy.array_equal(Utils.str2ltrv(s), expected))

    @parameterized.expand([
        ('a', numpy.array([1 / 1] + [0] * 26)),
        ('ab', numpy.array([1 / 2] * 2 + [0] * 25)),
        ('zbaacccccb', numpy.array([2 / 10] * 2 +
                                   [5 / 10] +
                                   [0] * 22 +
                                   [1 / 10] +
                                   [0])),
        ('', numpy.array([0] * 27))
    ])
    def test_str2ltrv_spaces_true(self, s, expected):
        self.assertTrue(numpy.array_equal(Utils.str2ltrv(s, True), expected))

    @parameterized.expand([
        ('x', 'x'),
        ('x', 'x '),
        ('Something with upper- and lower-case...AND punctuation!!! #string',
         'somethingwithupperandlowercaseandpunctuationstring')
    ])
    def test_str2ltrv_spaces_false_non_letter(self, a, b):
        self.assertTrue(numpy.array_equal(Utils.str2ltrv(a), Utils.str2ltrv(b)))

class TestScoreEnglish(unittest.TestCase):
    def test_score_english_huge_strings_spaces_false(self):
        common_f = [
            ('a', .08129 ),
            ('b', .01485 ),
            ('c', .02192 ),
            ('d', .04233 ),
            ('e', .12646 ),
            ('f', .02218 ),
            ('g', .02006 ),
            ('h', .06066 ),
            ('i', .06934 ),
            ('j', .00152 ),
            ('k', .01286 ),
            ('l', .04006 ),
            ('m', .02395 ),
            ('n', .06718 ),
            ('o', .07472 ),
            ('p', .0192  ),
            ('q', .00095 ),
            ('r', .05959 ),
            ('s', .06298 ),
            ('t', .09313 ),
            ('u', .02745 ),
            ('v', .00973 ),
            ('w', .02548 ),
            ('x', .00149 ),
            ('y', .01985 ),
            ('z', .00077 ),
        ]
        scale_factor = 100000
        denom = functools.reduce(lambda beg, inc : beg + inc[1] * scale_factor,
                                 common_f,
                                 0)
        s = functools.reduce(lambda beg, inc : beg + inc[0] * int(inc[1] * scale_factor),
                             common_f,
                             '')
        expected = 0
        error_margin = .0001
        score = Utils.score_english(s)
        self.assertTrue(abs(score - expected)  < error_margin)
        s_plus_v = functools.reduce(lambda beg, inc : beg + inc[0] * int(inc[1] * scale_factor),
                             common_f,
                             'v')
        worse_score = Utils.score_english(s_plus_v)
        self.assertTrue(worse_score > score)

    def test_score_english_huge_strings_spaces_true(self):
        common_f = [
            ('a', .08129 ),
            ('b', .01485 ),
            ('c', .02192 ),
            ('d', .04233 ),
            ('e', .12646 ),
            ('f', .02218 ),
            ('g', .02006 ),
            ('h', .06066 ),
            ('i', .06934 ),
            ('j', .00152 ),
            ('k', .01286 ),
            ('l', .04006 ),
            ('m', .02395 ),
            ('n', .06718 ),
            ('o', .07472 ),
            ('p', .0192  ),
            ('q', .00095 ),
            ('r', .05959 ),
            ('s', .06298 ),
            ('t', .09313 ),
            ('u', .02745 ),
            ('v', .00973 ),
            ('w', .02548 ),
            ('x', .00149 ),
            ('y', .01985 ),
            ('z', .00077 ),
        ]
        scale_factor = 100000
        denom = functools.reduce(lambda beg, inc : beg + inc[1] * scale_factor,
                                 common_f,
                                 0)
        s = functools.reduce(lambda beg, inc : beg + inc[0] * int(inc[1] * scale_factor),
                             common_f,
                             '')
        expected = 0
        error_margin = .0001
        score = Utils.score_english(s)
        self.assertTrue(abs(score - expected)  < error_margin)
        s_plus_v = functools.reduce(lambda beg, inc : beg + inc[0] * int(inc[1] * scale_factor),
                             common_f,
                             'v')
        worse_score = Utils.score_english(s_plus_v)
        self.assertTrue(worse_score > score)

class TestHexstr2num(unittest.TestCase):
    @parameterized.expand([
        ('1d2A', 7466),
        ('1dA', 474)
    ])
    def test_hexstr2num(self, hexstr, expected):
        self.assertEqual(Utils.hexstr2num(hexstr), expected)

class TestRepeatedXOR(unittest.TestCase):
    @parameterized.expand([
        ('', '', ''),
        ('1b', 'X', 'C'),
        ('1b373733', 'X', 'Cook'),
        ('1b373733', 'XX', 'Cook'),
        ('1b373733', 'Xy', 'CNoJ'),
    ])
    def test_repeated_XOR(self, s, k, expected):
        self.assertEqual(Utils.repeated_XOR(s, k), expected)

class TestDecrypt1ByteXOR(unittest.TestCase):
    @parameterized.expand([
        ('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736',
        (88, 'X', 0.22531424758579757, 'Cooking MC\'s like a pound of bacon'))
    ])
    def test_decrypt_1_byte_XOR(self, ctext, expected):
        self.assertEqual(Utils.decrypt_1_byte_XOR(ctext), expected)
