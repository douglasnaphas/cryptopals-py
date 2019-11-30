import math
import base64

class S1C1():
    @staticmethod
    def ret_true():
        return True

    @staticmethod
    def hex_to_base64(hx):
        hx_str = '0x' + hx
        n = int(hx_str, 16)
        num_bytes = math.ceil(n.bit_length() / 8)
        b = (n).to_bytes(num_bytes, 'big')
        return str(base64.b64encode(b))[2:-1]
