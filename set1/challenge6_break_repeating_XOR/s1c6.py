# run with:
# cat set1/challenge6_break_repeating_XOR/6.txt | python -m set1.challenge6_break_repeating_XOR.s1c6

import argparse
import functools
import sys
from utils.utils import Utils

def main():
    parser = argparse.ArgumentParser(description='Encrypt with repeated XOR')
    parser.add_argument('-k', '--key', type=str, required=False,
                        help='the key to encrypt with') # might not need this
    args = parser.parse_args()
    cs = Utils.buildStringFromTextIOWrapper(sys.stdin)
    ct = Utils.b64_to_bytearray(cs)
    MIN_KEYSIZE = 2
    MAX_KEYSIZE = 40
    hds = {ks: Utils.hamming_bytearray(ct[0:ks], ct[ks:2 * ks]) for ks in range(MIN_KEYSIZE, MAX_KEYSIZE + 1)}
    hds = Utils.hdist_by_ksize(cs, list(range(MIN_KEYSIZE, MAX_KEYSIZE + 1)))
    print(hds)

if __name__ == "__main__":
    main()


