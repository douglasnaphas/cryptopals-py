import argparse
import functools
import sys
from utils.utils import Utils

# To see the desired result from https://cryptopals.com/sets/1/challenges/5,
# run:
# cat set1/challenge5_repeating_XOR/stanza-no-nls.txt | tr -d '\n' | \
# python -m set1.challenge5_repeating_XOR.s1c5 -k 'ICE'

def main():
    parser = argparse.ArgumentParser(description='Encrypt with repeated XOR')
    parser.add_argument('-k', '--key', type=str, required=True,
                        help='the key to encrypt with')
    args = parser.parse_args()
    for line in sys.stdin:
        print(Utils.repeated_XOR_encrypt(line, args.key))

if __name__ == "__main__":
    main()


