import argparse
import functools
import sys
from utils.utils import Utils

def main():
    parser = argparse.ArgumentParser(description='Encrypt with repeated XOR')
    parser.add_argument('-k', '--key', type=str, required=True,
                        help='the key to encrypt with')
    args = parser.parse_args()
    ct = Utils.buildStringFromTextIOWrapper(sys.stdin)
    MIN_KEYSIZE = 2
    MAX_KEYSIZE = 8
    # need to convert the input string to a number
    # maybe get a byte array?

    hds = {ks: Utils.hamming(ct[0:ks], ct[ks:2 * ks]) for ks in range(MIN_KEYSIZE, MAX_KEYSIZE + 1)}
    print(hds)

if __name__ == "__main__":
    main()


