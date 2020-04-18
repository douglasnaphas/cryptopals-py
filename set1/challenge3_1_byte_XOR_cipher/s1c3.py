#import sys
#sys.path.append('../../utils')
#sys.path.append('../..')
from utils.utils import Utils
from set1.challenge2_fixed_XOR.s1c2 import S1C2

# Run with:
# python -m set1.challenge3_1_byte_XOR_cipher.s1c3

class S1C3():
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
    print("Hello")
    # we will use S1C2.fixed_XOR(hex string, hex string)

    # get the input string as a number
    ctext = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    ctn = Utils.hexstr2num(ctext)
    
    # get the length of the input
    ctlen = int(len(ctext) / 2)

    # get the set of possible key characters (one character each)
    FIRST_PRINTABLE_DEC = 32
    LAST_PRINTABLE_DEC = 126
    candidate_chars = set(range(FIRST_PRINTABLE_DEC, LAST_PRINTABLE_DEC + 1))

    # for each candidate char, make what the key would be by reproducing it
    # ctlen times, and save its score in a dictionary keyed on the key char
    d = {cc : Utils.score_english(S1C2.fixed_XOR(ctext, hex(ord(chr(cc)))[2:])) for cc in candidate_chars}
#    print(d)
#    print(e)
    f = {cc : hex(ord(chr(cc)))[2:] * ctlen for cc in candidate_chars}
    for k, v in f.items():
        print(k, ' : ', v)
    e = {cc : S1C2.fixed_XOR(ctext, hex(ord(chr(cc)))[2:] * ctlen) for cc in candidate_chars}
    for k, v in e.items():
        print(k, ' : ', v)
    g = {k : bytes.fromhex(v).decode('utf-8') for k, v in e.items()}
    # exclude anything in the 


#    h = {k : Utils.score_english(v) for k, v in g.items()}
#    for k, v in h.items():
#        print(k, ' : ', v)
    
    

    



if __name__ == "__main__":
    main()


