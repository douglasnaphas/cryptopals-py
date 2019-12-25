import math

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
