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
