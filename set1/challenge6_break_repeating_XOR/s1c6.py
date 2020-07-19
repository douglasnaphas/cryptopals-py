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
    MIN_KEYSIZE = 2
    MAX_KEYSIZE = 40
    hds = Utils.hdist_by_ksize(cs, list(range(MIN_KEYSIZE, MAX_KEYSIZE + 1)), 2)
    # print(hds)
    for k, v in hds.items():
        print(k, '->', v) if v < 3 else False

if __name__ == "__main__":
    main()


