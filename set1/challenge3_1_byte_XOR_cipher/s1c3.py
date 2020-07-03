#import sys
#sys.path.append('../../utils')
#sys.path.append('../..')
from utils.utils import Utils
from set1.challenge2_fixed_XOR.s1c2 import S1C2

# Run with:
# python -m set1.challenge3_1_byte_XOR_cipher.s1c3

class S1C3():
    @staticmethod
    def repeated_XOR(s, k):
        """Return s XOR'd with k, repeated.

        Positional arguments:
        s -- The string to XOR, hex-encoded, for example, '436f' means 'Co'
        k -- The key to repeat and XOR against s, for example, 'X'

        Examples:
        # XOR '1b37373331363f', which encodes 'Cooking', with 'X'
        repeated_XOR('1b37373331363f', 'X')
        '1b37373331363f'

        # Odd number of quartets, like 0xabc
        """
        return ""

    @classmethod
    def decipher_1_byte_XOR(cls, ctext):
        """Return a tuple containing the deciphered ctext, and the 1-byte key.
        pre: ctext is enciphered via XOR with one a single-character key.
        """
        return ""

    @classmethod
    def xor_w_1_char(cls, char):
        pass

    @classmethod
    def xor_w_all_lowercase(cls):
        pass

    @classmethod
    def get_candidate_keys(cls, blen):
        """Print 
        """ 

def main():
    # get the input string as a number
    ctext = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

    # get the set of possible key characters (one character each)
    FIRST_PRINTABLE_DEC = 32
    LAST_PRINTABLE_DEC = 126
    candidate_chars = set(range(FIRST_PRINTABLE_DEC, LAST_PRINTABLE_DEC + 1))

    e = {cc : Utils.repeated_XOR(ctext, chr(cc)) for cc in candidate_chars}
    loscore = 100
    lokey = 'nothing'
    loval = 'nothing'
    for k, v in e.items():
        try:
            score = Utils.score_english(v)
            if score < 0.24:
                print(k, " : ", score, " : ", v)
            if score < loscore:
                loscore = score
                lokey = k
                loval = v
        except:
            pass
    print(lokey, " : ", loscore, " : ", loval)


if __name__ == "__main__":
    main()


