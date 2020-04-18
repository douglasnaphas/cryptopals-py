import math
import numpy
import string
from collections import Counter
import functools

class Utils():
    
    @staticmethod
    def nby(n):
        """Return the number of bytes (>=1) to represent int n.

        ex: 255 -> 1
            256 -> 2

        Throw on non-int n.
        
        Positional argument:
        n -- The int to represent.
        """
        if n == 0:
            return 1
        return math.ceil(n.bit_length() / 8)

    @classmethod
    def score_english(cls, txt):
        """Return the Euclidean distance between txt and a vector representing
        the frequency of characters in English.

        Positional argument:
        txt -- The string to score.
        """
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
        v = numpy.array(list(map(lambda t: t[1], common_f)))
        return numpy.linalg.norm(cls.str2ltrv(txt) - v)

    # something based on
    # functools.reduce(lambda beg, inc : beg + ord(inc), 'abcdefghijklmnopqrstuvwxyz', 0)
    # and ascii_lowercase


# function that gets the distance between two letter vectors, test with easy vectors

# function that calls ^^^ with arg and common_f, use mocking to test that ^^^
# was called with the right args

    @staticmethod
    def str2ltrv(s):
        """"String to letter vector
        ex: 'babB' -> [1, 3, 0, 0, 0, ... ]
        """
        if not isinstance(s, str):
            raise Exception("str2ltrv: input must be a string")
        if len(s) == 0:
            return numpy.array([0] * 26)
        lowers = str.lower(s)
        d = dict(Counter(lowers).items())
        alpha = list(string.ascii_lowercase)
        denom = functools.reduce(
            lambda beg, inc : (beg + 1) if inc.islower() else beg,
            lowers,
            0
        )
        v = list(map(lambda ltr : d.get(ltr, 0) / denom, alpha))
        return numpy.array(v)

    @staticmethod
    def hexstr2num(hexstr):
        """Convert an un-prefixed hex string like '1d2A' into a number like 7466
        ex: '1dA' -> 474
        """
        return int('0x' + str(hexstr), 16)

    @staticmethod
    def num2ascii(num):
        """Convert a decimal number like 74
        """
        pass
