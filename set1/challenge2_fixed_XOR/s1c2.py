class S1C2():
    @staticmethod
    def fixed_XOR(a, b):
        int_a = int('0x' + str(a), 16)
        int_b = int('0x' + str(b), 16)
        return hex(int_a ^ int_b)[2:]
