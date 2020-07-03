from utils.utils import Utils

# Run with:
# python -m set1.challenge3_1_byte_XOR_cipher.s1c3

class S1C3:
    @staticmethod
    def s1c3():
        ctext = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
        return Utils.decrypt_1_byte_XOR(ctext)


def main():
    print(S1C3.s1c3())


if __name__ == "__main__":
    main()


