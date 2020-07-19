import math
import numpy
import string
from collections import Counter
import functools
import base64

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
    def score_english(cls, txt, spaces=False):
        """Return the Euclidean distance between txt and a vector representing
        the frequency of characters in English.

        Lower numbers mean txt is more likely to be English.

        Examples:
        # should be True
        score_english('This is some normal text in English') < score_english('zzzzqqqqqq')

        # should be False
        score_english('No, this is text with spaces', True) < score_english('ThisIsTextWithNoSpaces')

        # should be True
        score_english('With and without spaces') == score_english('WithAndWithoutSpaces')

        Positional argument:
        txt -- The string to score.

        Optional keyword argument:
        spaces -- boolean, whether to consider spaces, default false
        """
        for c in txt:
            if c not in string.printable:
                return 100 # return a bad score if there are any unprintable characters
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
        common_f_w_spaces = [
            ("a",  0.0651738),
            ("b",  0.0124248),
            ("c",  0.0217339),
            ("d",  0.0349835),
            ("e",  0.1041442),
            ("f",  0.0197881),
            ("g",  0.0158610),
            ("h",  0.0492888),
            ("i",  0.0558094),
            ("j",  0.0009033),
            ("k",  0.0050529),
            ("l",  0.0331490),
            ("m",  0.0202124),
            ("n",  0.0564513),
            ("o",  0.0596302),
            ("p",  0.0137645),
            ("q",  0.0008606),
            ("r",  0.0497563),
            ("s",  0.0515760),
            ("t",  0.0729357),
            ("u",  0.0225134),
            ("v",  0.0082903),
            ("w",  0.0171272),
            ("x",  0.0013692),
            ("y",  0.0145984),
            ("z",  0.0007836),
            (" ",  0.1918182),
        ]
        if spaces:
            f = common_f_w_spaces
        else:
            f = common_f
        v = numpy.array(list(map(lambda t: t[1], f)))
        return numpy.linalg.norm(cls.str2ltrv(txt, spaces) - v)

    @staticmethod
    def str2ltrv(s, spaces=False):
        """"String to letter vector

        Examples:
        str2ltrv('babB') # [1, 3, 0, 0, 0, ...] length 26
        str2ltrv('babB', True) # [1, 3, 0, 0, 0, ..., 0] length 27
        str2ltrv('bab B', True) # [1, 3, 0, 0, 0, ..., 1] length 27
        str2ltrv('bab B\t\nc', True) # [1, 3, 1, 0, 0, ..., 3] length 27

        Positional argument:
        s -- The string to convert to a letter vector

        Optional keyword argument:
        spaces -- boolean, whether to count spaces, default False
        """
        if not isinstance(s, str):
            raise Exception("str2ltrv: input must be a string")
        alpha_len = 26
        if spaces:
            alpha_len = 27
        if len(s) == 0:
            return numpy.array([0] * alpha_len)
        lowers = str.lower(s)
        d = dict(Counter(lowers).items())
        alpha = list(string.ascii_lowercase)
        if(spaces):
            alpha.append(' ')
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

    @staticmethod
    def repeated_XOR_decrypt(s, k):
        """Decrypt a hex-encoded (no leading '0x') string by repeated XOR with k

        Positional arguments:
        s -- The string to decrypt, example '1b373733', which means
            0001 1011 0011 0111 0011 0111 0011 0011
        k -- The key to XOR s against, for example 'X', or 'Xyz'
        """
        if s == '':
            return ''
        return ''.join(
            [
                chr(int(y, 16) ^ ord(k[i % len(k)])) for i, y in
                enumerate([''.join(x) for x in zip(s[0::2], s[1::2])])
            ]
            )
    
    @staticmethod
    def repeated_XOR_encrypt(s, k, llen=75):
        """Encrypt a plaintext string by repeat-XOR-ing it with k, hex-encode
        the outcome
        """
        if s == '':
            return ''
        return ''.join(list(map(lambda x: hex(x)[2:] if x > 16 else '0' + hex(x)[2:], [ord(c) ^ ord(k[i % len(k)]) for i, c in enumerate(s)])))
    
    @classmethod
    def decrypt_1_byte_XOR(cls, ctext):
        """Decrypt a hex-encoded string encrypted with a single-byte XOR

        Return a tuple containing:
        - the ASCII code point of the key
        - the key
        - the score (lower is better) of the winning key
        - the message decrypted using the winning key

        Example:
        # From https://cryptopals.com/sets/1/challenges/3
        decrypt_1_byte_XOR('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')
        (88, 'X', 0.22531424758579757, 'Cooking MC\'s like a pound of bacon')
        """
        # get the set of possible key characters (one character each)
        FIRST_PRINTABLE_DEC = 32
        LAST_PRINTABLE_DEC = 126
        candidate_chars = set(range(FIRST_PRINTABLE_DEC, LAST_PRINTABLE_DEC + 1))
        e = {cc : cls.repeated_XOR_decrypt(ctext, chr(cc)) for cc in candidate_chars}
        loscore = 100
        lokey = 0
        loval = 'nothing'
        for k, v in e.items():
            try:
                score = cls.score_english(v, True)
                if score < loscore:
                    loscore = score
                    lokey = k
                    loval = v
            except:
                pass
        return (lokey, chr(lokey), loscore, loval)

    @staticmethod
    def hd(n1, n2):
        s = 0
        while n1 | n2:
            s = int(s) + int(1 & (n1 ^ n2))
            n1 = n1 >> 1
            n2 = n2 >> 1
        return s
    
    @classmethod
    def hamming(cls, s1, s2):
        """"Return the Hamming distance (the number of bits that differ)
        between s1 and s2.

        For example:
        hamming("this is a test", "wokka wokka!!!") # 37

        Positional arguments:
        s1 -- String
        s2 -- String
        """
        return functools.reduce(
            lambda acc, curr: acc + curr,
            [cls.hd(ord(t[0]), ord(t[1])) for t in list(zip(s1, s2))]
        )

    @classmethod
    def hamming_bytearray(cls, ba1, ba2):
        """"Return the Hamming distance (the number of bits that differ)
        between bytearrays ba1 and ba2.

        For example:
        hamming(b'this is a test', b'wokka wokka!!!') # 37

        Positional arguments:
        ba1 -- bytearray
        ba2 -- bytearray
        """
        return functools.reduce(
            lambda acc, curr: acc + curr,
            [cls.hd(t[0], t[1]) for t in list(zip(ba1, ba2))]
        )
    
    @staticmethod
    def buildStringFromTextIOWrapper(textIOWrapper):
        """Iterate over the lines in textIOWrapper, concat them into a string
        with no newlines

        Required positional argument:
        textIOWrapper -- Something that allows `for line in textIOWrapper`
        """
        s = ""
        for line in textIOWrapper:
            s = s + line.rstrip()
        return s
    
    @staticmethod
    def b64toInt(b64):
        return int.from_bytes(base64.b64decode(b64), 'big')
    
    @staticmethod
    def b64_to_bytearray(b64):
        return bytearray(base64.b64decode(b64))

    @classmethod
    def hdist_by_ksize(cls, s, keylens, npairs=1):
        ct = cls.b64_to_bytearray(s)
        hbk = {}
        for ks in keylens:
            for n in range(npairs):
                hbk[ks] = hbk.get(ks, 0) + cls.hamming_bytearray(      # increment the total distance, then divide by ks and npairs outside
                    ct[ks * 2 * n: ks * (2 * n + 1)], # the loops
                    ct[ks * (2 * n + 1):ks * (2 * n + 2)]
                ) / ks
            hbk[ks] = hbk[ks] / npairs
        return hbk