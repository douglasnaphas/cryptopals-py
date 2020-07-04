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
    print(ct)

if __name__ == "__main__":
    main()


