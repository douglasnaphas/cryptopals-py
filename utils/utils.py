import math
import numpy
import string
from collections import Counter

class Utils():
    
    @staticmethod
    def nby(n):
        """Return the number of bytes (>=1) to represent int n.

        Throw on non-int n.
        
        Positional argument:
        n -- The int to represent.
        """
        if n == 0:
            return 1
        return math.ceil(n.bit_length() / 8)

    @staticmethod
    def score_english(txt):
        """Return the Euclidean distance between txt and a vector representing
        the frequency of characters in English.

        Positional argument:
        txt -- The string to score.
        """
        return 0

    # something based on
    # functools.reduce(lambda beg, inc : beg + ord(inc), 'abcdefghijklmnopqrstuvwxyz', 0)
    # and ascii_lowercase

    @staticmethod
    def str2ltrv(s):
        """"String to letter vector
        """
        if not isinstance(s, str):
            raise Exception("str2ltrv: input must be a string")
        d = dict(Counter(str.lower(s)).items())
        alpha = list(string.ascii_lowercase)
        v = list(map(lambda ltr : d.get(ltr, 0), alpha))
        return numpy.array(v)
