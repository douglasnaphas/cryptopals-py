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
    parser.add_argument('--print-keysizes', action='store_true')
    parser.add_argument('-n', '--npairs', required=False, default=1, type=int)
    args = parser.parse_args()
    npairs = args.npairs
    print_keysizes = args.print_keysizes
    cs = Utils.buildStringFromTextIOWrapper(sys.stdin)
    MIN_KEYSIZE = 2
    MAX_KEYSIZE = 40
    print(args)
    hds = Utils.hdist_by_ksize(cs, list(range(MIN_KEYSIZE, MAX_KEYSIZE + 1)), npairs)
    hds_sorted = sorted(
        [(keysize, distance) for keysize, distance in hds.items()],
        key=lambda t: t[1]
    )
    if print_keysizes:
        for t in hds_sorted:
            print(t[0], ' -> ', t[1])


if __name__ == "__main__":
    main()


