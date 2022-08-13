# https://en.wikipedia.org/wiki/HKDF

# Imports
from math import ceil

# HMAC based Key Derivation Function Class
class HKDF:
    def __init__(self, input_key_material, prf, salt = b'', info = b'', length = 32):
        self.salt = salt if len(salt) else bytes([0] * 32)

        self.ikm = input_key_material
        self.length = length 
        self.info = info
        self.prf = prf

    # HKDF Function
    def hkdf(self):
        prk = self.prf(self.salt, self.ikm)

        temp = b''
        output = b''
        for q in range(ceil(self.length / 32)):
            temp = self.prf(prk, temp + self.info + bytes([q + 1]))
            output += temp

        return output[:self.length]